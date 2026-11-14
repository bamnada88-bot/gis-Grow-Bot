# -*- coding: utf-8 -*-
"""Green Grow Bot — Risk Register workbook (openpyxl)."""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule
from openpyxl.worksheet.datavalidation import DataValidation

OUT = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
NAVY = "0B1B3D"; GOLD = "D4AF37"; SUB = PatternFill("solid", fgColor="E8ECF5")
TOT = PatternFill("solid", fgColor="F3E9CF"); INP = PatternFill("solid", fgColor="FFF9E3")
GREEN = "C6EFCE"; AMBER = "FFEB9C"; RED = "FFC7CE"; GREY = "F2F2F2"
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

wb = Workbook()


def sheet(t):
    ws = wb.create_sheet(t)
    ws.sheet_view.rightToLeft = True
    ws.sheet_view.showGridLines = False
    return ws


def head_row(ws, row, headers, widths):
    for i, (h, w) in enumerate(zip(headers, widths), start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = F_HDR; c.fill = PatternFill("solid", fgColor=NAVY); c.border = BOX; c.alignment = AL_C
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 36


def title_block(ws, t, s, span):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=span)
    c = ws.cell(row=1, column=1, value=t); c.font = F_TITLE; c.alignment = AL_R
    ws.row_dimensions[1].height = 26
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=span)
    c = ws.cell(row=2, column=1, value=s); c.font = F_SMALL; c.alignment = AL_R
    ws.row_dimensions[2].height = 32


def note(ws, row, text, span):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=span)
    c = ws.cell(row=row, column=1, value=text); c.font = F_SMALL; c.alignment = AL_R
    ws.row_dimensions[row].height = 30


