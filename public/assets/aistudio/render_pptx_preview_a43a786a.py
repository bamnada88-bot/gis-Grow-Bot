# -*- coding: utf-8 -*-
"""Render the executive PPTX to PNG previews via an HTML mirror + Playwright.

python-pptx exposes enough geometry/formatting to rebuild each slide as absolutely
positioned HTML, which the browser renders with the same Dubai typeface — giving a
true visual check of the deck (no LibreOffice needed).
"""
import base64, io, os, re
from pptx import Presentation
from pptx.util import Emu

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
PPTX = os.path.join(PKG, "Green_Grow_Bot_Executive_Presentation.pptx")
PREV = os.path.join(PKG, "preview")
os.makedirs(PREV, exist_ok=True)
HTML_OUT = os.path.join(PREV, "deck_preview.html")

EMU_IN = 914400
PX_IN = 96.0


def px(v):
    return (v or 0) / EMU_IN * PX_IN


def solid_rgb(fill):
    try:
        if fill.type is not None and fill.type == 1:  # MSO_FILL.SOLID
            c = fill.fore_color
            if c.type == 1:  # RGB
                return "#%s" % str(c.rgb)
    except Exception:
        pass
    return None


NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def run_html(r):
    txt = (r.text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    txt = txt.replace("\n", "<br/>")
    size = r.font.size.pt if r.font.size else 12
    bold = "font-weight:700;" if r.font.bold else "font-weight:400;"
    color = "#16233F"
    try:
        if r.font.color and r.font.color.type == 1:
            color = "#%s" % str(r.font.color.rgb)
    except Exception:
        pass
    rPr = r._r.find(NS + "rPr")
    fam = "Dubai"
    if rPr is not None:
        el = rPr.find(NS + "latin")
        if el is not None and el.get("typeface"):
            fam = el.get("typeface")
    return ('<span style="font-family:%s;font-size:%.2fpt;%scolor:%s;">%s</span>'
            % (fam, size, bold, color, txt))


def shape_html(shp):
    l, t = px(shp.left), px(shp.top)
    w, h = px(shp.width), px(shp.height)
    style = "position:absolute;left:%.2fpx;top:%.2fpx;width:%.2fpx;height:%.2fpx;" % (l, t, w, h)
    # shape fill / line
    try:
        f = solid_rgb(shp.fill)
        if f:
            style += "background:%s;" % f
        ln = shp.line
        lc = solid_rgb(ln.fill) if ln.fill.type == 1 else None
        if lc:
            style += "border:1px solid %s;box-sizing:border-box;" % lc
    except Exception:
        pass
    # picture
    if shp.shape_type == 13:  # PICTURE
        try:
            blob = shp.image.blob
            b64 = base64.b64encode(blob).decode("ascii")
            return ('<img src="data:image/png;base64,%s" style="%sobject-fit:contain;">' % (b64, style))
        except Exception:
            return ""
    # table
    if getattr(shp, "has_table", False) and shp.has_table:
        tbl = shp.table
        out = ['<table style="%sborder-collapse:collapse;table-layout:fixed;max-width:100%%;">' % style]
        colw = [px(c.width) for c in tbl.columns]
        for ri, row in enumerate(tbl.rows):
            out.append("<tr>")
            for ci, cell in enumerate(row.cells):
                try:
                    bg = solid_rgb(cell.fill) or "#FFFFFF"
                except Exception:
                    bg = "#FFFFFF"
                out.append('<td style="width:%.1fpx;background:%s;border:1px solid #E3E8F2;'
                           'padding:4px 7px;vertical-align:middle;word-wrap:break-word;'
                           'overflow-wrap:anywhere;">' % (colw[ci], bg))
                for p in cell.text_frame.paragraphs:
                    algn = {1: "left", 2: "center", 3: "right", 4: "justify"}.get(int(p.alignment or 1), "right")
                    pPr = p._p.find(NS + "pPr")
                    is_rtl = True
                    if pPr is not None and pPr.get("rtl") is not None:
                        is_rtl = pPr.get("rtl") == "1"
                    out.append('<div style="text-align:%s;direction:%s;">' % (algn, "rtl" if is_rtl else "ltr"))
                    for r in p.runs:
                        out.append(run_html(r))
                    out.append("</div>")
                out.append("</td>")
            out.append("</tr>")
        out.append("</table>")
        return "".join(out)
    # text
    if not shp.has_text_frame:
        return '<div style="%s"></div>' % style
    tf = shp.text_frame
    if not tf.text.strip():
        return '<div style="%s"></div>' % style
    try:
        va = {1: "top", 2: "middle", 3: "bottom"}.get(int(tf.vertical_anchor or 1), "top")
    except Exception:
        va = "top"
    out = ['<div style="%sbox-sizing:border-box;padding:0 0 0 0;overflow:hidden;' % style]
    out.append('display:flex;flex-direction:column;justify-content:%s;">' % va)
    for p in tf.paragraphs:
        try:
            algn = {1: "left", 2: "center", 3: "right", 4: "justify"}.get(int(p.alignment or 1), "right")
        except Exception:
            algn = "right"
        pPr = p._p.find(NS + "pPr")
        is_rtl = True
        if pPr is not None and pPr.get("rtl") is not None:
            is_rtl = pPr.get("rtl") == "1"
        ls = p.line_spacing if isinstance(p.line_spacing, float) else 1.2
        sa = p.space_after.pt if p.space_after else 0
        out.append('<div style="text-align:%s;direction:%s;line-height:%.2f;margin-bottom:%.1fpt;">'
                   % (algn, "rtl" if is_rtl else "ltr", ls, sa))
        for r in p.runs:
            out.append(run_html(r))
        out.append("</div>")
    out.append("</div>")
    return "".join(out)


prs = Presentation(PPTX)
SW, SH = px(prs.slide_width), px(prs.slide_height)

pages = []
for i, slide in enumerate(prs.slides, 1):
    bg = "#FFFFFF"
    try:
        b = solid_rgb(slide.background.fill)
        if b:
            bg = b
    except Exception:
        pass
    body = []
    for shp in slide.shapes:
        body.append(shape_html(shp))
    pages.append(
        '<div class="slide" style="width:%.0fpx;height:%.0fpx;background:%s;position:relative;'
        'overflow:hidden;">%s</div>' % (SW, SH, bg, "".join(body)))

css = """
@font-face{font-family:Dubai;src:url('file:///C:/Windows/Fonts/DUBAI-REGULAR.TTF');font-weight:400}
@font-face{font-family:Dubai;src:url('file:///C:/Windows/Fonts/DUBAI-BOLD.TTF');font-weight:700}
@font-face{font-family:Dubai;src:url('file:///C:/Windows/Fonts/DUBAI-MEDIUM.TTF');font-weight:600}
@font-face{font-family:Dubai;src:url('file:///C:/Windows/Fonts/DUBAI-LIGHT.TTF');font-weight:300}
@font-face{font-family:Montserrat;src:local('Montserrat')}
body{margin:0;background:#5A6478;font-family:Dubai,sans-serif;}
.slide{margin:0 auto 18px;box-shadow:0 6px 26px rgba(0,0,0,.35);}
"""
html = ("<!doctype html><html dir='rtl'><head><meta charset='utf-8'><title>Green Grow Bot — "
        "Executive deck preview</title><style>%s</style></head><body>%s</body></html>"
        % (css, "".join(pages)))
io.open(HTML_OUT, "w", encoding="utf-8").write(html)
print("html written:", HTML_OUT, "| slides:", len(pages), "| %.0fx%.0f px" % (SW, SH))
