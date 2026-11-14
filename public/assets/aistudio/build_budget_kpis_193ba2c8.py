# -*- coding: utf-8 -*-
"""Green Grow Bot — Budget & KPIs workbook (openpyxl)."""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule
from openpyxl.worksheet.datavalidation import DataValidation

OUT = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"

NAVY = "0B1B3D"; GOLD = "D4AF37"; CREAM = "FBF9F4"; SILVER = "E5E7EB"
GREEN = "C6EFCE"; AMBER = "FFEB9C"; RED = "FFC7CE"; GREY = "F2F2F2"
HDR = PatternFill("solid", fgColor=NAVY)
SUB = PatternFill("solid", fgColor="E8ECF5")
INP = PatternFill("solid", fgColor="FFF9E3")
TOT = PatternFill("solid", fgColor="F3E9CF")
F_HDR = Font(name="Dubai", size=10, bold=True, color=GOLD)
F_BODY = Font(name="Dubai", size=10, color="16233F")
F_BOLD = Font(name="Dubai", size=10, bold=True, color="16233F")
F_TITLE = Font(name="Dubai", size=15, bold=True, color=NAVY)
F_SMALL = Font(name="Dubai", size=8.5, color="5A6478")
THIN = Side(style="thin", color="C9D0E0")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
AL_R = Alignment(horizontal="right", vertical="center", wrap_text=True)
AL_C = Alignment(horizontal="center", vertical="center", wrap_text=True)
AL_L = Alignment(horizontal="left", vertical="center", wrap_text=True)
MONEY = '#,##0" ج.م"'

wb = Workbook()


def sheet(title):
    ws = wb.create_sheet(title)
    ws.sheet_view.rightToLeft = True
    ws.sheet_view.showGridLines = False
    return ws


def head_row(ws, row, headers, widths):
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = F_HDR; c.fill = HDR; c.border = BOX; c.alignment = AL_C
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 34


def title_block(ws, title, sub, span=7):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=span)
    c = ws.cell(row=1, column=1, value=title); c.font = F_TITLE; c.alignment = AL_R
    ws.row_dimensions[1].height = 26
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=span)
    c = ws.cell(row=2, column=1, value=sub); c.font = F_SMALL; c.alignment = AL_R
    ws.row_dimensions[2].height = 30


def note(ws, row, text, span=7):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=span)
    c = ws.cell(row=row, column=1, value=text); c.font = F_SMALL; c.alignment = AL_R
    ws.row_dimensions[row].height = 28


# ---------------------------------------------------------------- scenarios
SCEN = {
    "A - اقتصادي": {
        "desc": "Cheops (352 م²) + Pre-function · 90 دعوة · 70–90 حضور · إنتاج داخلي · احتياطي 8%",
        "rate": 0.08,
        "items": [
            ("قاعة وخدمات الفندق (Cheops + Pre-function، 6 ساعات)", "تقدير", 45000, "F",
             "يحتاج عرض سعر — التقدير حد أدنى للتخطيط"),
            ("الضيافة (بوفيه مفتوح)", "180 × 220", 39600, "F",
             "سعر الفندق الفعلي مرتفع عادة — تحقق إلزامي"),
            ("التصميم والطباعة (دعوة A5 ×180 + لوحات ×12)", "تقدير", 11500, "F",
             "مقابل عروض المطابع"),
            ("التوصيل الرقمي (نسخ دعوة + تغطية)", "تقدير", 3500, "F", ""),
            ("تجهيز النموذج الأولي (قطع + تجميع + نسخة احتياطية)", "تقدير", 18500, "F",
             "أسعار المكونات: electronicsegypt.com 28 Oct 2026"),
            ("الصوت والإضاءة والشاشة (تجاوز ما يوفره الفندق)", "تقدير", 9000, "F", ""),
            ("التصوير (3 ساعات) + مونتاج سريع 48 ساعة", "تقدير", 15000, "F", ""),
            ("مطبوعات متنوعة (كروت، تذاكر، شهادات)", "تقدير", 6000, "F", ""),
            ("مواصلات وتوصيل دعوات", "تقدير", 4000, "F", ""),
        ],
        "unpriced": "D5+D6+D10+D11",
    },
    "B - متوسط احترافي": {
        "desc": "Tutankhamun Section II + Pre-function · 110 دعوة · 110–140 حضور · إنتاج مختلط · احتياطي 8%",
        "rate": 0.08,
        "items": [
            ("قاعة Tutankhamun Section II + Pre-function (8 ساعات)", "تقدير", 95000, "F",
             "يحتاج عرض سعر"),
            ("الضيافة (بوفيه + قهوة + كيك)", "240 × 420", 100800, "F",
             "سعر الفندق الفعلي مرتفع عادة — تحقق إلزامي"),
            ("التصميم والطباعة المتكامل (دعوة، كتيّب، لوحات، شهادات، تذاكر)", "تقدير", 28000, "F", ""),
            ("توصيل رقمي + إدارة دعوات", "تقدير", 9000, "F", ""),
            ("نموذج أولي متكامل (روبوتان فعليان + عرض حي + احتياطي)", "تقدير", 42000, "F", ""),
            ("الصوت والإضاءة + شاشتان + مراقبة", "تقدير", 32000, "F", ""),
            ("تصوير + فيديو + مونتاج 72 ساعة + محتوى", "تقدير", 38000, "F", ""),
            ("مجموعات عمل ومطبوعات تعليمية", "تقدير", 14000, "F", ""),
            ("لوجستيات ومأذونات ونقل", "تقدير", 11000, "F", ""),
        ],
        "unpriced": "D5+D6+D10+D11",
    },
    "C - فاخر": {
        "desc": "Tutankhamun Section I + Pre-function + استقبال خاص · 130 دعوة · 160–200 حضور · إنتاج كامل · احتياطي 10%",
        "rate": 0.10,
        "items": [
            ("قاعة Tutankhamun Section I + Pre-function + استقبال خاص", "تقدير", 180000, "F",
             "يحتاج عرض سعر"),
            ("الضيافة الفاخرة (3 كاونترات + محطة قهوة + كيك + عشاء خفيف)", "320 × 780", 249600, "F",
             "سعر الفندق الفعلي مرتفع عادة — تحقق إلزامي"),
            ("الهوية والتصميم والطباعة", "تقدير", 65000, "F", ""),
            ("توصيل رقمي وإدارة دعوات", "تقدير", 18000, "F", ""),
            ("نموذج أولي (3 روبوتات + محطة عرض + احتياطي)", "تقدير", 85000, "F", ""),
            ("الإنتاج الفني (مسرح، إضاءة، صوت، شاشات، مؤثرات)", "تقدير", 78000, "F", ""),
            ("التصوير والفيديو والمونتاج + أفلام + بث", "تقدير", 75000, "F", ""),
            ("محتوى تعليمي ومطبوعات وجلسات موازية", "تقدير", 28000, "F", ""),
            ("لوجستيات ومأذونات ونقل", "تقدير", 22000, "F", ""),
        ],
        "unpriced": "D5+D6+D10+D11",
    },
}

