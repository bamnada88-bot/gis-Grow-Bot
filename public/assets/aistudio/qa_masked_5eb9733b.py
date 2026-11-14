# -*- coding: utf-8 -*-
"""Print every line containing Hangul/Greek/Cyrillic/etc. with foreign chars masked as [X]."""
import io, os, re

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
OUT = os.path.join(PKG, "qa_masked_lines.txt")

FOREIGN = re.compile("[^\u0600-\u06ff\u0020-\u007e\u00a0\u200e\u200f\u2010-\u203a"
                     "\u2040-\u206f\u20a0-\u20bf\u2100-\u2bff\u3000-\u303f"
                     "\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af"
                     "\uf900-\ufaff\uff00-\uffef]")

files = []
for root, dirs, fs in os.walk(PKG):
    dirs[:] = [d for d in dirs if d not in ("dist", "node_modules", ".git", "__pycache__")]
    for f in fs:
        if f.lower().endswith(".md"):
            files.append(os.path.join(root, f))

buf = []
for f in sorted(files):
    rel = os.path.relpath(f, PKG)
    for i, ln in enumerate(io.open(f, encoding="utf-8").read().split("\n"), 1):
        if FOREIGN.search(ln):
            masked = "".join("[X]" if FOREIGN.match(c) else c for c in ln)
            buf.append("%s L%d" % (rel, i))
            buf.append("    " + masked.strip()[:500])
            buf.append("")

io.open(OUT, "w", encoding="utf-8").write("\n".join(buf))
print("written:", OUT, "| lines:", len(buf) // 3)
