# -*- coding: utf-8 -*-
"""Green Grow Bot — Executive presentation builder (Arabic, RTL, 16:9).

Design system
-------------
navy  #0B1B3D   axmind navy #051629   royal #2D78FF
gold  #D4AF37   cream #FBF9F4          ink  #16233F
Arabic typeface: Dubai (installed system-wide). Latin runs fall back to Montserrat.
Every paragraph is marked RTL so PowerPoint lays the Arabic out correctly.
"""
import io, os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
OUT = os.path.join(PKG, "Green_Grow_Bot_Executive_Presentation.pptx")

NAVY = RGBColor(0x0B, 0x1B, 0x3D)
AXNAVY = RGBColor(0x05, 0x16, 0x29)
ROYAL = RGBColor(0x2D, 0x78, 0xFF)
GOLD = RGBColor(0xD4, 0xAF, 0x37)
CREAM = RGBColor(0xFB, 0xF9, 0xF4)
INK = RGBColor(0x16, 0x23, 0x3F)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
MUTED = RGBColor(0x8A, 0x9A, 0xB8)
SOFT = RGBColor(0xEC, 0xEF, 0xF6)
FAINT = RGBColor(0xE3, 0xE8, 0xF2)
GREEN = RGBColor(0x1F, 0x8A, 0x5B)
RED = RGBColor(0xB3, 0x2D, 0x2D)

AR = "Dubai"
LAT = "Montserrat"

W, H = Inches(13.333), Inches(7.5)
M = Inches(0.72)            # side margin
CW = W - 2 * M              # content width

prs = Presentation()
prs.slide_width, prs.slide_height = W, H
BLANK = prs.slide_layouts[6]


# ----------------------------------------------------------------- primitives
def slide(bg=CREAM):
    s = prs.slides.add_slide(BLANK)
    bgfill = s.background.fill
    bgfill.solid()
    bgfill.fore_color.rgb = bg
    return s


def rect(s, x, y, w, h, fill=None, line=None, lw=Pt(1), shape=MSO_SHAPE.RECTANGLE, adj=None):
    sh = s.shapes.add_shape(shape, int(x), int(y), int(w), int(h))
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line
        sh.line.width = lw
    sh.shadow.inherit = False
    if adj is not None:
        try:
            sh.adjustments[0] = adj
        except Exception:
            pass
    tf = sh.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.12)
    tf.margin_top = tf.margin_bottom = Inches(0.06)
    return sh


def _rtl(p):
    pPr = p._p.get_or_add_pPr()
    pPr.set("rtl", "1")
    pPr.set("algn", p._p.get_or_add_pPr().get("algn") or "r")


def style_run(r, size, color, bold=False, font=AR, italic=False):
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    rPr = r._r.get_or_add_rPr()
    for tag in ("a:latin", "a:cs", "a:ea"):
        el = rPr.find(qn(tag))
        if el is None:
            el = parse_xml('<a:%s xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"/>'
                           % tag.split(":")[1])
            rPr.append(el)
        el.set("typeface", font)