scen_rows = {}
for name, s in SCEN.items():
    ws = sheet(name)
    title_block(ws, f"ميزانية الحفل — السيناريو {name}", s["desc"], span=7)
    head_row(ws, 4,
             ["#", "البند", "أساس التسعير", "التقدير المبدئي", "عرض السعر الفعلي", "الفارق", "المصدر / ملاحظات"],
             [5, 46, 20, 18, 18, 14, 40])
    r = 5
    for i, (item, basis, amt, tag, memo) in enumerate(s["items"], start=1):
        vals = [i, item, basis, amt, None, None, memo]
        for ci, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=ci, value=v); c.border = BOX; c.font = F_BODY
            c.alignment = AL_C if ci in (1, 3) else (AL_L if ci == 7 else AL_R)
            if ci == 4:
                c.number_format = MONEY; c.fill = SUB
            if ci == 5:
                c.fill = INP; c.number_format = MONEY
            if ci == 6:
                c.number_format = MONEY
                c.value = f"=IF(E{r}=\"\",\"\",E{r}-D{r})"
        ws.row_dimensions[r].height = 30
        r += 1
    last = r - 1
    rows = {}
    def put(rr, label, formula, fill=None, bold=True, fmt=MONEY, note_txt=""):
        ws.merge_cells(start_row=rr, start_column=2, end_row=rr, end_column=3)
        c = ws.cell(row=rr, column=2, value=label)
        c.font = F_BOLD if bold else F_BODY; c.border = BOX; c.alignment = AL_R
        ws.cell(row=rr, column=3).border = BOX
        v = ws.cell(row=rr, column=4, value=formula)
        v.number_format = fmt; v.border = BOX; v.alignment = AL_C
        v.font = F_BOLD; v.fill = fill or SUB
        ws.cell(row=rr, column=5).border = BOX
        ws.cell(row=rr, column=6).border = BOX
        nc = ws.cell(row=rr, column=7, value=note_txt); nc.font = F_SMALL; nc.border = BOX; nc.alignment = AL_L
        ws.row_dimensions[rr].height = 22
        rows[label] = rr

    put(last + 1, "إجمالي البنود 1–9 (تقديري)", f"=SUM(D5:D{last})", TOT,
        note_txt="لا يشمل الاحتياطي ولا هامش عدم اليقين")
    put(last + 2, "احتياطي الطوارئ", f"=ROUND(D{last+1}*{s['rate']},0)", SUB,
        note_txt=f"{int(s['rate']*100)}% من إجمالي البنود")
    put(last + 3, "الإجمالي التقديري (floor) — حد أدنى للتخطيط", f"=D{last+1}+D{last+2}", TOT,
        note_txt="لا يُعتمد كميزانية قبل وصول عروض الأسعار")
    put(last + 4, "مجموع البنود غير المسعّرة (1، 2، 6، 7)", f"={s['unpriced']}", SUB,
        note_txt="الفندق والضيافة والإنتاج الفني والتصوير")
    put(last + 5, "هامش عدم اليقين 25% على البنود غير المسعّرة", f"=ROUND(D{last+4}*0.25,0)", SUB,
        note_txt="سقف أمان تعويضي حتى تصل عروض الأسعار")
    put(last + 6, "السقف المعتمد للاعتماد", f"=D{last+3}+D{last+5}", TOT,
        note_txt="الحد الأقصى المسموح بالصرف")
    put(last + 7, "الفرق: السقف − التقدير المبدئي", f"=D{last+6}-D{last+3}", SUB,
        note_txt="حجم المخاطرة المالية")
    scen_rows[name] = dict(sheet=name, floor=last + 3, ceiling=last + 6, sub=last + 1)
    note(ws, last + 9,
         "⚠ جميع الأرقام تقديرات تخطيط وليست عروض أسعار. بنود الفندق والضيافة والإنتاج الفني غير مسعّرة. "
         "عمود «عرض السعر الفعلي» يُملأ من نموذج RFQ المرفق، وعمود «الفارق» يحسب تلقائيًا. "
         "مصادر أسعار المكونات: electronicsegypt.com (أسعار محدّثة 28 أكتوبر 2026).", span=7)
    note(ws, last + 10,
         "الضرائب والخدمات المستثناة من النطاق: ضريبة القيمة المضافة (غير محتسبة)، بدل المبيت، تأجير معدات المطبخ، "
         "الترجمة Simultaneous، هدايا الضيوف فوق التذاكر، أتعاب المورّد، التأمين الإضافي، وأي رسوم غير مذكورة — كلها تحتاج تأكيد.", span=7)
    ws.freeze_panes = "A5"

