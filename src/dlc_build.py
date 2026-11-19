"""Собрать src/dlc/<collection>.json из src/dlc_src/*.py.

Каждый модуль-описание задаёт: COLL, LABEL, E = {EN: (RU name, RU description | None)}, необязательно FOLDERS,
DV = {EN: "DV ..."} (таблица СЛ оружия), TABLES = {EN: {"name":..., "results": {range: text}}}, ACTORS (имена NPC),
EXTRA (dict с сырыми записями Babele).
"""
import glob
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
# Папка системы cyberpunk-red-core (0.92.4): переменная CPR_SYSTEM_DIR или соседняя cpr-v14-port/system
SYS = os.environ.get("CPR_SYSTEM_DIR") or os.path.join(os.path.dirname(os.path.dirname(HERE)), "cpr-v14-port", "system")

DV_RU = {k: v["name"] for k, v in json.load(open(os.path.join(SYS, "babele", "ru", "cyberpunk-red-core.internal_dv-tables.json"),
                                               encoding="utf-8"))["entries"].items()}
DV_RU.update({
    "DV Generic": "СЛ Общая",
    "DV Long-Barrel Pistol": "СЛ Удлинённый пистолет",
    "DV Snubnose Pistol": "СЛ Укороченный пистолет",
    "DV Subcompact SMG": "СЛ Субкомпактный ПП",
    "DV Short-Barrel Shotgun": "СЛ Укороченный дробовик",
    "DV Long-Barrel Shotgun": "СЛ Удлинённый дробовик",
    "DV Carbine": "СЛ Карабин",
    "DV Battle Rifle": "СЛ Боевая винтовка",
    "DV Marksman Rifle": "СЛ Марксманская винтовка",
    "DV Scout Rifle": "СЛ Скаутская винтовка",
    "DV Anti-materiel Rifle": "СЛ Крупнокалиберная снайперская винтовка",
    "DV Shortbow": "СЛ Короткий лук/арбалет",
    "DV Longbow": "СЛ Длинный лук/арбалет",
    "DV Missile Launcher": "СЛ Ракетная установка",
    "DV Machine Pistol (Autofire)": "СЛ Автоматический пистолет (Автоогонь)",
    "DV Machine Gun (Autofire)": "СЛ Пулемёт (Автоогонь)",
})


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class Pack:
    """Описание одной коллекции для модулей с несколькими паками (MULTI)."""

    def __init__(self, coll, label, actors=None, entries=None, folders=None):
        self.COLL, self.LABEL = coll, label
        self.ACTORS = actors or {}
        self.E = entries or {}
        if folders:
            self.FOLDERS = folders


def write(m, out_dir):
    entries = {}
    for en, val in getattr(m, "E", {}).items():
        name, desc = val if isinstance(val, tuple) else (val, None)
        e = {"name": name}
        if desc:
            e["description"] = desc
        dv = getattr(m, "DV", {}).get(en)
        if dv:
            e["dvTable"] = DV_RU.get(dv, dv)
        entries[en] = e
    for en, val in getattr(m, "TABLES", {}).items():
        entries[en] = val
    for en, val in getattr(m, "ACTORS", {}).items():
        entries[en] = val if isinstance(val, dict) else {"name": val}
    entries.update(getattr(m, "EXTRA", {}))
    data = {"entries": entries}
    if m.LABEL:
        data = {"label": m.LABEL, **data}
    mapping = dict(getattr(m, "MAPPING", {}))
    if getattr(m, "DV", None):
        mapping["dvTable"] = "system.dvTable"
    if mapping:
        data["mapping"] = mapping
    if getattr(m, "FOLDERS", None):
        data["folders"] = m.FOLDERS
    json.dump(data, open(os.path.join(out_dir, f"{m.COLL}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"  dlc {m.COLL}: {len(entries)} entries")


def build():
    out_dir = os.path.join(HERE, "dlc")
    os.makedirs(out_dir, exist_ok=True)
    for old in glob.glob(os.path.join(out_dir, "*.json")):
        os.remove(old)
    for path in sorted(glob.glob(os.path.join(HERE, "dlc_src", "*.py"))):
        m = load(path)
        for pack in getattr(m, "MULTI", None) or [m]:
            write(pack, out_dir)


if __name__ == "__main__":
    build()
