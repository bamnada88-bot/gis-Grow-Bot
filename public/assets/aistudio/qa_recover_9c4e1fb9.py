# -*- coding: utf-8 -*-
"""Recover the original (pre-cleanup) lines that contained Hangul/CJK noise
from the worker agent session transcripts."""
import io, json, os, re

BASE = r"C:\Users\ALSAHABA\.minimax\v2\sessions\2026\10\28"
OUT = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package\qa_recovered_lines.txt"

SESSIONS = [
    "12-36-04-205-session_bXZzX2QyNWIwNDk4MmQwYjRkYjFhMTExZjVmMDhlMmU3OTUw",
    "12-36-34-325-session_bXZzXzVjZWMzZDZiYTE3NjQ3YjVhZjQyOTYxZGM4Y2VhNTRm",
]
NOISE = re.compile("[\u3000-\u303f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff"
                    "\uff00-\uffef\u0400-\u04ff\uac00-\ud7af]")

seen = set()
out = []
for s in SESSIONS:
    p = os.path.join(BASE, s, "messages.jsonl")
    if not os.path.exists(p):
        continue
    for raw in io.open(p, encoding="utf-8", errors="replace"):
        if not NOISE.search(raw):
            continue
        # pull every JSON string value in the line
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
            elif isinstance(cur, str) and NOISE.search(cur):
                for ln in cur.split("\n"):
                    if NOISE.search(ln) and ln.strip() not in seen:
                        seen.add(ln.strip())
                        out.append(ln.rstrip())

io.open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("recovered lines:", len(out), "->", OUT)