RISKS = [
    ("RSK-01", "عدم تأكيد الشخصيات المهمة", 4, 5, "دعوات مبكرة (3 نوفمبر) + سلم تصعيد + متابعة يومية + تحويل الفئة إلى «مشارك» لا «ضيف»", "تفعيل海报 الفرقة: فتح جلسة حوار专场 بدل الجلسة العامة؛ إصدار بيان بديل دونVegetal أسماء", "PRO", "عدم الرد خلال 5 أيام من الإرسال", "مفتوح", 2),
    ("RSK-02", "عدم تأكيد حجز الفندق والقاعة", 4, 5, "إرسال RFQ فورًا (29 أكتوبر) + احتياطي: Marriott Mena House / Cairo Marriott —信息披露 تخطيطي فقط", "تأكيد كتابي من الفندق؛ إن لم يصل: الانتقال إلى السيناريو الأقل أو فندق بديل بموافقة PM", "PM + LOG", "لا تأكيد كتابي حتى 3 نوفمبر 2026", "مفتوح", 2),
    ("RSK-03", "تأخر الطباعة", 3, 3, "تسليم المطبعة 3 نوفمبر + PDF رقمي جاهز + معاينة 13 نوفمبر", "تحويل فوري إلى النسخة الرقمية + تصغير الكمية + إرسال الدعوة عبر الواتساب", "LOG", "لا معاينة مطبوعة حتى 9 نوفمبر", "مفتوح", 1),
    ("RSK-04", "ضعف الحضور", 3, 4, "ثلاث موجات دعوة + متابعة فردية + فتح التسجيل مبكرًا + ضيافة/نماذج هامة", "التحويل إلى «حلقة مغلقة» + خفض التكاليف + تأجيل التوسّع في المرحلة الثانية", "PRO", "نسبة التأكيد < 30% في 6 نوفمبر 2026", "مفتوح", 3),
    ("RSK-05", "تعطل الروبوت أثناء العرض", 3, 4, "نسخة احتياطية جاهزة + بروفة 13 نوفمبر + خطة بديلة مصوّرة 90 ثانية + حقوق تعليمية السلامة", "تشغيل الفيديو المسجّل ثم متابعة المعلم بالشرح النظري؛ العبارة المعتمدة: «شكرًا لصبركم — لدينا نسخة جاهزة»", "DEMO", "فشل في اختبار 13 نوفمبر 2026", "مفتوح", 2),
    ("RSK-06", "عطل الصوت أو الشاشة", 2, 4, "ملف عرض على لابتوب + USB + كابلات احتياطية + باور UPS + بِث احتياطي", "تشغيل من جهاز مستقل + ميكروفون يدوي + استمرار الفقرة بصوت المذيع", "TEC", "—", "مفتوح", 1),
    ("RSK-07", "تجاوز الميزانية", 3, 4, "سقف معتمد + موافقة مسبقة على أي بند + احتياطي 8–10% + مراجعة أسبوعية", "وقف البنود الاختيارية (لا «تعذّر استبعادها») + تحويل من الاحتياطي بموافقة PM", "FIN", "انحراف ≥ 5% في 10 نوفمبر 2026", "مفتوح", 2),
    ("RSK-08", "عدم وجود موافقات التصوير", 3, 4, "نموذج موافقة + جمع 100% قبل 7 نوفمبر + قائمة الأسماء المسموح بتصويرهم + لافتة قاعة", "منع التصوير + لافتة «بدون تصوير» + تغطية بديلة بالرسوم والعرض التقديمي", "PR", "موافقات < 60% في 10 نوفمبر 2026", "مفتوح", 2),
    ("RSK-09", "استخدام اسم أو شعار جهة دون إذن", 2, 4, "قاعدة «بلا موافقة مكتوبة = بلا شعار» + مراجعة كل مادة قبل النشر + قائمة الشعارات المسموحة", "تصحيح فوري خلال 24 ساعة + تنويه + سحب المادة", "PM + PR", "أي طلبUses شعار غير موثّق", "مفتوح", 1),
    ("RSK-10", "ضعف التغطية الإعلامية", 3, 3, "قائمة وسائل A (8 جهات) + pitch مبكر + حقيبة صحفيين + عرض حي قابل للتصوير", "تكثيف التغطية الرقمية الرسمية + توثيق الحفل بمحتوى أصلي + تأجيل التغطية كـ«نشر» لا «تغطية»", "PR", "أقل من 3 تأكيدات إعلامية في 7 نوفمبر 2026", "مفتوح", 2),
    ("RSK-11", "المبالغة في الوعود", 3, 4, "مراجعة نصية إلزامية لكل مادة + قائمة عبارات ممنوعة + تدريب المذيع والمتحدثين + формуلة معتمدة", "تصحيح علني + مراجعة الخطاب + مراجعة كل مادة لاحقة", "CT + PR", "أي ادعاء غير مسند في مسودة", "مفتوح", 2),
    ("RSK-12", "اعتراض أولياء الأمور", 2, 3, "جلسة تعريف مسبقة + FAQ واضح + رسالة أولياء أمور بلغة بسيطة +不开 «ضمان وظائف»", "جلسة استيضاح خلال 48 ساعة + رد موثّق + مراجعة البرنامج التعليمي", "مدير المدرسة", "استفساران سالبان أو أكثر", "مفتوح", 2),
    ("RSK-13", "مخاطر السلامة في العروض العملية", 2, 4, "تقييم مخاطر مكتوب + حواجز + مشرف سلامة + فحص البطاريات + لا dzieci في العرض", "إيقاف العرض فورًا + عرض مصوّر + إبلاغ + توثيق الحادثة", "SAFE", "—", "مفتوح", 1),
    ("RSK-14", "نشر معلومات غير دقيقة", 3, 3, "مصدر الحقيقة الوحيد = الملف المرجعي + مراجعة قبل النشر + تصحيح خلال 24 ساعة", "تصحيح في 24 ساعة + تحديث الملف المرجعي + مراجعة المخزون", "PR + PM", "—", "مفتوح", 2),
    ("RSK-15", "الاعتماد على حدث واحد دون متابعة", 4, 5, "خطة 90 يومًا مرتبطة بالمبادرة + بوابات انتقال + مسؤوليات محددة + KPIs مرتبطة", "تحويل الحفل إلى مسار عمل + تشغيل المرحلة التجريبية + أول تقرير قياس", "مدير المدرسة + PM", "لا خطة معتمدة حتى 20 نوفمبر 2026", "مفتوح", 2),
]

