#!/usr/bin/env python3
"""Import Unicode glyphs absent from a UFO from an official Open Huninn TTF.

The importer is intentionally additive: it never overwrites a GLIF or a cmap
entry already present in the UFO. It preserves outlines and advances from the
reference TTF, but the imported glyphs are dehinted because UFO GLIF does not
store TrueType instructions.
"""

from __future__ import annotations

import argparse
import copy
import html
from pathlib import Path
from xml.etree import ElementTree as ET

from fontTools.ttLib import TTFont
from fontTools.ufoLib.glifLib import writeGlyphToString


def glyphs_in_ufo(glyph_dir: Path) -> tuple[set[str], set[int]]:
    names: set[str] = set()
    codepoints: set[int] = set()
    for path in glyph_dir.glob("*.glif"):
        root = ET.parse(path).getroot()
        names.add(root.attrib["name"])
        codepoints.update(int(node.attrib["hex"], 16) for node in root.findall("unicode"))
    return names, codepoints


def filename_for(glyph_name: str, used_filenames: set[str]) -> str:
    # UFO filenames are implementation details. Keep names readable and ensure
    # each new filename is unique without renaming existing project files.
    stem = "".join(char if char.isalnum() or char in "._-" else "_" for char in glyph_name)
    candidate = f"{stem}.glif"
    suffix = 1
    while candidate in used_filenames:
        candidate = f"{stem}.{suffix}.glif"
        suffix += 1
    used_filenames.add(candidate)
    return candidate


class Glyph:
    def __init__(self, glyph_set, glyph_name: str, width: int, codepoints: list[int]):
        self.width = width
        self.height = 0
        self.unicodes = codepoints
        self._glyph_set = glyph_set
        self._glyph_name = glyph_name

    def drawPoints(self, point_pen) -> None:
        self._glyph_set[self._glyph_name].drawPoints(point_pen)


def append_contents(contents_path: Path, records: list[tuple[str, str]]) -> None:
    text = contents_path.read_text(encoding="utf-8")
    marker = "  </dict>\n</plist>\n"
    if not text.endswith(marker):
        raise ValueError(f"Unexpected contents.plist ending: {contents_path}")
    entries = "".join(
        f"    <key>{html.escape(name)}</key>\n    <string>{html.escape(filename)}</string>\n"
        for name, filename in records
    )
    contents_path.write_text(text[: -len(marker)] + entries + marker, encoding="utf-8")


def write_glif(path: Path, glyph_set, source_name: str, target_name: str, width: int, codepoints: list[int], anchors=()) -> None:
    glif = Glyph(glyph_set, source_name, width, codepoints)
    root = ET.fromstring(writeGlyphToString(target_name, glif, drawPointsFunc=glif.drawPoints, formatVersion=2))
    insert_at = max((index for index, node in enumerate(root) if node.tag == "unicode"), default=0) + 1
    for anchor in anchors:
        root.insert(insert_at, copy.deepcopy(anchor))
        insert_at += 1
    ET.indent(root, space="  ")
    path.write_text("<?xml version='1.0' encoding='UTF-8'?>\n" + ET.tostring(root, encoding="unicode") + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ufo", type=Path, required=True, help="Target UFO directory")
    parser.add_argument("--upstream", type=Path, required=True, help="Official Open Huninn TTF")
    parser.add_argument("--include-unencoded", action="store_true", help="Also add missing, unencoded upstream feature/support glyphs")
    parser.add_argument("--sync-existing", action="store_true", help="Replace existing Unicode glyph outlines and advances with the upstream version")
    args = parser.parse_args()

    glyph_dir = args.ufo / "glyphs"
    contents_path = glyph_dir / "contents.plist"
    if not glyph_dir.is_dir() or not contents_path.is_file():
        raise ValueError(f"Not a package UFO glyph directory: {glyph_dir}")

    font = TTFont(args.upstream)
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    existing_names, existing_codepoints = glyphs_in_ufo(glyph_dir)
    glyph_paths = {ET.parse(path).getroot().attrib["name"]: path for path in glyph_dir.glob("*.glif")}
    codepoint_to_target = {}
    for target_name, path in glyph_paths.items():
        root = ET.parse(path).getroot()
        for node in root.findall("unicode"):
            codepoint_to_target[int(node.attrib["hex"], 16)] = target_name
    used_filenames = set(ET.parse(contents_path).getroot().itertext())

    missing: list[tuple[int | None, str]] = [(codepoint, glyph_name) for codepoint, glyph_name in sorted(cmap.items()) if codepoint not in existing_codepoints]
    if args.include_unencoded:
        encoded_names = set(cmap.values())
        missing.extend((None, name) for name in font.getGlyphOrder() if name not in encoded_names and name not in existing_names)
    if not missing and not args.sync_existing:
        print("No missing Unicode glyphs to import.")
        return

    conflicts = [name for _, name in missing if name in existing_names]
    if conflicts:
        raise ValueError(f"Refusing to overwrite existing glyph names: {', '.join(conflicts[:10])}")

    contents_records: list[tuple[str, str]] = []
    for codepoint, glyph_name in missing:
        filename = filename_for(glyph_name, used_filenames)
        width = font["hmtx"].metrics[glyph_name][0]
        write_glif(glyph_dir / filename, glyph_set, glyph_name, glyph_name, width, [] if codepoint is None else [codepoint])
        contents_records.append((glyph_name, filename))

    if contents_records:
        append_contents(contents_path, contents_records)
    synced = 0
    if args.sync_existing:
        grouped = {}
        for codepoint, source_name in cmap.items():
            target_name = codepoint_to_target.get(codepoint)
            if target_name is not None:
                grouped.setdefault(target_name, []).append((codepoint, source_name))
        for target_name, entries in grouped.items():
            source_names = {source_name for _, source_name in entries}
            if len(source_names) != 1:
                continue
            path = glyph_paths[target_name]
            old_root = ET.parse(path).getroot()
            anchors = old_root.findall("anchor")
            source_name = entries[0][1]
            codepoints = [codepoint for codepoint, _ in entries]
            write_glif(path, glyph_set, source_name, target_name, font["hmtx"].metrics[source_name][0], codepoints, anchors)
            synced += 1
    print(f"Imported {len(missing)} glyphs and synchronized {synced} existing Unicode glyphs from {args.upstream.name}.")


if __name__ == "__main__":
    main()
