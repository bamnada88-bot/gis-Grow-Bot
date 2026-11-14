# -*- coding: utf-8 -*-
"""Merge every read of the canonical spec found in the session transcripts into one
reconstructed original file (line-numbered outputs are re-parsed)."""
import io, json, os, re

BASE = r"C:\Users\ALSAHABA\.minimax\v2\sessions\2026\10\28"
OUT = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package\qa_spec_original_full.md"

NUMLINE = re.compile(r"(?m)^\s*(\d+)\u2192(.*)$")

lines = {}
for root, dirs, fs in os.walk(BASE):
    for f in fs:
        if f != "messages.jsonl":
            continue
        for raw in io.open(os.path.join(root, f), encoding="utf-8", errors="replace"):
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
                elif isinstance(cur, str):
                    for m in NUMLINE.finditer(cur):
                        n = int(m.group(1))
                        txt = m.group(2).rstrip("\n")
                        if n not in lines or len(txt) > len(lines[n]):
                            lines[n] = txt

if lines:
    maxn = max(lines)
    out = []
    for i in range(1, maxn + 1):
        out.append(lines.get(i, ""))
    io.open(OUT, "w", encoding="utf-8").write("\n".join(out))
    print("recovered lines: %d (max line %d) -> %s" % (len(lines), maxn, OUT))
else:
    print("NOT RECOVERED")