def text(s, x, y, w, h, lines, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.TOP,
         rtl=True, space_after=6, line_spacing=1.18):
    """lines: list of (text, size, color, bold) OR (text, size, color, bold, font)."""
    tb = s.shapes.add_textbox(int(x), int(y), int(w), int(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    for i, item in enumerate(lines):
        t, sz, col, bd = item[0], item[1], item[2], item[3]
        fnt = item[4] if len(item) > 4 else AR
        line_rtl = item[5] if len(item) > 5 else rtl
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        pPr = p._p.get_or_add_pPr()
        pPr.set("rtl", "1" if line_rtl else "0")
        p.space_after = Pt(space_after)
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = t
        style_run(r, sz, col, bd, fnt)
    return tb


def bullets(s, x, y, w, h, items, size=13.5, color=INK, gap=9, marker="—",
            marker_color=GOLD, bold_head=True, line_spacing=1.22):
    tb = s.shapes.add_textbox(int(x), int(y), int(w), int(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    for i, it in enumerate(items):
        head, body = (it if isinstance(it, tuple) else (None, it))
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        pPr = p._p.get_or_add_pPr()
        pPr.set("rtl", "1")
        p.alignment = PP_ALIGN.RIGHT
        p.space_after = Pt(gap)
        p.line_spacing = line_spacing
        rm = p.add_run()
        rm.text = marker + " "
        style_run(rm, size, marker_color, True)
        if head:
            rh = p.add_run()
            rh.text = head + ": "
            style_run(rh, size, color, bold_head)
        rb = p.add_run()
        rb.text = body
        style_run(rb, size, color, False)
    return tb


PAGE = {"n": 0}


def chrome(s, title, kicker=None, section=None, dark=False):
    """Standard content-slide furniture: title, rule, footer."""
    PAGE["n"] += 1
    tcol = WHITE if dark else INK
    mcol = MUTED if dark else RGBColor(0x6B, 0x7A, 0x96)
    if kicker:
        text(s, M, Inches(0.42), CW, Inches(0.3),
             [(kicker, 10.5, GOLD, True)], space_after=0)
    text(s, M, Inches(0.72), CW, Inches(0.62),
         [(title, 27, tcol, True)], space_after=0, line_spacing=1.0)
    rect(s, W - M - Inches(1.5), Inches(1.42), Inches(1.5), Inches(0.035), fill=GOLD)
    rect(s, M, Inches(1.42), CW - Inches(1.62), Inches(0.012),
         fill=FAINT if not dark else RGBColor(0x2A, 0x3A, 0x5C))
    # footer
    rect(s, 0, H - Inches(0.42), W, Inches(0.42),
         fill=NAVY if not dark else AXNAVY)
    text(s, M, H - Inches(0.335), Inches(5.4), Inches(0.26),
         [("Green Grow Bot · " + (section or "الإطلاق"), 9.5, RGBColor(0xB9, 0xC6, 0xDC), False)],
         align=PP_ALIGN.LEFT, space_after=0)
    text(s, W - M - Inches(1.2), H - Inches(0.335), Inches(1.2), Inches(0.26),
         [(str(PAGE["n"]), 9.5, GOLD, True)], align=PP_ALIGN.RIGHT, space_after=0)


def logo_plaque(s, x, y, h):
    """GIS logo on a white rounded plaque (the master PNG has a white ground)."""
    rect(s, x, y, h * 0.8, h, fill=WHITE, shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.10)
    s.shapes.add_picture(os.path.join(PKG, "assets", "logos", "gis_logo_master.png"),
                         int(x + Inches(0.05)), int(y + Inches(0.045)),
                         height=int(h - Inches(0.09)))


def card(s, x, y, w, h, head, body, head_color=NAVY, body_color=INK,
         accent=GOLD, head_size=14.5, body_size=11.5, fill=WHITE):
    sh = rect(s, x, y, w, h, fill=fill, line=FAINT, lw=Pt(0.75))
    rect(s, x + w - Inches(0.055), y, Inches(0.055), h, fill=accent)
    text(s, x + Inches(0.16), y + Inches(0.14), w - Inches(0.34), Inches(0.42),
         [(head, head_size, head_color, True)], space_after=0, line_spacing=1.05)
    text(s, x + Inches(0.16), y + Inches(0.58), w - Inches(0.34), h - Inches(0.7),
         [(body, body_size, body_color, False)], space_after=0, line_spacing=1.24)
    return sh


def table(s, x, y, w, data, col_w, header_h=Inches(0.42), row_h=Inches(0.34),
          head_size=11, body_size=10.5, head_fill=NAVY, head_color=WHITE,
          zebra=True, align_first_bold=True):
    rows, cols = len(data), len(data[0])
    h = header_h + row_h * (rows - 1)
    gf = s.shapes.add_table(rows, cols, int(x), int(y), int(w), int(h))
    tbl = gf.table
    # kill banding so our explicit fills win
    tblPr = tbl._tbl.find(qn("a:tblPr"))
    if tblPr is not None:
        tblPr.set("bandRow", "0")
        tblPr.set("firstRow", "1")
        tblPr.set("rtl", "1")
    total = sum(col_w)
    for i, cw in enumerate(col_w):
        tbl.columns[i].width = Emu(int(w * cw / total))
    tbl.rows[0].height = int(header_h)
    for r in range(1, rows):
        tbl.rows[r].height = int(row_h)
    for r in range(rows):
        for c in range(cols):
            cell = tbl.cell(r, c)
            cell.margin_left = cell.margin_right = Inches(0.08)
            cell.margin_top = cell.margin_bottom = Inches(0.03)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            if r == 0:
                cell.fill.fore_color.rgb = head_fill
            else:
                cell.fill.fore_color.rgb = (WHITE if (r % 2 == 1 or not zebra) else SOFT)
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            pPr = p._p.get_or_add_pPr()
            pPr.set("rtl", "1")
            p.alignment = PP_ALIGN.RIGHT
            p.line_spacing = 1.1
            run = p.add_run()
            run.text = str(data[r][c])
            style_run(run, head_size if r == 0 else body_size,
                      head_color if r == 0 else INK,
                      True if (r == 0 or (c == 0 and align_first_bold)) else False)
    return gf


def chip(s, x, y, w, h, label, fill=NAVY, color=WHITE, size=10.5, rtl=True):
    sh = rect(s, x, y, w, h, fill=fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.45)
    tf = sh.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    pPr = p._p.get_or_add_pPr()
    pPr.set("rtl", "1" if rtl else "0")
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = label
    style_run(r, size, color, True)
    return sh


def fade_picture(pic, pct):
    """Apply alpha transparency to a picture so it reads as a background watermark."""
    blip = pic._element.blipFill.find(qn("a:blip"))
    if blip is None:
        return pic
    for tag in ("a:alphaModFix",):
        el = blip.find(qn(tag))
        if el is None:
            el = parse_xml('<a:alphaModFix xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" amt="%d"/>'
                           % int(pct * 1000))
            blip.append(el)
        else:
            el.set("amt", str(int(pct * 1000)))
    return pic


# ============================================================== 1 — COVER
s = slide(NAVY)
rect(s, 0, 0, W, H, fill=NAVY)
# depth bands
rect(s, 0, H - Inches(1.9), W, Inches(1.9), fill=AXNAVY)
rect(s, W - M - Inches(1.9), Inches(1.05), Inches(1.9), Inches(0.035), fill=GOLD)
# robot, bottom-left, faded to a watermark
fade_picture(s.shapes.add_picture(os.path.join(PKG, "assets", "robot.png"),
                                  int(-Inches(0.7)), int(H - Inches(4.6)),
                                  height=Inches(4.6)), 26)
# logo plaque top-right
logo_plaque(s, W - M - Inches(1.18), Inches(0.45), Inches(1.35))
text(s, W - M - Inches(4.6), Inches(0.62), Inches(3.2), Inches(0.9),
     [("PRESS KIT", 13, GOLD, True, LAT),
      ("حقيبة الصحفيين", 12.5, RGBColor(0xC7, 0xD3, 0xE8), False)],
     align=PP_ALIGN.RIGHT, space_after=2)
text(s, M, Inches(1.25), Inches(9.4), Inches(1.9),
     [("مبادرة تعليمية تطبيقية", 15, GOLD, True),
      ("من التعليم إلى الابتكار", 43, WHITE, True),
      ("مشروع واحد يتطور مع الطالب", 27, RGBColor(0x9F, 0xB4, 0xD6), False)],
     space_after=7, line_spacing=1.05)
rect(s, W - M - Inches(3.2), Inches(3.92), Inches(3.2), Inches(0.03), fill=GOLD)
text(s, M, Inches(4.18), Inches(9.0), Inches(1.1),
     [("عرض تنفيذي للإطلاق", 12.5, RGBColor(0xB9, 0xC6, 0xDC), False),
      ("Green International Schools · Al Obour, Egypt", 12.5, RGBColor(0xB9, 0xC6, 0xDC), False, LAT, False),
      ("الأحد 15 نوفمبر 2026  ·  فندق JW Marriott Hotel Cairo", 12.5, GOLD, True)],
     space_after=5)
chip(s, M, Inches(5.32), Inches(1.72), Inches(0.34), "#GreenGrowBot", fill=AXNAVY,
     color=GOLD, size=11, rtl=False)
rect(s, M, Inches(5.95), Inches(9.6), Inches(0.012), fill=RGBColor(0x2A, 0x3A, 0x5C))
text(s, M, Inches(6.1), Inches(9.6), Inches(0.7),
     [("إعداد: الأستاذ أحمد جبر  ·  «الصفقة الرسمية» المعلَّقة: الفندق، الحضور، الموافقات  "
       "·  النسخة: 10 نوفمبر 2026", 10.5, MUTED, False)],
     space_after=0)

# ============================================================== 2 — CONTENTS
s = slide(CREAM)
chrome(s, "ماذا سنغطي في 15 دقيقة", kicker="جدول المحتويات", section="المحتويات")
items = [
    ("01", "الملخص التنفيذي", "المشكلة، الفكرة، والقرار المطلوب"),
    ("02", "لماذا الآن؟", "نافذة التنفيذ + حالة الجدول الزمني اليوم"),
    ("03", "النموذج التعليمي", "9 مراحل من KG1 إلى G12 — مشروع واحد متصل"),
    ("04", "شكل الحفل والجمهور", "البرنامج، القاعة، والفئات المستهدفة"),
    ("05", "الميزانية والقياس", "3 سيناريوهات + سقف الاعتماد + مؤشرات الأداء"),
    ("06", "المخاطر والقرارات", "ما يمكن أن يفشل، ومن يقرر، ومتى"),
]
x0, y0 = M, Inches(1.85)
cw, ch = (CW - Inches(0.34)) / 2, Inches(1.45)
for i, (n, t, d) in enumerate(items):
    col, row = i % 2, i // 2
    x = W - M - cw - col * (cw + Inches(0.34))
    y = y0 + row * (ch + Inches(0.22))
    rect(s, x, y, cw, ch, fill=WHITE, line=FAINT, lw=Pt(0.75))
    rect(s, x + cw - Inches(0.05), y, Inches(0.05), ch, fill=GOLD if i % 2 == 0 else ROYAL)
    text(s, x + Inches(0.18), y + Inches(0.18), Inches(0.7), Inches(0.5),
         [(n, 24, RGBColor(0xD8, 0xDF, 0xEC), True, LAT)], align=PP_ALIGN.LEFT, space_after=0)
    text(s, x + Inches(0.18), y + Inches(0.3), cw - Inches(0.42), Inches(0.4),
         [(t, 15, NAVY, True)], space_after=0)
    text(s, x + Inches(0.18), y + Inches(0.78), cw - Inches(0.42), Inches(0.55),
         [(d, 11.5, RGBColor(0x5A, 0x69, 0x86), False)], space_after=0, line_spacing=1.2)

# ============================================================== 3 — EXEC SUMMARY
s = slide(CREAM)
chrome(s, "الملخص التنفيذي", kicker="الخلاصة في ثلاث نقاط", section="الملخص التنفيذي")
cw3 = (CW - Inches(0.44)) / 3
heads = [
    ("المشكلة", "الطالب يكتسب المعرفة في الفصل ثم يجد مكانًا آخر ليجرّبها. "
                "المشاريع القائمة مُشتَّتة، وقياس أثرها ضعيف، وتكلفتها تتكرر.",
     NAVY),
    ("الفكرة", "روبوت واحد — أو منظومة واحدة — ينمو مع الطالب من الروضة حتى الصف الثاني عشر، "
               "مبنيًا فوق المنهج لا بديلًا منه، وبمعيار قبول موثّق في كل مرحلة.",
     ROYAL),
    ("الطلب", "إقرار ميزانية بسقف **191,418 ج.م** (سيناريو A)، وتثبيت القاعة، "
              "وإغلاق 7 قرارات خلال 24 ساعة.", GOLD),
]
for i, (h, b, acc) in enumerate(heads):
    x = W - M - cw3 - i * (cw3 + Inches(0.22))
    card(s, x, Inches(1.78), cw3, Inches(2.55), h, b, accent=acc,
         head_size=17, body_size=12)
rect(s, M, Inches(4.62), CW, Inches(1.52), fill=NAVY)
text(s, M + Inches(0.26), Inches(4.78), CW - Inches(0.52), Inches(0.32),
     [("القرار المطلوب اليوم", 13, GOLD, True)], space_after=0)
text(s, M + Inches(0.26), Inches(5.12), CW - Inches(0.52), Inches(0.95),
     [("الموافقة على سيناريو A بوصفه أرضية تصميم — 90 دعوة، قاعة Cheops + Pre-function، "
       "وإنتاج أساسي — مع تحويل أي بند لم يُسعَّر كتابيًا إلى «معلَّق» لا إلى «معتمد». "
       "سقف الإنفاق لا يُتجاوز إلا بقرار موثّق من PM + FIN.", 12.5, RGBColor(0xD5, 0xDF, 0xF0), False)],
     space_after=0, line_spacing=1.26)

# ============================================================== 4 — WHY NOW
s = slide(CREAM)
chrome(s, "لماذا الآن؟", kicker="نافذة التنفيذ", section="لماذا الآن")
reasons = [
    ("فجوة موثّقة", "أغلب التقييمات التعليمية تتوقف عند المستويين الأول والثاني من نموذج كيركباتريك. "
                    "المبادرة تُنتج أثرًا يُقاس على أربعة مستويات."),
    ("تدرّج قابل للتنفيذ", "سُلّم منصات مُوثَّق في مدارس دولية بالمنطقة، ومسار KG→G12 قابل للتسليم "
                           "دون اختراع من الصفر."),
    ("أسعار قابلة للدقة", "أسعار المكونات المصرية ومنتجات LEGO و WhalesBot تم التحقق منها في "
                          "28 أكتوبر 2026 — ما ينقص هو قرار الشراء، لا المعرفة."),
]
cw4 = (CW - Inches(0.44)) / 3
for i, (h, b) in enumerate(reasons):
    x = W - M - cw4 - i * (cw4 + Inches(0.22))
    card(s, x, Inches(1.78), cw4, Inches(2.1), h, b, accent=ROYAL, head_size=15, body_size=11.5)
# status strip
rect(s, M, Inches(4.18), CW, Inches(1.85), fill=RGBColor(0xFD, 0xF6, 0xE6), line=GOLD, lw=Pt(1))
rect(s, W - M - Inches(0.06), Inches(4.18), Inches(0.06), Inches(1.85), fill=RED)
text(s, M + Inches(0.28), Inches(4.34), CW - Inches(0.62), Inches(0.36),
     [("حالة الجدول الزمني — يُقرأ أولًا", 14, RED, True)], space_after=0)
text(s, M + Inches(0.28), Inches(4.72), CW - Inches(0.62), Inches(0.72),
     [("الحزمة بُنيت على خط أساس 27 أكتوبر 2026 (19 يومًا). اليوم 10 نوفمبر 2026 — "
       "والمتبقي 5 أيام فقط. جميع مواعيد 1–3 نوفمبر مُنتهية زمنيًا ولم يُقيَّد تنفيذها؛ "
       "المحتوى صالح، والجدول يحتاج إعادة ضبط خلال 24 ساعة.", 12.5, INK, False)],
     space_after=0, line_spacing=1.26)
gates = [("حجز القاعة", "[يحتاج تأكيد]"), ("RFQ الأسعار", "لم يُطلب"),
         ("دعوات الضيوف", "لم تُرسل"), ("موافقات التصوير", "لم تُجمع")]
gw = (CW - Inches(0.66)) / 4
for i, (k, v) in enumerate(gates):
    x = W - M - Inches(0.28) - gw - i * gw
    text(s, x, Inches(5.48), gw - Inches(0.08), Inches(0.26),
         [(k, 10.5, RGBColor(0x6B, 0x7A, 0x96), False)], space_after=0)
    text(s, x, Inches(5.72), gw - Inches(0.08), Inches(0.26),
         [(v, 11.5, RED, True)], space_after=0)

# ============================================================== 5 — CORE IDEA
s = slide(NAVY)
chrome(s, "الفكرة المحورية: مشروع واحد يتطور مع الطالب", kicker="ما الذي يميّزنا",
       section="النموذج التعليمي", dark=True)
text(s, M, Inches(1.72), CW, Inches(0.4),
     [("ليس مشروعًا في مادة. إنه مشروع في حياة الطالب — يبدأ في الروضة وينتهي موثَّقًا في ملف الإنجاز.",
       14, RGBColor(0xC7, 0xD3, 0xE8), False)], space_after=0)
# 9-stage ladder
stages = [("KG1–2", "عربة بعجلة"), ("G3", "دارة + LED"), ("G4–5", "خوارزمية"),
          ("G6", "حساسات"), ("G7–8", "تحكّم مغلق"), ("G9–10", "تصميم هندسي"),
          ("G11", "اتصال وإنترنت"), ("G12", "نظام متكامل"), ("G12", "مشروع تخرج")]
bw = (CW - Inches(0.16) * 8) / 9
LADDER_BOTTOM = Inches(5.02)
for i, (g, t) in enumerate(stages):
    x = W - M - bw - i * (bw + Inches(0.16))
    h = Inches(1.52) + Inches(0.104) * i
    y = LADDER_BOTTOM - h
    rect(s, x, y, bw, h, fill=RGBColor(0x16, 0x29, 0x4F),
         line=RGBColor(0x2B, 0x40, 0x6C), lw=Pt(0.75))
    rect(s, x, y, bw, Inches(0.05), fill=GOLD if i == 8 else ROYAL)
    text(s, x, y + Inches(0.14), bw, Inches(0.26),
         [(g, 11.5, GOLD if i == 8 else RGBColor(0x9F, 0xB4, 0xD6), True, LAT)],
         align=PP_ALIGN.CENTER, space_after=0)
    text(s, x + Inches(0.05), y + Inches(0.44), bw - Inches(0.1), h - Inches(0.52),
         [(t, 9.5, WHITE, False)], align=PP_ALIGN.CENTER, space_after=0, line_spacing=1.12)
rect(s, M, LADDER_BOTTOM + Inches(0.04), CW, Inches(0.02), fill=RGBColor(0x27, 0x3C, 0x66))
text(s, M, Inches(5.18), CW, Inches(0.3),
     [("↑  كل مرحلة تضيف مفهومًا واحدًا — ولا يُعاد تدريس ما سبق، بل يُستخدم كمادة خام",
       11.5, GOLD, True)], align=PP_ALIGN.CENTER, space_after=0)
pts = [("المنهج لا يُلغى", "المبادرة طبقة تطبيق فوقه — لا بديل ولا تقصير لأي هدف."),
       ("الأثر موثّق", "ملف إنجاز تراكمي + Rubric موحّد رباعي الأبعاد في كل مرحلة."),
       ("قابلية التكرار", "نفس المعلم يوثّق الخطأ ويعدّل التصميم — يستطيع أي معلم آخر تكراره.")]
pw = (CW - Inches(0.36)) / 3
for i, (h, b) in enumerate(pts):
    x = W - M - pw - i * (pw + Inches(0.18))
    rect(s, x, Inches(5.62), pw, Inches(0.95), fill=AXNAVY, line=RGBColor(0x27, 0x3C, 0x66), lw=Pt(0.75))
    text(s, x + Inches(0.14), Inches(5.74), pw - Inches(0.28), Inches(0.26),
         [(h, 12, GOLD, True)], space_after=0)
    text(s, x + Inches(0.14), Inches(6.02), pw - Inches(0.28), Inches(0.5),
         [(b, 10, RGBColor(0xB9, 0xC6, 0xDC), False)], space_after=0, line_spacing=1.16)

# ============================================================== 6 — 9 STAGES TABLE
s = slide(CREAM)
chrome(s, "النموذج: 9 مراحل من KG1 إلى G12", kicker="خريطة المراحل", section="النموذج التعليمي")
rows = [
    ["المرحلة", "الفئة", "المحور المعرفي", "الأداة/المنصة"],
    ["1 · KG1–KG2", "4–6", "السبب والنتيجة، المحاور، التصنيف", "WhalesBot U20 Pro / كتل بناء"],
    ["2 · G1–G2", "6–8", "المدخلات والمخرجات، الحركة، القياس", "LEGO WeDo 2.0"],
    ["3 · G3", "8–9", "الدارة الكهربائية والقطبية", "micro:bit / micro:bit V2"],
    ["4 · G4–G5", "9–11", "الخوارزمية والتكرار والشرط", "LEGO Spike Prime / PictoBlox"],
    ["5 · G6", "11–12", "الحساسات و ADC والمعايرة", "Arduino Uno · LM35 · MPU-6050"],
    ["6 · G7–G8", "12–14", "التحكّم المغلق والتغذية الراجعة", "Arduino + L298N / ESP32"],
    ["7 · G9–G10", "14–16", "التصميم الهندسي والتكلفة والمخاطر", "Tinkercad / Wokwi + CAD"],
    ["8 · G11", "16–17", "الأنظمة المتكاملة وإنترنت الأشياء", "ESP32 + MQTT + لوحة ويب"],
    ["9 · G12", "17–18", "مشروع التخرج + التقييم المزدوج", "تجميع كل الأدوات + معرض"],
]
table(s, M, Inches(1.72), CW, rows, [1.5, 0.8, 3.1, 2.9],
      header_h=Inches(0.4), row_h=Inches(0.335), head_size=11.5, body_size=10.5)
text(s, M, Inches(5.35), CW, Inches(0.6),
     [("قاعدة الثبات: المنهج الأكاديمي هو الأساس، والمبادرة طبقة فوقه. "
       "لا تُحذف حصة، ولا يُختصر هدف، ولا يُعطَّل مفهوم من منهجي في مقابل نشاط تقني.",
       11.5, INK, False)], space_after=0, line_spacing=1.22)
rect(s, M, Inches(6.05), CW, Inches(0.72), fill=WHITE, line=FAINT, lw=Pt(0.75))
text(s, M + Inches(0.2), Inches(6.16), CW - Inches(0.4), Inches(0.5),
     [("الأرقام من المواصفة المرجعية §4؛ أسعار المكوّنات موثّقة في 28 أكتوبر 2026. "
       "تكلفة الطيار (G6) هي الأدنى ويمكن أن تُقاس في 6 أسابيع — نبدأ بها.",
       11, RGBColor(0x5A, 0x69, 0x86), False)], space_after=0, line_spacing=1.2)

# ============================================================== 7 — WHAT WE DON'T PROMISE
s = slide(CREAM)
chrome(s, "ما لا نَعِد به", kicker="الحدود الصريحة", section="النموذج التعليمي")
text(s, M, Inches(1.7), CW, Inches(0.34),
     [("هذه الشريحة هي عقدنا مع الحضور والإعلام — تُوزَّع كما هي في حقيبة الصحفيين.",
       12, RGBColor(0x5A, 0x69, 0x86), False)], space_after=0)
nos = [
    ("وظائف", "لن نَعِد بوظيفة، ولن نَعِد بقبول جامعي. ما نلتزم به: مسار موثّق ومقاس لكل طالب."),
    ("اعتماد", "إتمام تدريب المعلمين داخل المبادرة لا يعني اعتمادًا حكوميًا ولا اعتمادًا من أي جهة خارجية."),
    ("شراكة أو رعاية", "أي شراكة أو رعاية أو شعار جهة يُذكر فقط بعد موافقة مكتوبة — وإلا فلا يُذكر."),
    ("أثر على قيمة المدرسة", "لا يُنسب أي تحسّن في قيمة المدرسة إلى الحفل. ما يُقاس هو مسار التحويل فقط."),
]
nw = (CW - Inches(0.36)) / 4
for i, (h, b) in enumerate(nos):
    x = W - M - nw - i * (nw + Inches(0.12))
    rect(s, x, Inches(2.22), nw, Inches(2.25), fill=WHITE, line=FAINT, lw=Pt(0.75))
    rect(s, x, Inches(2.22), nw, Inches(0.05), fill=RED)
    text(s, x + Inches(0.16), Inches(2.42), nw - Inches(0.32), Inches(0.3),
         [("لا " + h, 14, RED, True)], space_after=0)
    text(s, x + Inches(0.16), Inches(2.82), nw - Inches(0.32), Inches(1.5),
         [(b, 11, INK, False)], space_after=0, line_spacing=1.24)
rect(s, M, Inches(4.78), CW, Inches(1.35), fill=NAVY)
text(s, M + Inches(0.26), Inches(4.94), CW - Inches(0.52), Inches(0.3),
     [("ما نَعِد به", 13, GOLD, True)], space_after=0)
bullets(s, M + Inches(0.26), Inches(5.26), CW - Inches(0.52), Inches(0.8),
        ["نموذج أولي حيّ يعمل أمام الحضور، وشهادات موثّقة على مسار الطالب عبر 9 مراحل.",
         "خطة قياس معلنة: EVT / COM / EDU / EXE — وهدف ومصدر لكل مؤشر.",
         "حزمة صداقية كاملة: دليل التكرار، نموذج الميزانية، وسجل المخاطر."],
        size=11.5, color=RGBColor(0xD5, 0xDF, 0xF0), gap=5)

# ============================================================== 8 — EVENT FORMAT
s = slide(CREAM)
chrome(s, "شكل الحفل: مؤتمر مصغّر + عرض حيّ + استقبال", kicker="البرنامج", section="الحفل")
text(s, M, Inches(1.66), CW, Inches(0.34),
     [("مسائي · 85 دقيقة للجلسة العامة · قاعة Cheops (352 م²) + Pre-function للتسجيل والاستقبال · "
       "حالة الحجز: [يحتاج تأكيد]", 11.5, RGBColor(0x5A, 0x69, 0x86), False)], space_after=0)
prog = [
    ("18:00", "تسجيل الضيوف", "توزيع الكروت وجمع الموافقات", SOFT),
    ("18:30", "ترحيب وكلمة افتتاح (9 د)", "تهيئة الحضور + تمثيل المدرسة", NAVY),
    ("18:39", "كلمة المؤسس (8 د)", "المشكلة والفكرة — بلا مبالغة", NAVY),
    ("18:47", "عرض المسار (12 د)", "خريطة KG→Grade 12 + تمهيد العرض", NAVY),
    ("19:00", "العرض الحي (12 د)", "النموذج يعمل أمام الحضور", ROYAL),
    ("19:12", "مداخلة الخبير (8 د)", "مصداقية أكاديمية — موثّقة", NAVY),
    ("19:20", "حوار مفتوح (24 د)", "أسئلة الحضور + مواقف مسجّلة", NAVY),
    ("19:44", "الخطوات القادمة (6 د)", "ما نطلبه اليوم بالاسم", GOLD),
    ("19:50", "شكر وختام (5 د)", "التسليم + شكر الحضور", SOFT),
    ("19:55", "إعلام وتواصل (20 د)", "تصوير ومقابلات مسجّلة", SOFT),
]
# timeline rail
rect(s, M, Inches(2.22), CW, Inches(0.02), fill=FAINT)
bw2 = (CW - Inches(0.1) * 4) / 5
for i, (t, h, d, col) in enumerate(prog):
    col_i, row_i = i % 5, i // 5
    x = W - M - bw2 - col_i * (bw2 + Inches(0.1))
    y = Inches(2.42) + row_i * Inches(1.95)
    rect(s, x, y, bw2, Inches(1.72), fill=WHITE, line=FAINT, lw=Pt(0.75))
    rect(s, x, y, bw2, Inches(0.05), fill=col)
    text(s, x + Inches(0.12), y + Inches(0.16), bw2 - Inches(0.24), Inches(0.28),
         [(t, 14, NAVY, True, LAT)], space_after=0)
    text(s, x + Inches(0.12), y + Inches(0.48), bw2 - Inches(0.24), Inches(0.44),
         [(h, 11.5, INK, True)], space_after=0, line_spacing=1.1)
    text(s, x + Inches(0.12), y + Inches(0.98), bw2 - Inches(0.24), Inches(0.62),
         [(d, 10, RGBColor(0x5A, 0x69, 0x86), False)], space_after=0, line_spacing=1.18)
rect(s, M, Inches(6.28), CW, Inches(0.62), fill=NAVY)
text(s, M + Inches(0.2), Inches(6.38), CW - Inches(0.4), Inches(0.24),
     [("20:15 — استقبال ختامي 45 دقيقة: ضيافة + 6 محادثات ثنائية مسجّلة", 11.5, GOLD, True)],
     space_after=0)
text(s, M + Inches(0.2), Inches(6.64), CW - Inches(0.4), Inches(0.22),
     [("قاعدة التشغيل: ما هو موقّع فقط يُنطق. أي اسم أو صفة غير مؤكدة تُقرأ بصيغة عامة أو تُحذف.",
       10.5, RED, True)], space_after=0)

# ============================================================== 9 — AUDIENCE
s = slide(CREAM)
chrome(s, "الجمهور والفئات المستهدفة", kicker="من نُدعي؟", section="الحفل")
aud = [
    ["الفئة", "الهدف من الدعوة", "الأولوية", "المالك"],
    ["قيادات وزارة التربية والتعليم والجهات التعليمية", "اعتراف واحتواء", "A", "PRO"],
    ["جهات تطوير المهارات (TIEC، وزارة الشباب، المحافظات)", "شراكة تشغيلية: مسابقات ومدرّبون", "A", "PRO"],
    ["أعضاء مجلس النواب والشيوخ", "محتوى المصداقية", "B", "PRO"],
    ["قيادات الجامعات وخبراء التعليم", "منهج قابل للتكرار والتوسع", "A", "CT"],
    ["القطاع الخاص وتقنية/روبوتكس", "شريك تطبيقي بمخرجات واضحة", "A", "CT"],
    ["أصحاب المؤسسات التعليمية والمستثمرون", "نموذج قابل للنسخ", "B", "CT"],
    ["الإعلام والصحفيون", "قصة تعليمية موثّقة", "A", "PR"],
    ["أولياء أمور مختارون", "ابنهم يبني مشروعًا شخصيًا", "C", "CRM"],
]
table(s, M, Inches(1.7), Inches(8.1), aud, [3.5, 2.6, 0.7, 0.7],
      header_h=Inches(0.38), row_h=Inches(0.335), head_size=11, body_size=10)
# funnel
fx = M + Inches(8.35)
fw = CW - Inches(8.35)
rect(s, fx, Inches(1.7), fw, Inches(3.55), fill=NAVY)
text(s, fx + Inches(0.2), Inches(1.86), fw - Inches(0.4), Inches(0.3),
     [("قمع التحويل — القياس الوحيد المنسوب للحفل", 11.5, GOLD, True)], space_after=0)
fun = [("استفسار", "COM-01", 1.0), ("زيارة مدرسية", "COM-02", 0.82),
       ("طلب تقديم", "COM-03", 0.64), ("تسجيل منسوب", "COM-04", 0.46)]
for i, (lab, kid, frac) in enumerate(fun):
    w = (fw - Inches(0.4)) * frac
    y = Inches(2.3) + i * Inches(0.62)
    rect(s, fx + (fw - Inches(0.2) - w), y, w, Inches(0.46),
         fill=ROYAL if i < 3 else GOLD)
    text(s, fx + Inches(0.2), y + Inches(0.08), fw - Inches(0.4), Inches(0.3),
         [(lab + "  ·  " + kid, 10.5, WHITE if i < 3 else NAVY, True)],
         align=PP_ALIGN.CENTER, space_after=0)
text(s, fx + Inches(0.2), Inches(4.92), fw - Inches(0.4), Inches(0.28),
     [("لا تُنسب أي تحسّن في قيمة المدرسة إلى الحفل.", 9.5,
       RGBColor(0xB9, 0xC6, 0xDC), False)], space_after=0)
rect(s, M, Inches(5.5), CW, Inches(1.25), fill=WHITE, line=FAINT, lw=Pt(0.75))
text(s, M + Inches(0.22), Inches(5.64), CW - Inches(0.44), Inches(0.3),
     [("الدعوات: 90 في سيناريو A (70–90 حضور) — والحد الأقصى 130 في سيناريو C (160–200 حضور). "
       "التصميم يتم على أرضية 90 دعوة حتى صدور عروض الأسعار.", 11.5, INK, False)],
     space_after=0, line_spacing=1.24)
text(s, M + Inches(0.22), Inches(6.14), CW - Inches(0.44), Inches(0.42),
     [("قاعدة الدعوة: الاسم غير المُتحقق لا يُذكر في الدعوة المطبوعة ولا في سجل الدعوات ولا على "
       "الميكروفون — يُوضع في خانة [ ] فقط.", 11, RED, False)], space_after=0, line_spacing=1.2)

# ============================================================== 10 — BUDGET
s = slide(CREAM)
chrome(s, "الميزانية وسقف الاعتماد", kicker="الجنيه المصري · تقديرات تخطيط", section="الميزانية")
sc = [
    ("A · اقتصادي", "164,268", "191,418", "Cheops + Pre-function · 90 دعوة · 70–90 حضور",
     "أرضية التصميم المعتمدة", True),
    ("B · متوسط احترافي", "399,384", "465,834", "Tutankhamun II · 110 دعوة · 110–140 حضور",
     "يتطلب RFQ كاملًا", False),
    ("C · فاخر", "880,660", "1,026,310", "Tutankhamun I + نطاق خاص · 130 دعوة · 160–200 حضور",
     "غير مُوصى به في 5 أيام", False),
]
bw3 = (CW - Inches(0.44)) / 3
for i, (name, floor, ceil, desc, note, active) in enumerate(sc):
    x = W - M - bw3 - i * (bw3 + Inches(0.22))
    fill = NAVY if active else WHITE
    rect(s, x, Inches(1.72), bw3, Inches(2.9), fill=fill,
         line=None if active else FAINT, lw=Pt(0.75))
    rect(s, x, Inches(1.72), bw3, Inches(0.06), fill=GOLD if active else ROYAL)
    tcol = WHITE if active else INK
    scol = RGBColor(0xB9, 0xC6, 0xDC) if active else RGBColor(0x5A, 0x69, 0x86)
    text(s, x + Inches(0.2), Inches(1.92), bw3 - Inches(0.4), Inches(0.32),
         [(name, 15, GOLD if active else NAVY, True)], space_after=0)
    text(s, x + Inches(0.2), Inches(2.34), bw3 - Inches(0.4), Inches(0.24),
         [("الحد الأدنى التقديري (floor)", 10, scol, False)], space_after=0)
    text(s, x + Inches(0.2), Inches(2.56), bw3 - Inches(0.4), Inches(0.42),
         [(floor, 24, tcol, True, LAT)], space_after=0)
    text(s, x + Inches(0.2), Inches(3.06), bw3 - Inches(0.4), Inches(0.24),
         [("السقف المعتمد للاعتماد", 10, scol, False)], space_after=0)
    text(s, x + Inches(0.2), Inches(3.28), bw3 - Inches(0.4), Inches(0.42),
         [(ceil, 24, GOLD if active else ROYAL, True, LAT)], space_after=0)
    text(s, x + Inches(0.2), Inches(3.8), bw3 - Inches(0.4), Inches(0.44),
         [(desc, 10.5, scol, False)], space_after=0, line_spacing=1.16)
    text(s, x + Inches(0.2), Inches(4.28), bw3 - Inches(0.4), Inches(0.26),
         [(note, 10.5, GOLD if active else RED, True)], space_after=0)
rect(s, M, Inches(4.84), CW, Inches(1.35), fill=RGBColor(0xFD, 0xF6, 0xE6), line=GOLD, lw=Pt(1))
text(s, M + Inches(0.24), Inches(4.98), CW - Inches(0.48), Inches(0.28),
     [("كيف يُقرأ الرقم — ولماذا هو سقف وليس عرض سعر", 12.5, NAVY, True)], space_after=0)
text(s, M + Inches(0.24), Inches(5.3), CW - Inches(0.48), Inches(0.8),
     [("الأرقام = بنود 1–9 المسعّرة + احتياطي طوارئ (8% في A وB و10% في C) + هامش عدم يقين 25% "
       "مطبَّق على البنود غير المسعّرة (الفندق والضيافة والإنتاج والتصوير). **الفندق والضيافة "
       "وحدهما غير مسعّرين.** لذلك الرقم حدّ أعلى موحّد، وليس التزامًا — ولا يُصرف أي مبلغ قبل عرض سعر مكتوب.",
       11.5, INK, False)], space_after=0, line_spacing=1.24)

# ============================================================== 11 — MEASUREMENT
s = slide(CREAM)
chrome(s, "قياس النجاح: أربعة عناقيد مؤشرات", kicker="EVT · COM · EDU · EXE", section="القياس")
kpi = [
    ["العنقود", "ماذا يقيس", "مؤشرات", "المالك"],
    ["EVT · الحفل", "تنفيذ الحدث نفسه: الدعوات، التأكيد، الحضور، التغطية", "EVT-01 … EVT-08", "PM + LOG"],
    ["COM · التجاري", "مسار التحويل فقط: استفسار ← زيارة ← تقديم ← تسجيل", "COM-01 … COM-09", "CRM + FIN"],
    ["EDU · التعليمي", "الأثر التعليمي على 4 مستويات (كيركباتريك) + إتمام ملف الإنجاز", "EDU-01 … EDU-06", "CT + المعلمون"],
    ["EXE · التنفيذي", "الانضباط: نسبة إنجاز الخطة، انحراف الميزانية، المخاطر المتبقية", "EXE-01 … EXE-03", "PM + FIN"],
]
table(s, M, Inches(1.72), CW, kpi, [1.55, 4.0, 1.5, 1.35],
      header_h=Inches(0.42), row_h=Inches(0.46), head_size=11.5, body_size=10.5)
rect(s, M, Inches(4.2), CW, Inches(1.0), fill=NAVY)
text(s, M + Inches(0.24), Inches(4.34), CW - Inches(0.48), Inches(0.28),
     [("القاعدة الحاكمة", 12, GOLD, True)], space_after=0)
text(s, M + Inches(0.24), Inches(4.64), CW - Inches(0.48), Inches(0.46),
     [("لا يُنسب أي تحسّن في قيمة المدرسة إلى الحفل أو إلى المبادرة. "
       "كل مؤشر له تعريف ومصدر وخط أساس وتاريخ قياس — والأهداف مبدئية حتى أول قياس فعلي.",
       12, RGBColor(0xD5, 0xDF, 0xF0), False)], space_after=0, line_spacing=1.22)
rect(s, M, Inches(5.42), CW, Inches(1.3), fill=WHITE, line=FAINT, lw=Pt(0.75))
text(s, M + Inches(0.24), Inches(5.56), CW - Inches(0.48), Inches(0.28),
     [("المصنّف الذي يحمل الأرقام الحيّة", 12, NAVY, True)], space_after=0)
text(s, M + Inches(0.24), Inches(5.86), CW - Inches(0.48), Inches(0.72),
     [("`Green_Grow_Bot_Budget_and_KPIs.xlsx` — 11 ورقة: الميزانية بثلاثة سيناريوهات مع النماذج "
       "المحسوبة، ونموذج RFQ لطلب عروض الأسعار، ولوحتا مؤشرات للحفل والتجاري والتعليمي، "
       "وتكلفة البرنامج التعليمي على مستوى المرحلة. كل خانة formula حيّة.",
       11.5, INK, False)], space_after=0, line_spacing=1.22)

# ============================================================== 12 — RISKS
s = slide(CREAM)
chrome(s, "أهم المخاطر وكيف نخفّفها", kicker="سجل المخاطر — 15 خطرًا مرقّمًا", section="المخاطر")
risks = [
    ["#", "الخطر", "الاحتمال", "الأثر", "إجراء التخفيف", "المالك"],
    ["RSK-02", "عدم تأكيد حجز الفندق والقاعة", "مرتفع", "حرج", "RFQ فوري + قاعات بديلة", "LOG"],
    ["RSK-01", "عدم تأكيد الشخصيات المهمة", "مرتفع", "مرتفع", "دعوات مبكرة + متابعة فردية", "PRO"],
    ["RSK-04", "ضعف الحضور", "متوسط", "مرتفع", "3 موجات دعوة + خفض التكاليف", "PRO"],
    ["RSK-06", "عطل الصوت أو الشاشة", "منخفض", "مرتفع", "تشغيل من لابتوب مستقل + كابلات احتياطية", "TEC"],
    ["RSK-08", "عدم وجود موافقات التصوير", "متوسط", "مرتفع", "نموذج موافقة + لافتة «بدون تصوير»", "PR"],
    ["RSK-09", "استخدام شعار جهة دون إذن", "منخفض", "مرتفع", "قاعدة: بلا موافقة = بلا شعار", "PM"],
]
table(s, M, Inches(1.72), CW, risks, [1.0, 2.85, 0.85, 0.75, 3.0, 0.7],
      header_h=Inches(0.4), row_h=Inches(0.42), head_size=11, body_size=10)
rect(s, M, Inches(4.72), CW, Inches(1.5), fill=NAVY)
text(s, M + Inches(0.24), Inches(4.86), CW - Inches(0.48), Inches(0.28),
     [("قاعدة الـ5 أيام", 12.5, GOLD, True)], space_after=0)
text(s, M + Inches(0.24), Inches(5.18), CW - Inches(0.48), Inches(0.92),
     [("باقي 5 أيام. أي بند لا يُغلق كتابيًا خلال 24 ساعة يُسقط من النطاق ولا يُستبدل بافتراض. "
       "أول بندين يسقطان عند تعذّر التأكيد: (1) عدد المدعوين يُخفَّض إلى قاعدة 90 دعوة، "
       "(2) الاستقبال يُحوَّل إلى قاعة داخلية بالمدرسة. القرار يُسجَّل في الملف المرجعي قبل التنفيذ.",
       11.5, RGBColor(0xD5, 0xDF, 0xF0), False)], space_after=0, line_spacing=1.26)

# ============================================================== 13 — ROADMAP
s = slide(CREAM)
chrome(s, "خارطة الطريق: 90 يومًا بعد الحفل", kicker="من الإطلاق إلى القرار", section="ما بعد الحفل")
phases = [
    ("المرحلة 1", "1–7 نوفمبر", "تشغيل تجريبي", "الفصلان الأولان فقط · خط أساس لكل مؤشر · نموذج تسجيل بسيط", ROYAL),
    ("المرحلة 2", "8–30 نوفمبر", "تثبيت", "تدريب المعلمين · أول قياس · حزمة شفافية · مسار التحويل", ROYAL),
    ("المرحلة 3", "31–60 ديسمبر", "توسيع", "4 فصول · لوحة KPI شهرية · أول ورشة شركاء · دليل المعلم", GOLD),
    ("المرحلة 4", "61–90 يومًا", "قرار التوسع", "قرار موثّق: نوسّع / نعدّل / نوقف · نموذج التكلفة", GOLD),
]
pw4 = (CW - Inches(0.54)) / 4
for i, (ph, days, title, body, acc) in enumerate(phases):
    x = W - M - pw4 - i * (pw4 + Inches(0.18))
    rect(s, x, Inches(1.78), pw4, Inches(2.45), fill=WHITE, line=FAINT, lw=Pt(0.75))
    rect(s, x, Inches(1.78), pw4, Inches(0.05), fill=acc)
    text(s, x + Inches(0.16), Inches(1.96), pw4 - Inches(0.32), Inches(0.26),
         [(ph, 11, RGBColor(0x6B, 0x7A, 0x96), True)], space_after=0)
    text(s, x + Inches(0.16), Inches(2.24), pw4 - Inches(0.32), Inches(0.32),
         [(days, 15, NAVY, True)], space_after=0)
    text(s, x + Inches(0.16), Inches(2.62), pw4 - Inches(0.32), Inches(0.3),
         [(title, 13, acc if acc == GOLD else ROYAL, True)], space_after=0)
    text(s, x + Inches(0.16), Inches(3.0), pw4 - Inches(0.32), Inches(1.1),
         [(body, 10.5, INK, False)], space_after=0, line_spacing=1.2)
    if i < 3:
        text(s, x - Inches(0.18), Inches(2.78), Inches(0.18), Inches(0.3),
             [("‹", 16, GOLD, True, LAT)], align=PP_ALIGN.CENTER, space_after=0)
rect(s, M, Inches(4.5), CW, Inches(1.7), fill=WHITE, line=FAINT, lw=Pt(0.75))
text(s, M + Inches(0.24), Inches(4.64), CW - Inches(0.48), Inches(0.28),
     [("بوابات القرار عبر التسعين يومًا", 12.5, NAVY, True)], space_after=0)
gates2 = [
    ("بعد 7 أيام", "تشغيل تجريبي سليم في فصلين + خط أساس مثبّت لكل مؤشر", ROYAL),
    ("بعد 30 يومًا", "أول قياس EDU-02 + حزمة شفافية معلنة + مسار تحويل يعمل", GOLD),
    ("بعد 60 يومًا", "تكلفة الطيار مُثبتة + قرار شراكة موثّق واحد على الأقل", ROYAL),
    ("بعد 90 يومًا", "قرار موثّق: نوسّع / نعدّل / نوقف — على بيانات لا على انطباع", GOLD),
]
gw2 = (CW - Inches(0.72)) / 4
for i, (k, v, c) in enumerate(gates2):
    x = W - M - gw2 - i * gw2
    text(s, x, Inches(5.04), gw2 - Inches(0.12), Inches(0.26),
         [(k, 11, c, True)], space_after=0)
    text(s, x, Inches(5.32), gw2 - Inches(0.12), Inches(0.76),
         [(v, 10.5, INK, False)], space_after=0, line_spacing=1.2)

# ============================================================== 14 — DECISIONS
s = slide(CREAM)
chrome(s, "القرارات المطلوبة خلال 24 ساعة", kicker="لا يُنفَّذ شيء بلا قرار مكتوب", section="القرارات")
dec = [
    ["#", "القرار", "الخيارات", "الموعد", "المالك"],
    ["1", "حجز القاعة والفندق", "أ) تأكيد كتابي · ب) قاعة بديلة · ج) قاعة داخلية بالمدرسة", "اليوم", "LOG + PM"],
    ["2", "سقف الإنفاق", "أ) 191,418 (A) · ب) 465,834 (B) · ج) 1,026,310 (C)", "اليوم", "FIN + PM"],
    ["3", "عدد الدعوات", "أ) 90 (A) · ب) 110 (B) · ج) 130 (C)", "اليوم", "PM"],
    ["4", "الصفة الرسمية بجوار الاسم", "أ) «رئيس مبادرات التعليم التطبيقي» · ب) «صاحب مبادرة GGB»", "اليوم", "PR"],
    ["5", "اعتماد شعار AXMIND", "أ) موقّع كتابيًا · ب) لا يظهر في أي مادة", "اليوم", "PR + PM"],
    ["6", "موافقات التصوير", "نموذج موافقة + عتبة ≥ 60% قبل التصوير", "12 نوفمبر", "PR + LOG"],
    ["7", "بيانات RSVP", "هاتف · بريد · رابط · رمز مصدر لكل استفسار", "11 نوفمبر", "CRM"],
]
table(s, M, Inches(1.7), CW, dec, [0.4, 2.35, 4.45, 1.0, 1.1],
      header_h=Inches(0.4), row_h=Inches(0.43), head_size=11, body_size=10)
rect(s, M, Inches(5.35), CW, Inches(1.3), fill=RGBColor(0xFD, 0xF6, 0xE6), line=GOLD, lw=Pt(1))
text(s, M + Inches(0.24), Inches(5.49), CW - Inches(0.48), Inches(0.28),
     [("القاعدة", 12.5, NAVY, True)], space_after=0)
text(s, M + Inches(0.24), Inches(5.8), CW - Inches(0.48), Inches(0.7),
     [("تُعتمد البنود من PM عبر قرارات موثّقة، وتُسجَّل في الملف المرجعي. "
       "كل بند بلا قرار مكتوب يبقى «معلَّقًا» — ولا يظهر في أي مادة مطبوعة ولا يُعلَن شفهيًا. "
       "هذا الشرط يحمي المدرسة من مخاطرة غير موثّقة.", 11.5, INK, False)], space_after=0, line_spacing=1.24)

# ============================================================== 15 — WHAT WE ASK
s = slide(NAVY)
chrome(s, "ما الذي نطلبه منكم اليوم", kicker="ثلاثة طلبات محددة", section="الخلاصة", dark=True)
asks = [
    ("1", "أقرّوا سقف 191,418 ج.م", "أرضية تصميم لسيناريو A: 90 دعوة، قاعة Cheops، إنتاج أساسي. "
     "لا يُصرف مبلغ قبل عرض سعر مكتوب."),
    ("2", "أغلقوا السبعة قرارات", "خلال 24 ساعة — البنود أعلاه. كل بند بلا قرار يبقى معلَّقًا "
     "ويُحذف من المواد."),
    ("3", "ادعموا زخم الجلسة", "مشاركتكم كشريك تطبيقي — Universities بالمعايير، القطاع الخاص "
     "بالدعم، المدارس بتبادل الخبرة."),
]
aw = (CW - Inches(0.44)) / 3
for i, (n, h, b) in enumerate(asks):
    x = W - M - aw - i * (aw + Inches(0.22))
    rect(s, x, Inches(1.85), aw, Inches(2.35), fill=AXNAVY, line=RGBColor(0x27, 0x3C, 0x66), lw=Pt(0.75))
    rect(s, x, Inches(1.85), aw, Inches(0.05), fill=GOLD)
    text(s, x + Inches(0.2), Inches(2.06), Inches(0.8), Inches(0.5),
         [(n, 30, GOLD, True, LAT)], align=PP_ALIGN.LEFT, space_after=0)
    text(s, x + Inches(0.2), Inches(2.66), aw - Inches(0.4), Inches(0.56),
         [(h, 15, WHITE, True)], space_after=0, line_spacing=1.08)
    text(s, x + Inches(0.2), Inches(3.26), aw - Inches(0.4), Inches(0.85),
         [(b, 11, RGBColor(0xB9, 0xC6, 0xDC), False)], space_after=0, line_spacing=1.22)
rect(s, M, Inches(4.55), CW, Inches(1.72), fill=WHITE)
text(s, M + Inches(0.3), Inches(4.72), CW - Inches(0.6), Inches(0.3),
     [("ما نلتزم به تجاهكم", 13, NAVY, True)], space_after=0)
bullets(s, M + Inches(0.3), Inches(5.08), CW - Inches(0.6), Inches(1.05),
        ["لا ادّعاء غير مثبت: لا وظائف، لا قبول جامعي، لا «معتمد من الدولة»، لا رعاية بلا موافقة.",
         "كل رقم معلن له مصدر في حقيبة الصحفيين — وما لا نعرفه نعلن أنه غير معروف.",
         "قياس معلن مسبقًا، وخط أساس يُملأ من أول قياس فعلي — لا من تقدير."],
        size=11.5, color=INK, gap=5)

# ============================================================== 16 — BACK COVER
s = slide(NAVY)
rect(s, 0, H - Inches(1.65), W, Inches(1.65), fill=AXNAVY)
logo_plaque(s, W - M - Inches(1.18), Inches(0.5), Inches(1.35))
text(s, M, Inches(1.25), Inches(9.4), Inches(1.5),
     [("شكرًا لكم", 40, WHITE, True),
      ("من التعليم إلى الابتكار — مشروع واحد يتطور مع الطالب", 19, GOLD, True)],
     space_after=10, line_spacing=1.06)
rect(s, W - M - Inches(3.4), Inches(2.72), Inches(3.4), Inches(0.03), fill=GOLD)
text(s, M, Inches(2.98), Inches(9.0), Inches(1.2),
     [("Green International Schools · Al Obour, Egypt", 14, RGBColor(0xC7, 0xD3, 0xE8), False, LAT, False),
      ("الأحد 15 نوفمبر 2026 · فندق JW Marriott Hotel Cairo", 13, RGBColor(0xC7, 0xD3, 0xE8), False)],
     space_after=6)
info = [("المسؤول", "[الاسم]"), ("البريد", "[البريد الإلكتروني]"),
        ("الهاتف", "[رقم الهاتف]"), ("المنصة الرسمية", "[الرابط]")]
iw = (CW - Inches(0.36)) / 4
for i, (k, v) in enumerate(info):
    x = W - M - iw - i * iw
    text(s, x, Inches(4.22), iw - Inches(0.1), Inches(0.26),
         [(k, 10, MUTED, False)], space_after=0)
    text(s, x, Inches(4.5), iw - Inches(0.1), Inches(0.3),
         [(v, 12, GOLD, True)], space_after=0)
chip(s, M, Inches(5.05), Inches(1.72), Inches(0.34), "#GreenGrowBot", fill=AXNAVY, color=GOLD, size=11, rtl=False)
text(s, M, Inches(6.25), Inches(11.5), Inches(0.4),
     [("Green Grow Bot · حقيبة الصحفيين والعرض التنفيذي · نسخة 10 نوفمبر 2026 · "
       "كل الأرقام التقديرية معلَّمة بمصدرها «تقدير» أو «يحتاج تأكيد»",
       10, MUTED, False)], space_after=0)

prs.save(OUT)
print("saved:", OUT)
print("slides:", len(prs.slides.__iter__.__self__._sldIdLst))
