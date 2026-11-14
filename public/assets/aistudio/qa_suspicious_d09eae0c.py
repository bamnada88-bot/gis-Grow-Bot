# -*- coding: utf-8 -*-
"""Dump full lines for a curated list of suspicious foreign tokens."""
import io, os, re

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
OUT = os.path.join(PKG, "qa_suspicious_lines.txt")

TOKENS = [
 "continuidad", "Initiative", "Subsidiary", "Monkeypatched", "improvisent", "selon",
 "descart", "reflectself", "perspectiva", "selfiereflection", "reclamaci",
 "independentemente", "olicited", "muitos", "who've", "pasefromGateway",
 "pollutantsowns", "kirkpatrickpartners", "tricotores", "sertifikat", "vinculados",
 "haqqiq", "ussi", "possibile", "Upsound", "osculate", "Mongo", "Streambadges",
 "promises", "sixty", "occurring", "heap", "adies", "paced", "lugar", "Gautierful",
 "provider", "plenary", "USBPresenter", "Mismatch", "ruined", "Beat", "sorry",
 "problem", "Pre-f", "visibilit", "abatic", "Gautier", "nasخ", "Assembler", "IDEREN",
 "mConfira", "Subsidia", "Etsy", "GGB", "nossier", "Nola", "GIGA", "Moments",
 "Require", "living", "ctorial", "Splendor", "COMPARE", "sustainability", "Charge",
 "Kata", "modules", "模块", "décart", "perishing", "Nolayer", "asures", "Incident",
 "Root", "cause", "consents", "Mimi", "ADU-", "errorMargins", "None", "symbolized",
 "complement", "pasefromGateway", "EXT-", "ossible", "Upsound", "map", "reach",
 "haqqiq", "EGC", "NOV-A", "GGB-", "rota", "visibilit", "tricotores", "ratic",
 "Concerned", "TRANSMISSION", "heap", "adies", "paced", "certain", "expanded",
 "therefore", "Ministry", "pushes", "Independent", "guarantee", "ourselves",
 "Several", "covered", "five-star", "INITIATIVE", "content", "lugar",
]

files = []
for root, dirs, fs in os.walk(PKG):
    dirs[:] = [d for d in dirs if d not in ("dist", "node_modules", ".git", "__pycache__")]
    for f in fs:
        if f.lower().endswith(".md"):
            files.append(os.path.join(root, f))

buf = []
seen = set()
for f in sorted(files):
    rel = os.path.relpath(f, PKG)
    for i, ln in enumerate(io.open(f, encoding="utf-8").read().split("\n"), 1):
        hits = [t for t in TOKENS if t in ln]
        if hits:
            buf.append("%s L%d  [%s]" % (rel, i, ",".join(hits)))
            buf.append("    " + ln.strip())
            buf.append("")

io.open(OUT, "w", encoding="utf-8").write("\n".join(buf))
print("written:", OUT, "| blocks:", len(buf) // 3)