ws = sheet("سجل المخاطر")
title_block(ws, "Green Grow Bot — سجل المخاطر والمسؤوليات",
            "الأحد 15 نوفمبر 2026. المقياس: الاحتمال × الأثر (1–5). الدرجة ≥ 15 = حرجة · 8–14 = مرتفعة · 4–7 = متوسطة · ≤ 3 = منخفضة. "
            "أعمدة التقييم المتبقّي تُملأ أسبوعيًا في المراجعة.", span=13)
head_row(ws, 4,
         ["ID", "الخطر", "الاحتمال (1–5)", "الأثر (1–5)", "الدرجة", "التصنيف", "الوقاية",
          "الاستجابة", "المسؤول", "مؤشر الإنذار المبكر", "الحالة", "الاحتمال المتبقي", "الدرجة المتبقية"],
         [9, 34, 13, 12, 11, 13, 46, 46, 14, 28, 12, 13, 14])
r = 5
for rid, name, p, i, prev, resp, own, warn, status, resid in RISKS:
    vals = [rid, name, p, i, f"=C{r}*D{r}", None, prev, resp, own, warn, status, resid, f"=L{r}*D{r}"]
    for ci, v in enumerate(vals, start=1):
        c = ws.cell(row=r, column=ci, value=v); c.border = BOX; c.font = F_BODY
        c.alignment = AL_C if ci in (1, 3, 4, 5, 6, 9, 11, 12, 13) else AL_R
        if ci in (3, 4, 12):
            c.fill = INP if ci == 12 else SUB
    ws.cell(row=r, column=6, value=f'=IF(E{r}>=15,"حرجة",IF(E{r}>=8,"مرتفعة",IF(E{r}>=4,"متوسطة","منخفضة")))')
    ws.cell(row=r, column=6).font = F_BOLD; ws.cell(row=r, column=6).alignment = AL_C; ws.cell(row=r, column=6).border = BOX
    ws.row_dimensions[r].height = 58
    r += 1
last = r - 1
ws.conditional_formatting.add(f"E5:E{last}", CellIsRule(operator="greaterThanOrEqual", formula=["15"], fill=PatternFill("solid", fgColor=RED)))
ws.conditional_formatting.add(f"E5:E{last}", CellIsRule(operator="between", formula=["8", "14"], fill=PatternFill("solid", fgColor=AMBER)))
ws.conditional_formatting.add(f"E5:E{last}", CellIsRule(operator="lessThanOrEqual", formula=["3"], fill=PatternFill("solid", fgColor=GREEN)))
ws.conditional_formatting.add(f"F5:F{last}", CellIsRule(operator="equal", formula=['"حرجة"'], fill=PatternFill("solid", fgColor=RED)))
ws.conditional_formatting.add(f"F5:F{last}", CellIsRule(operator="equal", formula=['"مرتفعة"'], fill=PatternFill("solid", fgColor=AMBER)))
ws.conditional_formatting.add(f"F5:F{last}", CellIsRule(operator="equal", formula=['"منخفضة"'], fill=PatternFill("solid", fgColor=GREEN)))
dv = DataValidation(type="list", formula1='"مفتوح,قيد المعالجة,مغلق,تصعيد"', allow_blank=True)
ws.add_data_validation(dv); dv.add(f"K5:K{last}")
dv2 = DataValidation(type="list", formula1='"1,2,3,4,5"', allow_blank=True)
ws.add_data_validation(dv2); dv2.add(f"C5:D{last}"); dv2.add(f"L5:L{last}")
note(ws, last + 2,
     "مبدأ تصميمي حاكم: قيمة الحفل يجب أن تبقى قائمة حتى لو غاب مسؤول كبير أو لم تحضر وسيلة إعلام. "
     "البرنامج مبني على جودة المبادرة والعرض العملي لا على أسماء الضيوف.", span=13)
