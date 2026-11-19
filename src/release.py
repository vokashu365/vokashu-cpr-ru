"""Pack module/ into dist/vokashu-cpr-ru.zip and copy module.json next to it for a GitHub release."""
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULE = ROOT / "module"
DIST = ROOT / "dist"


def main():
    meta = json.loads((MODULE / "module.json").read_text(encoding="utf-8"))
    version = meta["version"]
    expected = f"/releases/download/v{version}/{meta['id']}.zip"
    if not meta.get("download", "").endswith(expected):
        raise SystemExit(f"module.json download does not point to v{version}: {meta.get('download')}")

    DIST.mkdir(exist_ok=True)
    zip_path = DIST / f"{meta['id']}.zip"
    files = sorted(p for p in MODULE.rglob("*") if p.is_file())
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, p.relative_to(MODULE).as_posix())
    shutil.copyfile(MODULE / "module.json", DIST / "module.json")
    print(f"{zip_path.name}: {len(files)} files, {zip_path.stat().st_size // 1024} KB, v{version}")


if __name__ == "__main__":
    main()