# ---------------------------------------------------------------- summary
ws = sheet("الملخص")
title_block(ws, "Green Grow Bot — ملخص الميزانية وسيناريوهات الحفل",
            "الأحد 15 نوفمبر 2026 — فندق JW Marriott Hotel Cairo. جميع الأرقام تقديرات تخطيط (ج.م) قابلة للتعديل؛ "
            "الأعمدة calculable تُحدَّث تلقائيًا من أوراق السيناريوهات.", span=8)
head_row(ws, 4,
         ["البُعد", "A — اقتصادي منضبط", "B — متوسط احترافي", "C — فاخر", "المصدر / الملاحظة"],
         [34, 22, 22, 22, 52])
rows_cmp = [
    ("حجم الحضور المستهدف", "70–90", "110–140", "160–200", "EVT-03"),
    ("عدد الدعوات المرسلة", "90", "110", "130", "EVT-01"),
    ("القاعة المقترحة", "Cheops (352 م²)", "Tutankhamun Sec. II (578 م²)", "Tutankhamun Sec. I", "السعة من موقع الفندق"),
    ("مستوى الضيافة", "بوفيه مفتوح", "بوفيه + قهوة + كيك", "3 كاونترات + عشاء خفيف", "سعر الفندق غير مؤكد"),
    ("الإنتاج الفني", "صوت وإضاءة أساسية", "تصميم مسرح + شاشتان", "إنتاج كامل + مؤثرات", ""),
    ("التصوير والمونتاج", "3 ساعات + 48 ساعة", "72 ساعة + محتوى", "فيلم + بث + محتوى", ""),
    ("معدات العرض", "روبوت + احتياطي", "روبوتان + محطة", "3 روبوتات + محطة", ""),
    ("نسبة احتياطي الطوارئ", "8%", "8%", "10%", ""),
]
r = 5
for lbl, a, b, c_, memo in rows_cmp:
    ws.cell(row=r, column=1, value=lbl).font = F_BOLD
    for ci, v in zip((2, 3, 4), (a, b, c_)):
        cc = ws.cell(row=r, column=ci, value=v); cc.font = F_BODY; cc.alignment = AL_C
    ws.cell(row=r, column=5, value=memo).font = F_SMALL
    for ci in range(1, 6):
        ws.cell(row=r, column=ci).border = BOX
        ws.cell(row=r, column=ci).fill = SUB if r % 2 else PatternFill()
    r += 1
fin_rows = [
    ("إجمالي البنود 1–9 (تقديري)", "sub"),
    ("الإجمالي التقديري (floor)", "floor"),
    ("هامش عدم اليقين 25%", "unc"),
    ("السقف المعتمد للاعتماد", "ceiling"),
]
for lbl, key in fin_rows:
    ws.cell(row=r, column=1, value=lbl).font = F_BOLD
    for ci, (sname, keys) in zip((2, 3, 4), [(s, scen_rows[s]) for s in SCEN]):
        src = {"sub": keys["sub"], "floor": keys["floor"], "ceiling": keys["ceiling"], "unc": keys["ceiling"] - 1}[key]
        cc = ws.cell(row=r, column=ci, value=f"='{sname}'!D{src}")
        cc.number_format = MONEY; cc.font = F_BOLD; cc.alignment = AL_C; cc.fill = TOT; cc.border = BOX
    ws.cell(row=r, column=1).border = BOX
    ws.cell(row=r, column=5, value="محسوب تلقائيًا من أوراق السيناريوهات").font = F_SMALL
    ws.cell(row=r, column=5).border = BOX
    r += 1
note(ws, r + 1,
     "قاعدة الاعتماد: لا يُصرف أي مبلغ قبل استلام عروض أسعار مكتوبة. "
     "السيناريو المعتمد: [ ] · سقف الإنفاق المعتمد: [ ] ج.م · تاريخ تجميد الميزانية: 14 نوفمبر 2026.", span=8)
note(ws, r + 2,
     "مؤشرات مرتبطة: EVT-08 تكلفة الحضور = التكلفة الفعلية ÷ الحضور الفعلي · EXE-02 انحراف الميزانية = (المعتمد − الفعلي) ÷ المعتمد.", span=8)

# ---------------------------------------------------------------- RFQ
ws = sheet("نموذج RFQ")
title_block(ws, "نموذج طلب عرض سعر (RFQ) — للمورد والفندق",
            "تُرسل البنود 1، 4، 5، 6، 7، 8، 9 كتابيًا إلى كل مورد. خانة السعر تُملأ بعرض السعر الرسمي المؤرَّخ فقط.", span=5)
head_row(ws, 4, ["#", "البند / السؤال", "الرد المطلوب", "قيمة عرض السعر", "تاريخ العرض / اسم المورّد"],
         [5, 42, 40, 20, 30])
