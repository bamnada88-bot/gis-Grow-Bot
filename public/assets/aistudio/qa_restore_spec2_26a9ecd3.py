# -*- coding: utf-8 -*-
"""Restore the damaged canonical-spec lines using two VERIFIED pure reads
(a) qa_spec_original.md  -> original lines 1..254
(b) the protocol worker's read at offset 253 -> original lines 253..447
Both are strict 'read' tool results of the spec file itself."""
import io, json, os, re

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
CUR = os.path.join(PKG, "Green_Grow_Bot_Canonical_Spec.md")
CLEAN = os.path.join(PKG, "qa_spec_original.md")
SESSION = (r"C:\Users\ALSAHABA\.minimax\v2\sessions\2026\10\28"
           r"\12-37-25-031-session_bXZzX2RmNWM4NTYxYzA3YjQwNTJhZjViMTVmY2UyYzIxN2Yz"
           r"\messages.jsonl")
NUMLINE = re.compile(r"(?m)^\s*(\d+)\u2192(.*)$")

# ---- source A: clean 254-line read (strip the tool's line-number gutter)
src_a = io.open(CLEAN, encoding="utf-8").read().split("\n")
src_a = [re.sub(r"^\s*\d+\u2192", "", x) for x in src_a]

# ---- source B: the offset-253 read, taken verbatim from the read tool result
src_b = {}
for raw in io.open(SESSION, encoding="utf-8", errors="replace"):
    if "Green_Grow_Bot_Canonical_Spec.md" not in raw:
        continue
    try:
        obj = json.loads(raw)
    except Exception:
        continue
    stack = [obj]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            stack.extend(cur.values())
        elif isinstance(cur, list):
            stack.extend(cur)
        elif isinstance(cur, str) and re.search(r"^\s*253\u2192\| 7 \|", cur, re.M):
            for m in NUMLINE.finditer(cur):
                src_b[int(m.group(1))] = m.group(2).rstrip("\n")

print("source A lines:", len(src_a), "| source B lines:", len(src_b))

orig = {}
for i, t in enumerate(src_a, 1):
    if t.strip():
        orig[i] = t
orig.update({k: v for k, v in src_b.items() if v.strip()})

cur = io.open(CUR, encoding="utf-8").read().split("\n")
OFFSET = 20
targets = [44, 88, 103, 104, 419]
for t in targets:
    j = t - OFFSET
    if j in orig:
        cur[t - 1] = orig[j]
        print("L%d restored from original L%d" % (t, j))
    else:
        print("L%d : NO SOURCE (j=%d)" % (t, j))

io.open(CUR, "w", encoding="utf-8").write("\n".join(cur))