note(ws, last + 3,
     "مراجعة السجل: أسبوعيًا مع PM · قبل كل بوابة قرار · في 13 نوفمبر (تجميد) · في 20 نوفمبر (إغلاق التحضير) · شهريًا خلال 90 يومًا بعد الإطلاق. "
     "كل تغيّر في الاحتمال أو الأثر يُوثّق بتاريخه وسببه.", span=13)
ws.freeze_panes = "C5"

# ------------------------------------------------------------------ matrix
ws = sheet("مصفوفة الاحتمال والأثر")
title_block(ws, "مصفوفة الاحتمال × الأثر", "الأرقام = عدد المخاطر في كل خلية (محسوبة تلقائيًا من «سجل المخاطر»).", span=7)
ws.cell(row=4, column=1, value="الأثر ← / الاحتمال ↓").font = F_BOLD
for j in range(1, 6):
    c = ws.cell(row=4, column=2 + j, value=j); c.font = F_HDR
    c.fill = PatternFill("solid", fgColor=NAVY); c.alignment = AL_C; c.border = BOX
    ws.column_dimensions[get_column_letter(2 + j)].width = 12
ws.column_dimensions["A"].width = 22
for i in range(1, 6):
    c = ws.cell(row=4 + i, column=1, value=i); c.font = F_HDR
    c.fill = PatternFill("solid", fgColor=NAVY); c.alignment = AL_C; c.border = BOX
    for j in range(1, 6):
        f = f"=COUNTIFS('سجل المخاطر'!$C$5:$C$19,{i},'سجل المخاطر'!$D$5:$D$19,{j})"
        cc = ws.cell(row=4 + i, column=2 + j, value=f); cc.alignment = AL_C; cc.border = BOX
        cc.font = F_BOLD
ws.conditional_formatting.add("B6:F10", CellIsRule(operator="greaterThanOrEqual", formula=["1"], fill=PatternFill("solid", fgColor=AMBER)))
note(ws, 12,
     "قراءة المصفوفة: الخلية (احتمال 4–5، أثر 4–5) = نطاق «السماح George» — أي خطر يقع هنا يستوجب تدخلًا فوريًا من PM "
     "ولا يُنتظر أسبوعيًا.шла Risk Register يحتوي 15 خطرًا مصنّفًا مسبقًا (الأعمدة C وD).", span=7)

# ------------------------------------------------------------------ actions
ws = sheet("خطة الإجراءات")
title_block(ws, "خطة الإجراءات — إجراءات الوقاية والاستجابة لكل خطر",
            "كل إجراء له مالك وموعد ودليل إنجاز. الإجراءات الوقائية تُنفَّذ قبل تاريخ الحدث؛ إجراءات الاستجابة تبقى جاهزة.", span=7)
head_row(ws, 4, ["ID", "الإجراء", "النوع", "المالك", "الموعد النهائي", "دليل الإنجاز", "الحالة"],
         [9, 60, 16, 14, 20, 34, 16])