rfq = [
    ("نوع الخدمة المطلوبة", "☐ قاعة وخدمات ☐ تجهيز فني ☐ ضيافة ☐ طباعة ☐ إنتاج ☐ استشارات ☐ تصوير ☐ أخرى: ______"),
    ("المواصفات المرفقة", "ملحق (أ) جدول التجهيزات · ملحق (ب) مخطط المكان · ملحق (ج) جدول الضيافة"),
    ("التاريخ والوقت", "الأحد 15 نوفمبر 2026 — من ______ إلى ______ (تشمل بحد استقبال الضيوف)"),
    ("مدة الاستعداد", "من ______ إلى ______ (تشمل التركيب والفحص والتشغيل وإزالة التجهيزات)"),
    ("عدد الضيوف المتوقع", "☐ 70–90  ☐ 110–140  ☐ 160–200  ☐ ________ (يُحدَّد بعد اعتماد السيناريو)"),
    ("الخدمات المشمولة", "________________________________________________________________________"),
    ("ما لا يشمله العرض", "________________________________________________________________________"),
    ("الضريبة والتضمين", "العرض شامل ضريبة القيمة المضافة؟  ☐ نعم  ☐ لا  ☐ غير محدد — مرفق الشهادة ☐"),
    ("مدة صلاحية العرض", "العرض صالح حتى ____ / ____ / 2026"),
    ("شرط الدفع", "____% عند الحجز · ____% عند التنفيذ · ____% بعد التسليم — أو حسب عرضكم: ______________"),
    ("الشروط الإلزامية (التشغيل)", "موظف تقني مخصّص · بديل فوري في حال عطل · سرية بيانات الضيوف ·不许 تصوير دون إذن"),
    ("التأمين والتراخيص", "________________________________________________________________________"),
    ("جهات الاتصال", "اسم: ______  الهاتف: ______  البريد: ______"),
    ("ملاحظات المورّد", "________________________________________________________________________"),
]
r = 5
for i, (q, ans) in enumerate(rfq, start=1):
    ws.cell(row=r, column=1, value=i).font = F_BODY
    ws.cell(row=r, column=2, value=q).font = F_BOLD
    ws.cell(row=r, column=3, value=ans).font = F_BODY
    ws.cell(row=r, column=4, value=None).fill = INP
    ws.cell(row=r, column=5, value=None).fill = INP
    for ci in range(1, 6):
        cc = ws.cell(row=r, column=ci); cc.border = BOX
        if ci in (1, 2, 4, 5): cc.alignment = AL_C if ci in (1, 4, 5) else AL_R
        else: cc.alignment = AL_R
    ws.row_dimensions[r].height = 32
    r += 1
note(ws, r + 1, "تُحفظ نسخة من كل عرض في مجلد الموردين مع تاريخ الاستلام، ويُحدَّث عمود «عرض السعر» في ورقة السيناريو.", span=5)

# ---------------------------------------------------------------- program cost
ws = sheet("تكلفة البرنامج التعليمي")
title_block(ws, "نموذج تكلفة تشغيل المراحل التعليمية (تقديري)",
            "مصدر أسعار المكونات: electronicsegypt.com — أسعار محدّثة 28 أكتوبر 2026. أسعار المنصات التعليمية "
            "(WhalesBot / LEGO Education / micro:bit) تحتاج عرض سعر من مورّد. الأرقام تقديرات تخطيط وليست عروض أسعار.", span=6)
head_row(ws, 4, ["المرحلة", "الصفوف", "المنصة المرجعية", "تكلفة تجهيز شعبة (30 طالبًا)", "تكلفة الطالب", "ملاحظات"],
         [34, 14, 30, 24, 18, 46])
prog = [
    ("1 — الاستكشاف الحسي والبناء البسيط", "KG1–KG2", "WhalesBot U20 Pro / كتل بناء", 24596, 24596, "سعر الوأس: ~24,596 ج.م (eg.shagoof.com) أو US$305 مباشرًا"),
    ("2 — الحركة والأشكال والآليات", "G1–G2", "LEGO Education WeDo 2.0", 0, 0, "يحتاج عرض سعر — يُملأ"),
    ("3 — الدوائر الإلكترونية الآمنة", "G3", "micro:bit + LED/بزر/جرس", 0, 0, "يحتاج عرض سعر + مكونات (Arduino 239، ESP32 280)"),
    ("4 — البرمجة المرئية", "G4–G5", "LEGO Spike Prime / micro:bit + PictoBlox", 0, 0, "يحتاج عرض سعر"),
    ("5 — الحساسات وجمع البيانات", "G6", "Arduino Uno + HC-SR04/DHT22/LM35/MPU-6050", 0, 0, "قطع مفردة: 239 + 65 + 45 + 110 ≈ 459 ج.م للطالب"),
    ("6 — التحكم والحركة", "G7–G8", "Arduino + L298N/ULN2003 + MG995/28BYJ-48", 0, 0, "قطع: 239 + 25 + 175 + 65 = 504 ج.م للطالب"),
    ("7 — التصميم الهندسي وحل المشكلات", "G9–G10", "محاكاة (Tinkercad/Wokwi) + CAD", 0, 0, "برمجيات/مختبر تصنيع — يحتاج تسعيرًا"),
    ("8 — الأنظمة المتكاملة", "G11", "ESP32 + IoT + MIT App Inventor", 0, 0, "ESP32 280 + OLED 265 + SIM800L 275 للطالب"),
    ("9 — مشروع التخرج", "G12", "تطبيقي + ملف إنجاز + معرض", 0, 0, "يعتمد على تجهيزات المرحلة 8 + قاعة عرض"),
]
r = 5
for stg, gr, plat, branch, per, memo in prog:
    ws.cell(row=r, column=1, value=stg).font = F_BOLD
    ws.cell(row=r, column=2, value=gr).font = F_BODY
    ws.cell(row=r, column=3, value=plat).font = F_BODY
    c = ws.cell(row=r, column=4, value=branch); c.number_format = MONEY; c.fill = INP
    c = ws.cell(row=r, column=5, value=per); c.number_format = MONEY; c.fill = INP
    ws.cell(row=r, column=6, value=memo).font = F_SMALL
    for ci in range(1, 7):
        cc = ws.cell(row=r, column=ci); cc.border = BOX
        cc.alignment = AL_L if ci == 6 else (AL_C if ci in (2, 4, 5) else AL_R)
    ws.row_dimensions[r].height = 28
    r += 1
