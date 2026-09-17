#!/usr/bin/env python3
"""
Compile KhmerDigital.designspace → 9 TTF weights in ttf/
"""
import os
import shutil
import subprocess
import xml.etree.ElementTree as ET
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

MISMATCHED_GLYPHS = [
    "uni19E0", "uni19E1", "uni19E2", "uni19E3", "uni19E4", "uni19E5", "uni19E6", "uni19E7", "uni19E8", "uni19E9",
    "uni19EA", "uni19EB", "uni19EC", "uni19ED", "uni19EE", "uni19EF", "uni19F1", "uni19F2", "uni19F3", "uni19F4",
    "uni19F5", "uni19F6", "uni19F7", "uni19F9", "uni19FA", "uni19FB", "uni19FC", "uni19FD", "uni19FE", "uni19FF"
]


def sanitize_regular_contours():
    """Align Regular master contour order with Thin/Black masters."""
    glyphs_dir = os.path.join("master_ufo", "KhmerDigital-Regular.ufo", "glyphs")
    if not os.path.isdir(glyphs_dir):
        return

    fixed = 0
    for name in MISMATCHED_GLYPHS:
        glif_path = os.path.join(glyphs_dir, f"{name}.glif")
        if not os.path.exists(glif_path):
            continue

        tree = ET.parse(glif_path)
        root = tree.getroot()
        outline = root.find("outline")
        if outline is None:
            continue

        contours = list(outline.findall("contour"))
        if not contours:
            continue

        lens = [len(list(c.findall("point"))) for c in contours]
        min_idx = lens.index(min(lens))

        # Rotate contour sequence so the contour with smallest point count comes first
        if min_idx != 0:
            reordered = contours[min_idx:] + contours[:min_idx]
            for c in contours:
                outline.remove(c)
            for c in reordered:
                outline.append(c)
            tree.write(glif_path, encoding="utf-8", xml_declaration=True)
            fixed += 1

    if fixed > 0:
        print(f"Sanitized contour order for {fixed} glyphs in KhmerDigital-Regular.ufo")


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

    # ── Reorder contours in Regular master to avoid IndexError ──
    sanitize_regular_contours()

    print("=" * 60)
    print("      COMPILING 9 STANDALONE WEIGHTS FROM DESIGNSPACE  ")
    print("=" * 60)

    subprocess.run([
        "fontmake", "-m", DS_FILE, "-o", "ttf",
        "-i",
        "--keep-overlaps",
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