"""Собрать модуль vokashu-cpr-ru в ../module.

- lang/ru.json — только ключи системы CPR, которые меняются (навыки, роли, термины по книгам);
- babele/ru — полный перевод всех компендиумов системы (основа — перевод системы, названия по книгам)
  + переводы DLC-модулей из src/dlc/*.json.

python -I -X utf8 src/build.py
"""
import glob
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import glossary as G  # noqa: E402
import glossary_bc as GBC  # noqa: E402
import glossary_extra as GX  # noqa: E402

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "module")
# Папка системы cyberpunk-red-core (0.92.4): переменная CPR_SYSTEM_DIR или соседняя cpr-v14-port/system
SYS = os.environ.get("CPR_SYSTEM_DIR") or os.path.join(os.path.dirname(os.path.dirname(HERE)), "cpr-v14-port", "system")
SYSID = "cyberpunk-red-core"


def sub_terms(text, terms):
    for pat, rep in terms:
        def repl(m, rep=rep):
            r = rep(m) if callable(rep) else m.expand(rep)
            if m.group(0)[:1].isupper() and r[:1].islower():
                r = r[:1].upper() + r[1:]
            return r
        text = re.sub(pat, repl, text)
    return text


def fix_text(s):
    return sub_terms(sub_terms(s, G.TERMS), G.DESC_TERMS)


# ------------------------------------------------------------------ lang
def build_lang():
    ru = json.load(open(os.path.join(SYS, "lang", "ru.json"), encoding="utf-8"))
    en = json.load(open(os.path.join(SYS, "lang", "en.json"), encoding="utf-8"))
    out = {}
    for k, v in ru.items():
        if isinstance(v, str):
            n = sub_terms(v, G.TERMS)
            if n != v:
                out[k] = n
    for k, v in G.SKILLS.items():
        key = f"CPR.global.itemType.skill.{k}"
        assert key in en, key
        out[key] = v
    for k, v in G.LANG_KEYS.items():
        assert k in en or k in ru, k
        out[k] = v
    out.update(G.NEW_KEYS)
    return dict(sorted(out.items()))


# ------------------------------------------------------------------ item names
def weapon_name(en):
    m = re.match(r"^(.*) \((Poor|Excellent)\)$", en)
    if m and m.group(1) in G.WEAPON_BASE:
        return f"{G.WEAPON_BASE[m.group(1)]} ({G.QUALITY[m.group(2)]})"
    return G.WEAPON_BASE.get(en)


def ammo_name(en):
    m = re.match(r"^(.*) \((.*)\)$", en)
    if not m or m.group(1) not in G.AMMO_KIND or m.group(2) not in G.AMMO_TYPE:
        return None
    noun, gender = G.AMMO_KIND[m.group(1)]
    adj = G.AMMO_TYPE[m.group(2)][{"m": 0, "f": 1, "pl": 2}[gender]]
    return f"{noun} ({adj})"


def clothing_name(en):
    for style in G.CLOTHING_STYLE:
        if en.startswith(style + " "):
            t = en[len(style) + 1:]
            if t in G.CLOTHING_TYPE:
                return f"{G.CLOTHING_TYPE[t]} ({style})"
    return None


def upgrade_name(en):
    if en in G.UPGRADES_SIMPLE:
        return G.UPGRADES_SIMPLE[en]
    m = re.match(r"^(Drum Magazine|Extended Magazine) \((.*)\)$", en)
    if m and m.group(2) in G.WEAPON_BASE:
        w = G.WEAPON_BASE[m.group(2)]
        return f"{G.MAGAZINE[m.group(1)]} ({w[0].lower() + w[1:] if not w.startswith('ПП') else w})"
    return None