ws.cell(row=r + 1, column=1, value="إجمالي معروف فقط (المرحلة 1)").font = F_BOLD
c = ws.cell(row=r + 1, column=4, value=f"=SUM(D5:D{r-1})"); c.number_format = MONEY; c.font = F_BOLD; c.fill = TOT; c.border = BOX
c = ws.cell(row=r + 1, column=5, value=f"=SUM(E5:E{r-1})"); c.number_format = MONEY; c.font = F_BOLD; c.fill = TOT; c.border = BOX
note(ws, r + 3,
     "ملاحظة: التكلفة التشغيلية الكاملة للبرنامج تشمل أيضًا زمن المعلمين، ومساحة المختبر، وكتابة المحتوى، "
     "والتدريب — وهي غير محتسبة هنا لأنها غير مرتبطة بعدد الطلاب مباشرة. تُقدَّر في مرحلة التشغيل التجريبي (المرحلة 2 من خارطة 90 يومًا).", span=6)

# ---------------------------------------------------------------- KPI sheets
KPI_HEAD = ["ID", "المؤشر", "التعريف", "معادلة الحساب", "المصدر", "المسؤول", "التوقيت",
            "خط الأساس", "الهدف المبدئي", "القيمة الفعلية", "طريقة التحقق", "الحالة"]
KPI_W = [9, 30, 40, 34, 22, 16, 20, 16, 18, 16, 34, 14]

def kpi_sheet(name, title, sub, rows):
    ws = sheet(name)
    title_block(ws, title, sub, span=12)
    head_row(ws, 4, KPI_HEAD, KPI_W)
    r = 5
    for row in rows:
        for ci, v in enumerate(row, start=1):
            c = ws.cell(row=r, column=ci, value=v)
            c.border = BOX; c.font = F_BODY
            c.alignment = AL_C if ci in (1, 6, 8, 9, 10, 12) else AL_R
            if ci == 9: c.fill = SUB
            if ci == 10: c.fill = INP
            if ci in (8, 9) and isinstance(v, (int, float)): c.number_format = '#,##0'
        ws.row_dimensions[r].height = 30
        r += 1
    note(ws, r + 1,
         "الأعمدة الصفراء (القيمة الفعلية) تُملأ بالبيانات الفعلية. عمود «الهدف المبدئي» = هدف افتراضي لم يُتحقق بعد "
         "ويُعاد ضبطه بعد أول قياس. خط الأساس يُستخرج من النظام قبل بدء القياس «بعد».", span=12)
    ws.freeze_panes = "C5"
    return ws

