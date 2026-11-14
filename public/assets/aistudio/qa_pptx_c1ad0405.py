# -*- coding: utf-8 -*-
"""Validate the executive PPTX: foreign-script residue, geometry, fonts, RTL, overflow risk."""
import io, os, re, zipfile
from pptx import Presentation
from pptx.util import Emu

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
PPTX = os.path.join(PKG, "Green_Grow_Bot_Executive_Presentation.pptx")
OUT = os.path.join(PKG, "qa_pptx_report.txt")

FOREIGN = re.compile("[\u3000-\u303f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af"
                     r"\u0400-\u04ff\u0370-\u03ff]")          # CJK / Hangul / Cyrillic / Greek
ARABIC = re.compile("[\u0600-\u06ff]")
LATIN = re.compile("[A-Za-z]")

prs = Presentation(PPTX)
SW, SH = prs.slide_width, prs.slide_height
report = []
issues = 0

report.append("slides: %d | size: %.3f x %.3f in" % (len(prs.slides), SW / 914400, SH / 914400))

for idx, slide in enumerate(prs.slides, 1):
    report.append("\n=== SLIDE %d ===" % idx)
    for shp in slide.shapes:
        # geometry
        try:
            l, t, w, h = shp.left, shp.top, shp.width, shp.height
            if l is not None and (l < -Emu(914400) or t < 0 or l + w > SW + Emu(457200) or t + h > SH + Emu(457200)):
                report.append("  GEOM  %-18s L=%.2f T=%.2f R=%.2f B=%.2f in"
                              % (shp.shape_type, l / 914400, t / 914400,
                                 (l + w) / 914400, (t + h) / 914400))
                issues += 1
        except Exception:
            pass
        # table geometry: sum of grid columns must not exceed the frame
        if getattr(shp, "has_table", False) and shp.has_table:
            tot = sum(c.width for c in shp.table.columns)
            if tot > shp.width + Emu(9144):
                report.append("  TABLE width sum=%.2f in vs frame=%.2f in (right edge %.2f in)"
                              % (tot / 914400, shp.width / 914400, (shp.left + tot) / 914400))
                issues += 1
            if (shp.left + tot) / 914400 > 13.34:
                report.append("  TABLE overflows right edge at %.2f in" % ((shp.left + tot) / 914400))
                issues += 1
        if not shp.has_text_frame:
            continue
        txt = shp.text_frame.text
        if not txt.strip():
            continue
        for f in FOREIGN.finditer(txt):
            ctx = txt[max(0, f.start() - 30):f.start() + 30]
            report.append("  FOREIGN %r in: ...%s..." % (f.group(0), ctx))
            issues += 1
        # mixed-script words glued to Arabic
        for m in re.finditer(r"(?<=[\u0600-\u06ff])[A-Za-z]{2,}(?![\u0600-\u06ff])", txt):
            w = m.group(0)
            if w not in ("Green", "Grow", "Bot", "JW", "Marriott", "AXMIND", "KHZ", "LED", "LCD"):
                report.append("  MIXED  '%s' in: %s" % (w, txt[:90].replace("\n", " ")))
                issues += 1
        # fonts / rtl
        for p in shp.text_frame.paragraphs:
            pPr = p._p.find("{http://schemas.openxmlformats.org/drawingml/2006/main}pPr")
            has_rtl = pPr is not None and pPr.get("rtl") == "1"
            for r in p.runs:
                rPr = r._r.find("{http://schemas.openxmlformats.org/drawingml/2006/main}rPr")
                latin = None
                cs = None
                if rPr is not None:
                    el = rPr.find("{http://schemas.openxmlformats.org/drawingml/2006/main}latin")
                    latin = el.get("typeface") if el is not None else None
                    el = rPr.find("{http://schemas.openxmlformats.org/drawingml/2006/main}cs")
                    cs = el.get("typeface") if el is not None else None
                if cs != "Dubai" and latin != "Montserrat":
                    report.append("  FONT  latin=%s cs=%s :: %s" % (latin, cs, r.text[:50]))
                    issues += 1
                if not has_rtl and ARABIC.search(r.text):
                    report.append("  RTL   missing rtl on: %s" % r.text[:50])
                    issues += 1
            # overflow estimate: chars per line vs box width
            if p.runs:
                size = p.runs[0].font.size.pt if p.runs[0].font.size else 12
                chars = sum(len(r.text) for r in p.runs)
                box_w = (shp.width or 0) / 914400
                if box_w > 0.4 and size:
                    per_line = max(1, int(box_w * 96 / (size * 0.62)))
                    lines_needed = max(1, -(-chars // per_line))
                    box_h = (shp.height or 0) / 914400
                    lines_avail = max(1, int(box_h * 72 / (size * 1.25)))
                    if lines_needed > lines_avail + 1:
                        report.append("  OVERFLOW? %d chars @%.0fpt in %.2fx%.2f in (need %d lines, have %d) :: %s"
                                      % (chars, size, box_w, box_h, lines_needed, lines_avail,
                                         p.text[:70].replace("\n", " ")))
                        issues += 1

report.append("\nTOTAL ISSUES: %d" % issues)
io.open(OUT, "w", encoding="utf-8").write("\n".join(report))
print("issues:", issues, "->", OUT)
