# -*- coding: utf-8 -*-
"""Scan package Markdown for generation artifacts. Writes UTF-8 report (no console printing of Arabic)."""
import io, os, re

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
OUT = os.path.join(PKG, "qa_artifacts_report.txt")

CJK = re.compile("[\u3000-\u303f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef]")
LAT_IN_AR = re.compile("(?<=[\u0600-\u06ff])[A-Za-z][A-Za-z'\-]*(?![\u0600-\u06ff])")
AR_IN_LAT = re.compile("(?<![A-Za-z\u0600-\u06ff])[\u0600-\u06ff]{1,4}(?=[A-Za-z\u0600-\u06ff])")
# any latin word (2+ letters) in a line that also contains Arabic
LAT_WORD = re.compile(r"[A-Za-z][A-Za-z'\-]{1,}")
HAS_AR = re.compile("[\u0600-\u06ff]")
URL = re.compile(r"(https?://|www\.|@[A-Za-z0-9_]+|file:///)")

WHITELIST = set("""
GIS AXMIND JW Marriott Hotel Cairo Egypt Al Obour Green Grow Bot Press Kit
HTML PDF PPTX XLSX ISBN RFQ KPI EVT EXE COM EDU RSK PM PRO CT TEC DEMO CRM LOG SAFE FIN
STEM FLL ESP32 Arduino LEGO micro bit PictoBlox WhalesBot Kirkpatrick UL IEC ISO TIEC RC NIS
Amideast ESD Logo QR SMS LMS YouTube LinkedIn TikTok Instagram Facebook MOOC
mm cm kg USD EGP USD AR EN AI U S I O T M D C L R G B A E N P
e g i pi pico sdk lcd ttl usb led pcb
GreenGrowBot From learning to building one project that grows with student
Green International Schools AI Module WhalesBot
kg m2 cm2 Rubric report goal baseline setup sprint demo MVP
""".split())

def scan(path):
    lines = io.open(path, encoding="utf-8").read().split("\n")
    out = []
    in_code = False
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        issues = []
        if CJK.search(ln):
            issues.append("CJK[" + ",".join(sorted(set(CJK.findall(ln)))) + "]")
        for m in LAT_IN_AR.finditer(ln):
            w = m.group(0)
            if w in WHITELIST or len(w) <= 1:
                continue
            issues.append("LAT|AR:" + w)
        if HAS_AR.search(ln) and not URL.search(ln):
            for m in LAT_WORD.finditer(ln):
                w = m.group(0)
                if w in WHITELIST:
                    continue
                if re.search("[\u0600-\u06ff]" + re.escape(w), ln) or re.search(re.escape(w) + r"[\u0600-\u06ff]", ln):
                    continue  # already reported as LAT|AR
                issues.append("LATword:" + w)
        if issues:
            out.append((i, sorted(set(issues)), s[:190]))
    return out

files = []
for root, dirs, fs in os.walk(PKG):
    dirs[:] = [d for d in dirs if d not in ("dist", "node_modules", ".git", "__pycache__")]
    for f in fs:
        if f.lower().endswith(".md"):
            files.append(os.path.join(root, f))

buf = []
total = 0
for f in sorted(files):
    res = scan(f)
    if not res:
        continue
    buf.append("=" * 110)
    buf.append(os.path.relpath(f, PKG))
    for i, iss, ln in res:
        buf.append("  L%-6d %-30s %s" % (i, " , ".join(iss), ln))
        total += 1
buf.append("")
buf.append("TOTAL FLAGGED LINES: %d" % total)
io.open(OUT, "w", encoding="utf-8").write("\n".join(buf))
print("report written:", OUT, "| flagged:", total)