EVT = [
    ("EVT-01", "عدد الدعوات المرسلة", "عدد الدعوات المُرسلة فعليًا", "عدّ سجل الدعوات", "سجل الدعوات", "PRO", "31 أكتوبر 2026", 0, 90, None, "مطابقة سجل الإرسال", "مبدئي"),
    ("EVT-02", "نسبة تأكيد الحضور", "نسبة الدعوات التي تأكيدت", "(المؤكدة ÷ المرسلة) × 100", "سجل الدعوات", "PRO", "9 نوفمبر 2026", 0, 45, None, "مطابقة RSVP بالقوائم", "مبدئي"),
    ("EVT-03", "الحضور الفعلي", "عدد الحاضرين فعليًا", "عدّ البوابة", "تسجيل البوابة", "مشرف القاعة", "15 نوفمبر 2026", 0, 90, None, "قسمة تذاكر الدخول", "مبدئي"),
    ("EVT-04", "نسبة الحضور من المؤكدين", "نسبة المرتبطين الحاضرين", "(الحاضرون ÷ المؤكدون) × 100", "البوابة + RSVP", "مشرف القاعة", "15 نوفمبر 2026", 0, 80, None, "مطابقة الأسماء", "مبدئي"),
    ("EVT-05", "الاجتماعات التعاونية بعد الحفل", "عدد الاجتماعات خلال 30 يومًا", "عدّ من CRM", "CRM", "CT", "15 ديسمبر 2026", 0, 6, None, "سجل CRM + محاضر", "مبدئي"),
    ("EVT-06", "فرص الشراكة المؤهلة", "فرص بملف ومالك ومسار", "عدّ من سجل الفرص", "سجل الفرص", "CT", "15 ديسمبر 2026", 0, 4, None, "مراجعة مجلس الإدارة", "مبدئي"),
    ("EVT-07", "التغطية الإعلامية الفعلية", "عدد المواد المنشورة (لا المدفوعة)", "عدّ من سجل التغطية", "سجل التغطية", "PR", "13 ديسمبر 2026", 0, 6, None, "أرشيف + روابط", "مبدئي"),
    ("EVT-08", "تكلفة الحضور", "تكلفة الحفل ÷ الحضور الفعلي", "= التكلفة الفعلية ÷ EVT-03", "المحاسبة + RSVP", "FIN", "20 نوفمبر 2026", 0, 0, None, "مطابقة الفاتورة", "يُحسب بعد التنفيذ"),
]
EXE = [
    ("EXE-01", "نسبة إنجاز الخطة التنفيذية", "المهام المنفذة ÷ المجدولة", "(منجزة ÷ مجدولة) × 100", "قائمة تحقق التنفيذ", "PM", "أسبوعيًا", 0, 85, None, "مراجعة القائمة", "مبدئي"),
    ("EXE-02", "انحراف الميزانية", "الفرق بين المعتمد والفعلي", "((المعتمد − الفعلي) ÷ المعتمد) × 100", "المحاسبة", "FIN", "20 نوفمبر 2026", 0, 10, None, "مطابقة الفواتير", "مبدئي"),
    ("EXE-03", "المخاطر الحرجة المتبقية", "عدد مخاطر عالية الأثر غير المعالجة", "عدّ", "سجل المخاطر", "PM", "أسبوعيًا", 15, 3, None, "مراجعة السجل", "مبدئي"),
]
COM = [
    ("COM-01", "الاستفسارات الجديدة", "استفسارات مصدرها الحفل", "عدّ برمز المصدر", "نموذج اهتمام + CRM", "CRM", "شهريًا", 0, 40, None, "مطابقة رمز المصدر", "مبدئي"),
    ("COM-02", "الزيارات المدرسية", "زيارات ناتجة عن الحفل", "عدّ", "جدول المواعيد", "CRM", "شهريًا", 0, 12, None, "سجل المواعيد", "مبدئي"),
    ("COM-03", "طلبات التقديم", "طلبات تقديم جديدة", "عدّ", "نظام القبول", "مسؤول القبول", "كل سنة دراسية", 0, 20, None, "نظام القبول", "مبدئي"),
    ("COM-04", "التسجيلات المنسوبة", "تسجيلات مرتبطة بمصدر الحفل", "عدّ", "نظام القبول", "مسؤول القبول", "كل سنة دراسية", 0, 8, None, "رمز المصدر", "مبدئي"),
    ("COM-05", "تكلفة الاستفسار", "تكلفة الحملة ÷ الاستفسارات", "= التكلفة ÷ COM-01", "المحاسبة + CRM", "FIN", "شهريًا", 0, 0, None, "ربط-leaf مع لوحة المؤشرات", "يُحسب بعد التنفيذ"),
    ("COM-06", "تكلفة اكتساب الطالب", "تكلفة الحملة ÷ التسجيلات", "= التكلفة ÷ COM-04", "المحاسبة + القبول", "FIN", "كل سنة دراسية", 0, 0, None, "ربط مع لوحة المؤشرات", "يُحسب بعد التنفيذ"),
    ("COM-07", "معدل الاحتفاظ بالطلاب", "المجددون ÷ طلاب العام السابق", "× 100", "نظام القبول", "مدير المدرسة", "آخر كل عام دراسي", 0, 90, None, "نظام القبول", "مبدئي — خط الأساس يحتاج استخراج"),
    ("COM-08", "متوسط الإيراد لكل طالب", "إيراد الرسوم ÷ عدد الطلاب", "= IR ÷ N", "الحسابات", "FIN", "سنوي", 65000, 0, None, "القوائم المالية", "خط الأساس تقديري — يحتاج توثيق"),
    ("COM-09", "أثر=value على قيمة المدرسة", "لا يُقاس بالحفل — يُقاس ببيانات تشغيلية", "لا توجد معادلة من الحفل", "قوائم مالية + تشغيل", "الإدارة المالية", "سنوي", 300000000, 0, None, "تقييم مستقل", "قيمة استرشادية غير مُثمَّنة — لا يُعلن"),
]
EDU = [
    ("EDU-01", "رضا المشاركين (L1)", "متوسط استجابة استبيان 1–5", "متوسط الاستجابات", "استبيان", "CT", "نهاية كل وحدة", 0, 4.2, None, "استبيان مجهول", "مبدئي"),
    ("EDU-02", "إتقان المهارات المستهدفة (L2)", "نسبة الطلاب عند ≥ 80% في الـRubric", "(المتقنين ÷ الإجمالي) × 100", "Rubric المشروع", "المعلم + CT", "نهاية كل مرحلة", 0, 75, None, "Rubric موحّد + تقييم مزدوج", "مبدئي"),
    ("EDU-03", "نقل التعلم إلى الممارسة (L3)", "المعلمون الذين يطبّقون المشروع فعليًا", "(المطبّقون ÷ المدرَّبون) × 100", "ملاحظة صفية مقننة", "CT", "90 يومًا", 0, 60, None, "ملاحظة مقننة + عيّنة ≥ 20", "مبدئي"),
    ("EDU-04", "اكتمال ملف الإنجاز (L4)", "الملفات المكتملة ÷ الطلاب النشطين", "× 100", "منصة الملفات", "المعلم", "كل 6 أسابيع", 0, 80, None, "قوائم مراجعة", "مبدئي"),
    ("EDU-05", "تقدم الطالب في المشروع", "مجموع نقاط Rubric الرباعي من 100", "تصميم + بناء وبرمجة + توثيق + عمل جماعي", "Rubric", "المعلم", "كل 6 أسابيع", 0, 15, None, "تقييم مزدوج", "الهدف = زيادة سنوية +15"),
    ("EDU-06", "نسبة تسليم مشروع التخرج", "المشاريع المسلّمة ÷ طلاب G12", "× 100", "سجل المشاريع", "CT", "نهاية G12", 0, 85, None, "مراجعة المعرض", "مبدئي"),
]
kpi_sheet("KPI الحفل", "مؤشرات الحفل (EVT) والتنفيذ (EXE)",
          "إطار القياس: نموذج كيركباتريك الأربعة (Reaction → Learning → Behavior → Results) يُطبَّق علىCCE المستويات EDU. "
          "مصادر: Kirkpatrick Partners · HSE Evaluation Guide 2023. خط الأساس للاستفسارات والتسجيلات يحتاج استخراجًا من النظام قبل بدء القياس «بعد».", EVT + EXE)
