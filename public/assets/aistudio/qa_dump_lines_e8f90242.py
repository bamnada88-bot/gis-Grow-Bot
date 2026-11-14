# -*- coding: utf-8 -*-
"""Dump the FULL text of every flagged line (CJK / latin-glued-to-arabic) for exact fix mapping."""
import io, os, re

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
OUT = os.path.join(PKG, "qa_full_lines.txt")

CJK = re.compile("[\u3000-\u303f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef]")
LAT_IN_AR = re.compile("(?<=[\u0600-\u06ff])[A-Za-z][A-Za-z'\-]*(?![\u0600-\u06ff])")

files = []
for root, dirs, fs in os.walk(PKG):
    dirs[:] = [d for d in dirs if d not in ("dist", "node_modules", ".git", "__pycache__")]
    for f in fs:
        if f.lower().endswith(".md"):
            files.append(os.path.join(root, f))

buf = []
for f in sorted(files):
    rel = os.path.relpath(f, PKG)
    lines = io.open(f, encoding="utf-8").read().split("\n")
    picked = []
    for i, ln in enumerate(lines, 1):
        cjk = bool(CJK.search(ln))
        lat = [m.group(0) for m in LAT_IN_AR.finditer(ln)]
        if cjk or lat:
            picked.append((i, ln, cjk, lat))
    if not picked:
        continue
    buf.append("#" * 110)
    buf.append("### " + rel)
    for i, ln, cjk, lat in picked:
        buf.append("L%d%s%s" % (i, " [CJK]" if cjk else "", (" [LAT:" + ",".join(lat) + "]") if lat else ""))
        buf.append("    " + ln)
    buf.append("")

io.open(OUT, "w", encoding="utf-8").write("\n".join(buf))
print("written:", OUT)
