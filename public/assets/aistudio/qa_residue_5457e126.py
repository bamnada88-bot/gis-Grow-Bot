# -*- coding: utf-8 -*-
"""Final sweep: report every non-Arabic/non-Latin-script residue + known artifact tokens."""
import io, os, re

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
OUT = os.path.join(PKG, "qa_final_residue.txt")

BAD = re.compile("[\u0400-\u04ff\u0370-\u03ff\u0530-\u058f\u0590-\u05ff"
                 "\u0700-\u074f\u0750-\u077f\u0780-\u07bf\u0900-\u097f\u0e00-\u0e7f"
                 "\u3000-\u303f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af"
                 "\uf900-\ufaff\uff00-\uffef]")

KNOWN = ["\u7684\u5b58\u5728", "\uc758\uc874", "\uc785\ub825", "\ucd9c\ub825",
         "\u8f93\u51fa", "\u8f93\u5165", "Villain", "\u0437\u0430\u0432\u0435\u0442",
         "Management", "\u5b89\u5168", "\u7ba1\u7406", "\u603b", "\u6559\u80b2",
         "\ub300\u5b6c", "Blackboard", "bridge", "bridge", "Bridge"]

files = []
for root, dirs, fs in os.walk(PKG):
    dirs[:] = [d for d in dirs if d not in ("dist", "node_modules", ".git", "__pycache__")]
    for f in fs:
        if f.lower().endswith(".md") and not f.startswith("qa_"):
            files.append(os.path.join(root, f))

buf = []
for f in sorted(files):
    rel = os.path.relpath(f, PKG)
    for i, ln in enumerate(io.open(f, encoding="utf-8").read().split("\n"), 1):
        hits = []
        for ch in ln:
            if "\u0600" <= ch <= "\u06ff":
                continue
            if BAD.match(ch):
                hits.append("SCRIPT:" + ch)
        for k in KNOWN:
            if k in ln:
                hits.append("TOK:" + k)
        if hits:
            buf.append("%s L%d  [%s]" % (rel, i, ",".join(sorted(set(hits)))))
            buf.append("    " + ln.strip()[:420])
            buf.append("")

io.open(OUT, "w", encoding="utf-8").write("\n".join(buf))
print("written:", OUT, "| blocks:", len(buf) // 3)