kpi_sheet("KPI التجاري", "المؤشرات التجارية والاستثمارية (COM)",
          "قاعدة إلزامية: لا يُنسب أي تحسّن في قيمة المدرسة إلى الحفل. ما يُنسب هو مسار التحويل فقط "
          "(استفسار ← زيارة ← تقديم ← تسجيل) وبشروط التحقق الموضّحة.", COM)
kpi_sheet("KPI التعليمي", "المؤشرات التعليمية (EDU)",
          "الهدف من，范 المشروع تنمية مهارات قابلة للنقل لا ضمان وظيفة أو قبول جامعي. "
          "المستويات: L1 رضا · L2 إتقان · L3 نقل التعلّم (يُقاس عند 90 يومًا) · L4 أثر على ملف الإنجاز والنتائج.", EDU)

# ---------------------------------------------------------------- dashboard
ws = sheet("لوحة المؤشرات")
title_block(ws, "لوحة المؤشرات الحيّة — تُحدَّث من لوحة المفاتيح",
            "أدخل القيم الفعلية في الخلايا الصفراء، فتُحسب النسب تلقائيًا. مصدر الحقيقة الوحيد هو نظام التشغيل "
            "(سجل البوابة + CRM + نظام القبول) — لا تُكتب هنا أرقام تقديرية.", span=6)
head_row(ws, 4, ["المُدخل", "القيمة", "الوحدة", "المؤشر المحسوب", "القيمة المحسوبة", "ملاحظة"],
         [40, 16, 14, 40, 18, 44])
inputs = [
    ("الدعوات المرسلة", 0, "دعوة", None, None, "EVT-01"),
    ("الدعوات المؤكدة", 0, "دعوة", None, None, "EVT-02"),
    ("الحضور الفعلي", 0, "ضيف", None, None, "EVT-03"),
    ("الاستفسارات الجديدة (مصدرها الحفل)", 0, "استفسار", None, None, "COM-01"),
    ("الزيارات المدرسية", 0, "زيارة", None, None, "COM-02"),
    ("طلبات التقديم", 0, "طلب", None, None, "COM-03"),
    ("التسجيلات المنسوبة", 0, "تسجيل", None, None, "COM-04"),
    ("التكلفة الفعلية للحملة (ج.م)", 0, "ج.م", None, None, "EVT-08 / COM-05 / COM-06"),
    ("عدد المواد الإعلامية المنشورة", 0, "مادة", None, None, "EVT-07"),
    ("عدد فرص الشراكة المؤهلة", 0, "فرصة", None, None, "EVT-06"),
    ("عدد الاجتماعات التعاونية", 0, "اجتماع", None, None, "EVT-05"),
]
r = 5
for lbl, val, unit, _, _, memo in inputs:
    ws.cell(row=r, column=1, value=lbl).font = F_BOLD
    c = ws.cell(row=r, column=2, value=val); c.fill = INP; c.font = F_BOLD; c.alignment = AL_C
    c.number_format = MONEY if unit == "ج.م" else '#,##0'
    ws.cell(row=r, column=3, value=unit).font = F_BODY
    ws.cell(row=r, column=6, value=memo).font = F_SMALL
    for ci in range(1, 7):
        cc = ws.cell(row=r, column=ci); cc.border = BOX
        cc.alignment = AL_C if ci in (2, 3) else (AL_L if ci == 6 else AL_R)
    r += 1