ACTIONS = [
    ("RSK-01", "إرسال موجة الدعوة الأولى للفئة A والتحقق من الأسماء قبل الإرسال", "وقاية", "PRO", "4 نوفمبر 2026", "سجل إرسال + بطاقات تحقق"),
    ("RSK-01", "سلم التصعيد + إيقاف بعد 14 يومًا", "وقاية", "PRO", "13 نوفمبر 2026", "سجل المتابعة"),
    ("RSK-02", "إرسال RFQ للفندق واستلام عرض سعر مكتوب", "وقاية", "LOG + FIN", "29 أكتوبر 2026", "خطاب عرض السعر"),
    ("RSK-02", "تجهيز خطة بديلة بفنادق بديلة (Mena House / Cairo Marriott)", "وقاية", "PM", "1 نوفمبر 2026", "ملاح��ة الخطة البديلة"),
    ("RSK-03", "تسليم ملفات الطباعة للمطبعة مع ملاحظات التجليد", "وقاية", "LOG", "3 نوفمبر 2026", "إيصال الاستلام"),
    ("RSK-03", "معاينة الطباعة قبل التجليد", "وقاية", "LOG + PM", "13 نوفمبر 2026", "محضر معاينة"),
    ("RSK-04", "متابعة يومية للاستفسارات ومتابعة غير المؤكدين", "وقاية", "PRO", "9–13 نوفمبر 2026", "سجل الدعوات"),
    ("RSK-04", "تفعيل تحويل الفئة C إلى مشاركين", "استجابة", "PM", "13 نوفمبر 2026", "قائمة المعدّلين"),
    ("RSK-05", "بروفة العرض + تشغيل النسخة الاحتياطية فعليًا", "وقاية", "DEMO", "13 نوفمبر 2026", "تقرير البروفة"),
    ("RSK-05", "تسجيل الفيديو الاحتياطي 90 ثانية واعتماده", "وقاية", "DEMO + PR", "13 نوفمبر 2026", "ملف الفيديو"),
    ("RSK-06", "تجهيز الملف على جهاز مستقل + USB + كابلات احتياطية", "وقاية", "TEC", "14 نوفمبر 2026", "تقرير الاختبار"),
    ("RSK-07", "تجميد الميزانية واعتماد السقف", "وقاية", "FIN + PM", "14 نوفمبر 2026", "قرار التجميد"),
    ("RSK-07", "مراجعة انحراف أسبوعية", "وقاية", "FIN", "أسبوعيًا", "لوحة الميزانية"),
    ("RSK-08", "جمع موافقات التصوير (أولياء الأمور والمعلمون)", "وقاية", "PR", "7 نوفمبر 2026", "قائمة الموافقين"),
    ("RSK-08", "تجهيز لافتة «بدون تصوير» + منطقة تصوير معزولة", "وقاية", "PR + SAFE", "14 نوفمبر 2026", "صور اللافتة"),
    ("RSK-09", "مراجعة كل مادة قبل النشر مقابل قائمة الشعارات المسموحة", "وقاية", "PR + PM", "مستمر", "قائمة المراجعة"),
    ("RSK-10", "إرسال pitch مبكر لـ 8 وسائل من الفئة A", "وقاية", "PR", "10 نوفمبر 2026", "سجل الإرسال"),
    ("RSK-11", "اعتماد قائمة العبارات الممنوعة وتدريب المتحدثين", "وقاية", "CT + PR", "8 نوفمبر 2026", "محضر التدريب"),
    ("RSK-12", "إرسال رسالة أولياء الأمور + FAQ", "وقاية", "CRM", "10 نوفمبر 2026", "قائمة الإرسال"),
    ("RSK-13", "تقييم مخاطر المختبر + فحص البطاريات + خطة إخلاء", "وقاية", "SAFE", "14 نوفمبر 2026", "محضر الفحص"),
    ("RSK-14", "تثبيت الملف المرجعي كمرجع وحيد للمحتوى", "وقاية", "PM", "30 أكتوبر 2026", "النسخة 1.0 المعتمدة"),
    ("RSK-15", "اعتماد خارطة 90 يومًا وربط المراحل ببوابات", "وقاية", "PM", "20 نوفمبر 2026", "الخارطة المعتمدة"),
    ("RSK-15", "تقرير أسبوعي حتى يوم 90 مع تحديث المؤشرات", "وقاية", "PM", "أسبوعيًا", "التقارير الأسبوعية"),
]
r = 5
for a in ACTIONS:
    for ci, v in enumerate(a, start=1):
        c = ws.cell(row=r, column=ci, value=v); c.border = BOX; c.font = F_BODY
        c.alignment = AL_C if ci in (1, 3, 4, 5, 7) else AL_R
        if ci == 7: c.fill = INP
    ws.row_dimensions[r].height = 26
    r += 1
