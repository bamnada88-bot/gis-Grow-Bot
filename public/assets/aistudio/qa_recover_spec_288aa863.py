# -*- coding: utf-8 -*-
"""Recover the ORIGINAL canonical spec from the worker session transcript."""
import io, json, os, re

BASE = r"C:\Users\ALSAHABA\.minimax\v2\sessions\2026\10\28"
OUT = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package\qa_spec_original.md"

cands = []
for root, dirs, fs in os.walk(BASE):
    for f in fs:
        if f != "messages.jsonl":
            continue
        p = os.path.join(root, f)
        for raw in io.open(p, encoding="utf-8", errors="replace"):
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
                elif isinstance(cur, str) and "# Green Grow Bot — المواصفة المرجعية" in cur:
                    cands.append((p, cur))

print("candidates:", len(cands))
best = None
for p, c in cands:
    # the read tool output has "   1→" line prefixes
    if re.search(r"^\s*1→# Green Grow Bot", c, re.M):
        txt = re.sub(r"(?m)^\s*(\d+)→", "", c)
        if best is None or len(txt) > len(best[1]):
            best = (p, txt)

if best:
    io.open(OUT, "w", encoding="utf-8").write(best[1])
    print("recovered from:", best[0], "| chars:", len(best[1]))
else:
    print("NOT RECOVERED")