calc = [
    ("نسبة تأكيد الحضور (EVT-02)", "=IF(B5=0,\"—\",ROUND(B6/B5*100,1))", "%", "محسوب تلقائيًا", "EVT-02"),
    ("نسبة الحضور من المؤكدين (EVT-04)", "=IF(B6=0,\"—\",ROUND(B7/B6*100,1))", "%", "محسوب تلقائيًا", "EVT-04"),
    ("تكلفة الحضور (EVT-08)", "=IF(B7=0,\"—\",ROUND(B12/B7,0))", "ج.م/ضيف", "التكلفة ÷ الحضور", "EVT-08"),
    ("تكلفة الاستفسار (COM-05)", "=IF(B8=0,\"—\",ROUND(B12/B8,0))", "ج.م/استفسار", "التكلفة ÷ الاستفسارات", "COM-05"),
    ("تكلفة اكتساب الطالب (COM-06)", "=IF(B11=0,\"—\",ROUND(B12/B11,0))", "ج.م/تسجيل", "التكلفة ÷ التسجيلات", "COM-06"),
    ("معدل تحويل الاستفسار إلى زيارة", "=IF(B8=0,\"—\",ROUND(B9/B8*100,1))", "%", "الزيارات ÷ الاستفسارات", "قمع التحويل"),
    ("معدل تحويل التسجيلات إلى طلبات تقديم", "=IF(B10=0,\"—\",ROUND(B11/B10*100,1))", "%", "التسجيلات ÷ الطلبات", "قمع التحويل"),
    ("كلفة المواد الإعلامية المنشورة", "=IF(B13=0,\"—\",ROUND(B12/B13,0))", "ج.م/مادة", "التكلفة ÷ المواد", "كفاءة التغطية"),
]
r += 1
ws.cell(row=r, column=1, value="المؤشرات المحسوبة").font = F_TITLE
r += 1
for lbl, formula, unit, memo, kpi in calc:
    ws.cell(row=r, column=1, value=lbl).font = F_BOLD
    c = ws.cell(row=r, column=2, value=formula); c.font = F_BOLD; c.fill = TOT; c.alignment = AL_C
    c.number_format = '#,##0.0'
    ws.cell(row=r, column=3, value=unit).font = F_BODY
    ws.cell(row=r, column=4, value=memo).font = F_BODY
    ws.cell(row=r, column=5, value=kpi).font = F_SMALL
    for ci in range(1, 7):
        cc = ws.cell(row=r, column=ci); cc.border = BOX
        cc.alignment = AL_C if ci in (2, 3, 5) else AL_R
    r += 1
note(ws, r + 1,
     "⚠ قاعدةMeasurement: كل قيمة تُدخل هنا يجب أن come من النظام (تسجيل البوابة، CRM، نظام القبول، المحاسبة). "
     "لا تُدخل أرقامًا تقديرية — الأرقام التقديرية تُفسد القياس. "
     "أعداد «قبل» تُقارن بخط الأساس المستخرج من 3 أشهر سابقة [يحتاج استخراج].", span=6)

# ---------------------------------------------------------------- readme
ws = sheet("دليل الاستخدام")
title_block(ws, "Green Grow Bot — دليل استخدام ملف الميزانية والمؤشرات",
            "الأحد 15 نوفمبر 2026 · فندق JW Marriott Hotel Cairo · مُدار ومدقق من منفذ الملف", span=2)
head_row(ws, 4, ["البند", "الشرح"], [38, 120])
guide = [
    ("مصدر الحقيقة", "هذا الملف مُشتق من Green_Grow_Bot_Canonical_Spec.md. أي تعديل جوهري يجب أن ينعكس في المرجع أولاً ثم هنا."),
    ("الأوراق", "الملخص (مقارنة السيناريوهات) · A/B/C (ميزانية كل سيناريو) · نموذج RFQ · تكلفة البرنامج · KPI الحفل · KPI التجاري · KPI التعليمي · لوحة المؤشرات · دليل الاستخدام."),
    ("الخلايا الصفراء", "حقول إدخال: عرض السعر الفعلي، التكلفة الفعلية، القيم الفعلية.Cells other من الحساب."),
    ("الأعمدة المحسوبة", "الفارق، إجمالي البنود، الاحتياطي، هامش عدم اليقين، السقف المعتمد، وجميع النسب في «لوحة المؤشرات». لا تُكتب فوقها."),
    ("تنبيه الميزانية", "كل الأرقام تقديرات تخطيط. بنود الفندق والضيافة والإنتاج الفني غير مسعّرة. لا يُعتمد أي إنفاق قبل وصول عروض أسعار مكتوبة."),
    ("تنبيه المؤشرات", "الأهداف «مبدئية» لم تتحقق بعد. خط الأساس يُستخرج قبل بدء القياس «بعد». يُفصل دائمًا بين التغطية التحريرية والتفاعل الرقمي والدعاية المدفوعة."),
    ("قاعدة النسبة", "لا يُنسب أي تحسّن في قيمة المدرسة إلى الحفل. ما يُنسب هو مسار التحويل فقط، وبشروط التحقق."),
    ("التحديث", "يُحدَّث الملف أسبوعيًا أثناء التحضير، ثم شهريًا خلال 90 يومًا بعد الإطلاق. كل تعديل يُوثَّق بتاريخه."),
    ("المصادر", "أسعار المكونات: electronicsegypt.com (محدّثة 28 أكتوبر 2026). سعات القاعة: موقع JW Marriott الرسمي. إطار القياس: Kirkpatrick Four Levels."),
    ("معلومات غير مؤكدة", "كل معلومة لم تُحقق تُكتب «يحتاج تأكيد» في النص لا في الخ_cells."),
]
r = 5
for k, v in guide:
    ws.cell(row=r, column=1, value=k).font = F_BOLD
    c = ws.cell(row=r, column=2, value=v); c.font = F_BODY; c.alignment = AL_R
    for ci in (1, 2):
        ws.cell(row=r, column=ci).border = BOX
        ws.cell(row=r, column=ci).fill = SUB if r % 2 else PatternFill()
    ws.row_dimensions[r].height = 34
    r += 1

del wb["Sheet"]
wb._sheets = [wb[n] for n in ["دليل الاستخدام", "الملخص", "A - اقتصادي", "B - متوسط احترافي",
                              "C - فاخر", "نموذج RFQ", "لوحة المؤشرات",
                              "KPI الحفل", "KPI التجاري", "KPI التعليمي",
                              "تكلفة البرنامج التعليمي"]]
path = os.path.join(OUT, "Green_Grow_Bot_Budget_and_KPIs.xlsx")
wb.save(path)
print("saved:", path)
print("sheets:", wb.sheetnames)