NAMERS = {
    "core_cyberware": G.CYBERWARE.get, "internal_cyberware-core": G.CYBERWARE.get,
    "core_weapons": weapon_name, "core_weapons-branded": G.BRANDED.get,
    "core_armor": G.ARMOR.get, "core_ammo": ammo_name, "core_gear": G.GEAR.get, "core_clothing": clothing_name,
    "core_drugs": G.DRUGS.get, "core_programs": G.PROGRAMS.get, "core_upgrades": upgrade_name,
    "core_vehicles": G.VEHICLES.get, "core_critical-injuries-body": G.CRIT_BODY.get,
    "core_critical-injuries-head": G.CRIT_HEAD.get, "core_roles": G.ROLES.get,
}
for _c in ("ammo", "armor", "clothing", "cyberware", "gear", "upgrades", "vehicles", "weapons"):
    NAMERS[f"black-chrome_{_c}"] = GBC.BC.get

EXTRA_NAMES = {
    "internal_dv-tables": {"DV Generic": "СЛ Общая", "DV Long-Barrel Pistol": "СЛ Удлинённый пистолет"},
    "internal_net-rolltables": {
        "All Other Floors (Basic)": "Остальные этажи (базовая)",
        "All Other Floors (Standard)": "Остальные этажи (стандартная)",
        "All Other Floors (Uncommon)": "Остальные этажи (необычная)",
        "All Other Floors (Advanced)": "Остальные этажи (продвинутая)",
        "Lobby": "Вестибюль",
    },
}


def fix_entry(v):
    if isinstance(v, str):
        return fix_text(v)
    if isinstance(v, dict):
        return {k: (x if k in ("dvTable",) else fix_entry(x)) for k, x in v.items()}
    if isinstance(v, list):
        return [fix_entry(x) for x in v]
    return v


def build_babele(report):
    dst = os.path.join(OUT, "babele", "ru")
    os.makedirs(dst, exist_ok=True)
    en_dir = os.path.join(SYS, "babele", "en")
    for f in sorted(glob.glob(os.path.join(SYS, "babele", "ru", f"{SYSID}.*.json"))):
        base = os.path.basename(f)
        coll = base[len(SYSID) + 1:-5]
        if not os.path.exists(os.path.join(en_dir, base)):
            continue  # устаревшие файлы перевода, которых нет в английском наборе
        data = json.load(open(f, encoding="utf-8"))
        namer = NAMERS.get(coll)
        extra = EXTRA_NAMES.get(coll, {})
        entries = {}
        renamed = 0
        for en_name, v in data.get("entries", {}).items():
            v = fix_entry(v) if isinstance(v, dict) else v
            new = (namer(en_name) if namer else None) or extra.get(en_name)
            if isinstance(v, dict) and new and v.get("name") != new:
                report.append(f"{coll}: {en_name}: {v.get('name')} → {new}")
                v = {**v, "name": new}
                renamed += 1
            entries[en_name] = v
        for en_name, ru_name in GX.EXTRA.get(coll, {}).items():
            entries.setdefault(en_name, {"name": ru_name})
        data["entries"] = entries
        if isinstance(data.get("label"), str):
            data["label"] = fix_text(data["label"])
        json.dump(data, open(os.path.join(dst, base), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    # DLC-модули: готовые переводы
    import dlc_build
    dlc_build.build()
    for f in sorted(glob.glob(os.path.join(HERE, "dlc", "*.json"))):
        shutil.copy2(f, os.path.join(dst, os.path.basename(f)))


def main():
    if os.path.isdir(os.path.join(OUT, "babele")):
        shutil.rmtree(os.path.join(OUT, "babele"))
    os.makedirs(os.path.join(OUT, "lang"), exist_ok=True)
    lang = build_lang()
    json.dump(lang, open(os.path.join(OUT, "lang", "ru.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    report = []
    build_babele(report)
    with open(os.path.join(ROOT, "build-report.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(report))
    print(f"lang keys: {len(lang)}; renamed entries: {len(report)}; babele files: {len(os.listdir(os.path.join(OUT, 'babele', 'ru')))}")


if __name__ == "__main__":
    main()