STATES_AR = "لم يبدأ,جاري,منجز,متعثر"
dv3 = DataValidation(type="list", formula1=chr(34) + STATES_AR + chr(34), allow_blank=True)
ws.add_data_validation(dv3); dv3.add(f"G5:G{r-1}")
ws.freeze_panes = "A5"

# ------------------------------------------------------------------ review log
ws = sheet("سجل المراجعة")
title_block(ws, "سجل مراجعة المخاطر (يُملأ أسبوعيًا)", "توثيق كل تغيّر في الاحتمال أو الأثر مع السبب والتاريخ — لا تُعدَّل القيم دون أثر مراجعة.", span=6)
head_row(ws, 4, ["التاريخ", "ID المخاطَر", "ما الذي تغيّر", "الاحتمال قبل/بعد", "الأثر قبل/بعد", "الإجراء المتخذ"],
         [18, 14, 44, 20, 20, 54])
r = 5
for i in range(12):
    for ci in range(1, 7):
        c = ws.cell(row=r, column=ci, value=None); c.border = BOX; c.fill = INP
    ws.row_dimensions[r].height = 26
    r += 1
note(ws, r + 1, "تُراجع المخاطر في: 30 أكتوبر · 7 نوفمبر · 13 نوفمبر (تجميد) · 20 نوفمبر · ثم أسبوعيًا خلال الـ90 يومًا.", span=6)

# ------------------------------------------------------------------ readme
ws = sheet("دليل الاستخدام")
title_block(ws, "دليل استخدام سجل المخاطر", "الأحد 15 نوفمبر 2026 · فندق JW Marriott Hotel Cairo · 15 خطرًا مصنّفًا مسبقًا.", span=2)
head_row(ws, 4, ["البند", "الشرح"], [38, 120])
guide = [
    ("الأوراق", "سجل المخاطر (15 خطرًا مع الوقاية والاستجابة والمؤشر المبكر) · مصفوفة الاحتمال والأثر (محسوبة) · خطة الإجراءات (27 إجراءً) · سجل المراجعة · دليل الاستخدام."),
    ("منطق الدرجة", "الدرجة = الاحتمال × الأثر. ≥15 حرجة (تدخل فوري) · 8–14 مرتفعة (متابعة أسبوعية) · 4–7 متوسطة · ≤3 منخفضة."),
    ("التصنيف التلقائي", "عمود «التصنيف» محسوب بصيغة. لا يُكتب فوقه."),
    ("التقييم المتبقي", "عمود «الاحتمال المتبقي» (أصفر) يُحدَّث بعد تنفيذ الوقاية، و«الدرجة المتبقية» تُحسب تلقائيًا. الهدف: خفض كل خطر حرج إلى ≤ 8 قبل 14 نوفمبر."),
    ("مؤشر الإنذار المبكر", "العمود J — هو ما يجعل المراجعة الأسبوعية ذات معنى: إن تحرك المؤشر، تُفعَّل الاستجابة قبل وقوع الضرر."),
    ("من يملك القرار", "PM يجمّع المراجعة الأسبوعية. تغيير أي مخاطرة إلى «تصعيد» يستلزم قرارًا موثّقًا."),
    ("علاقة بالمؤشرات", "EXE-03 (المخاطر الحرجة المتبقية ≤ 3) و RSK-15 هما risks الرئيسية على استمرارية самого المشروع بعد الحفل."),
    ("مبدأ التصميم", "قيمة الحفل تبقى قائمة حتى لو غاب مسؤول كبير أو لم تحضر وسيلة إعلام."),
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
wb._sheets = [wb[n] for n in ["دليل الاستخدام", "سجل المخاطر", "مصفوفة الاحتمال والأثر", "خطة الإجراءات", "سجل المراجعة"]]
path = os.path.join(OUT, "Green_Grow_Bot_Risk_Register.xlsx")
wb.save(path)
print("saved:", path)
