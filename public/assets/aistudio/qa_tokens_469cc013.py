# -*- coding: utf-8 -*-
"""Aggregate the distinct foreign tokens flagged in the artifact scan."""
import io, os, re, collections

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
OUT = os.path.join(PKG, "qa_tokens_report.txt")

CJK = re.compile("[\u3000-\u303f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef]")
LAT_IN_AR = re.compile("(?<=[\u0600-\u06ff])[A-Za-z][A-Za-z'\-]*(?![\u0600-\u06ff])")
LAT_WORD = re.compile(r"[A-Za-z][A-Za-z'\-]{1,}")
HAS_AR = re.compile("[\u0600-\u06ff]")
URL = re.compile(r"(https?://|www\.|@[A-Za-z0-9_]+|file:///)")

tokens = collections.Counter()
cjk_hits = []
latar_hits = []

files = []
for root, dirs, fs in os.walk(PKG):
    dirs[:] = [d for d in dirs if d not in ("dist", "node_modules", ".git", "__pycache__")]
    for f in fs:
        if f.lower().endswith(".md") and not f.startswith("qa_"):
            files.append(os.path.join(root, f))

for f in sorted(files):
    rel = os.path.relpath(f, PKG)
    for i, ln in enumerate(io.open(f, encoding="utf-8").read().split("\n"), 1):
        if CJK.search(ln):
            cjk_hits.append((rel, i, "".join(sorted(set(CJK.findall(ln)))), ln.strip()[:170]))
        for m in LAT_IN_AR.finditer(ln):
            tokens["LAT|AR:" + m.group(0)] += 1
            latar_hits.append((rel, i, m.group(0), ln.strip()[:170]))
        if HAS_AR.search(ln) and not URL.search(ln):
            for m in LAT_WORD.finditer(ln):
                w = m.group(0)
                if re.search("[\u0600-\u06ff]" + re.escape(w), ln) or re.search(re.escape(w) + r"[\u0600-\u06ff]", ln):
                    continue
                tokens["WORD:" + w] += 1

buf = []
buf.append("### CJK CHARACTER HITS (%d)" % len(cjk_hits))
for r, i, c, ln in cjk_hits:
    buf.append("  %s L%d  [%s]  %s" % (r, i, c, ln))
buf.append("")
buf.append("### LATIN GLUED TO ARABIC (%d)" % len(latar_hits))
for r, i, w, ln in latar_hits:
    buf.append("  %s L%d  <%s>  %s" % (r, i, w, ln))
buf.append("")
buf.append("### ALL LATIN TOKENS IN ARABIC LINES (count desc)")
for w, n in tokens.most_common():
    buf.append("  %-30s %d" % (w, n))
io.open(OUT, "w", encoding="utf-8").write("\n".join(buf))
print("written:", OUT, "| cjk:", len(cjk_hits), "| lat|ar:", len(latar_hits), "| tokens:", len(tokens))
