#!/usr/bin/env python3
"""
compile_weights.py
Compile KhmerDigital.designspace → 9 TTF weights in ttf/
Run this after to_glyphs.py has already built master_ufo/ and KhmerDigital.designspace
"""
import os
import shutil
import subprocess
from fontTools.ttLib import TTFont

DS_FILE    = "KhmerDigital.designspace"
TARGET_DIR = "ttf"

MASTERS = [
    {"file": "KhmerDigital-Thin.ttf",    "weight": 100},
    {"file": "KhmerDigital-Regular.ttf", "weight": 400},
    {"file": "KhmerDigital-Black.ttf",   "weight": 900},
]

INSTANCES = [
    {"name": "Thin",       "weight": 100},
    {"name": "ExtraLight", "weight": 200},
    {"name": "Light",      "weight": 300},
    {"name": "Regular",    "weight": 400},
    {"name": "Medium",     "weight": 500},
    {"name": "SemiBold",   "weight": 600},
    {"name": "Bold",       "weight": 700},
    {"name": "ExtraBold",  "weight": 800},
    {"name": "Black",      "weight": 900},
]

OT_TABLES = ["GSUB", "GPOS", "GDEF", "gasp"]


def nearest_master_file(weight: int) -> str:
    return min(MASTERS, key=lambda m: abs(m["weight"] - weight))["file"]


def inject_ot_tables(compiled_path: str, weight: int) -> None:
    master_path = nearest_master_file(weight)
    if not os.path.exists(master_path):
        print(f"  WARNING: master '{master_path}' not found — skipping OT inject")
        return

    master_tt   = TTFont(master_path)
    compiled_tt = TTFont(compiled_path)

    if master_tt.getGlyphOrder() != compiled_tt.getGlyphOrder():
        print(f"  WARNING: glyph order mismatch in {compiled_path} — skipping OT inject")
        return

    injected = []
    for tag in OT_TABLES:
        if tag in master_tt:
            compiled_tt[tag] = master_tt[tag]
            injected.append(tag)

    compiled_tt.save(compiled_path)
    print(f"  [{os.path.basename(compiled_path)}]  injected {injected} from {master_path}")


def run():
    if not os.path.exists(DS_FILE):
        print(f"Error: '{DS_FILE}' not found. Run to_glyphs.py first.")
        return

    print("=" * 60)
    print("      COMPILING 9 STANDALONE WEIGHTS FROM DESIGNSPACE  ")
    print("=" * 60)

    subprocess.run([
        "fontmake", "-m", DS_FILE, "-o", "ttf",
        "--interpolate",
        "--keep-overlaps",
        "--no-autohint",
    ], check=True)

    os.makedirs(TARGET_DIR, exist_ok=True)
    source_dir = "instance_ttf"
    compiled   = []

    if os.path.exists(source_dir):
        for root, _dirs, files in os.walk(source_dir):
            for file in files:
                if file.endswith(".ttf"):
                    src_path  = os.path.join(root, file)
                    dest_path = os.path.join(TARGET_DIR, file)
                    shutil.move(src_path, dest_path)
                    compiled.append(dest_path)
                    print(f" -> Saved: {dest_path}")

        shutil.rmtree(source_dir)
        for cleanup in ("master_ttf", "instance_ufo"):
            if os.path.exists(cleanup):
                shutil.rmtree(cleanup)

    # ── Inject OT tables from nearest master ──────────────
    print("\n" + "=" * 60)
    print("      INJECTING OPENTYPE TABLES                        ")
    print("=" * 60)

    for path in sorted(compiled):
        style  = os.path.basename(path).replace("KhmerDigital-", "").replace(".ttf", "")
        weight = next(
            (i["weight"] for i in INSTANCES if i["name"].lower() == style.lower()),
            400
        )
        inject_ot_tables(path, weight)

    print("\n" + "=" * 60)
    print(f"DONE: {len(compiled)} weights saved to '{TARGET_DIR}/'")
    print("=" * 60)


if __name__ == "__main__":
    run()