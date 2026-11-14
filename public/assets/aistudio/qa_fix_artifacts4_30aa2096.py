# -*- coding: utf-8 -*-
"""Final artifact repair pass — applies every remaining correction and strips residual
foreign scripts, logging every change."""
import io, os, re

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"

REPL = {
"Green_Grow_Bot_Canonical_Spec.md": [
    ("④ اعتماد قوائم والفريق", "④ اعتماد قوائم الضيافة والفريق"),
],
"Green_Grow_Bot_Master_Strategy.md": [
    ("ب Presented by تقديم الوثيقة، وبناءً على المرجع",
     "**تقديم الوثيقة (Presented by):** بناءً على المرجع"),
    ("في التقييم التعليمي؛  أن أغلب", "في التقييم التعليمي؛ المشكلة أن أغلب"),
    ("المحصلة: التصعيد لا ينفع مع 19 يومًا",
     "المحصلة: التصعيد لم يعد خيارًا واقعيًا مع 19 يومًا"),
    ("رؤية واضحة لتطور الطالب عبر السنين", "رؤية واضحة لتطور أبنائهم عبر السنين"),
    ("الشركاء: إمكانات تعاون — جهات التعليم", "الشركاء المحتملون: جهات التعليم"),
    ("مشتتة على أولياء الأمور (parent-borne) | موحّدة على مسار واحد (سيناريو مالي)",
     "مشتتة على المواد وأعباء أولياء الأمور (parent-borne) | موحّدة على مسار واحد وفق سيناريو مالي معتمد"),
    ("مرسلة، مؤكدة، ملغاة، متوقفة", "مرسلة، مؤكدة، ملغاة، وحالاتها"),
    ("الزيارات القادمة ونتائجها", "الزيارات المدرسية، ونتيجتها"),
    ("اعتماد قوائم الطعام والفريق", "اعتماد قوائم الضيافة والفريق"),
    ("بدء تتبّع الاستفسارات", "بدء متابعة الاستفسارات"),
    ("بمكان الحفل ويقيد المواعيد", "بالمكان ويقيد المواعيد"),
    ("وهذا قرار لا يستطيع خارجه. وهذا يستدعي —", "وهذا قرار لا يستطيع طرف خارجي اتخاذه —"),
],
"Green_Grow_Bot_Educational_Model.md": [
    ("عدم توصيل μC Villain زاвет", "عدم توصيل المتحكم بمصدر خارجي"),
    ("عدم توصيل μC Villain завет", "عدم توصيل المتحكم بمصدر خارجي"),
    ("عدم توصيل μC Villain", "عدم توصيل المتحكم"),
    ("إدارةالمشروع، عرض وت defenses", "إدارة المشروع، عرض وتوثيق"),
    ("إدارة 项目، عرض وت defenses", "إدارة المشروع، عرض وتوثيق"),
    ("إدارة المشروع، عرض وتوثيق", "إدارة المشروع، عرض وتوثيق"),
    ("إدارة  السلامة للمعرض", "إدارة السلامة للمعرض"),
    ("لا لحام بالطلاب وحدهم؛ طاولات", "لا لحام بالطلاب وحدهم؛ طاولات"),
    ("ويقارنه بالنيابة | التحكم؛ الزمن؛ الضغط والتدفق",
     "ويقارنه بالقيمة النظرية | التحكم؛ الزمن؛ الضغط والتدفق"),
    ("مبرر صريح يخاطب discard المبدأ", "مبرر صريح يخاطب المبدأ"),
    ("ومعمل الأ cience", "ومعمل العلوم"),
    ("لاحق.  Initiative يُقاس ويُنشر", "لاحق. نتيجة المبادرة تُقاس وتُنشر"),
    ("Initiative يُقاس ويُنشر", "المبادرة تُقاس وتُنشر"),
    ("ت twitching", "ت"),
],
"Green_Grow_Bot_Event_Runbook.md": [
    ("> من ∂Mismatch يقرأ ما تعلّمه طالب — على بعد √من الواحد والستين — سيبدأ في مكان ما. **f_team، نلتقي في الصف.**",
     "> من سؤال يقرأ ما تعلّمه طالب — على بعد √ من الواحد والستين — سيبدأ في مكان ما. "
     "**في نهاية المطاف، نلتقي في الصف.**"),
    ("بنى  شيئًا بيديه", "بنى شيئًا بيديه"),
],
"Green_Grow_Bot_PR_and_Media.md": [
    ("|  محدد | ✅ | حقيبة / مختبر / تدريب معلمين / شراكة |",
     "| نوع الاهتمام | ✅ | حقيبة / مختبر / تدريب معلمين / شراكة |"),
    ("### 6.1 القمع وم-map التحول", "### 6.1 القمع ومسار التحويل"),
],
"Green_Grow_Bot_Protocol_and_Invitations.md": [
    ("تأكيد الصفة제한ية", "تأكيد الصفة والشروط"),
    ("موعد 도착 للوصول موصى به", "موعد الوصول موصى به"),
    ("موعد 도착 موصى به", "موعد الوصول موصى به"),
    ("تصويري أنا خلالalisia proceedings", "تصويري أنا خلال"),
],
"Green_Grow_Bot_Speaker_Script.md": [
    ("مؤشر ضوئي:if أضاف دارة بسيطة", "مؤشر ضوئي: يضيف دارة بسيطة"),
    ("أودّ أن أقول لكم شيئًا واحدًا عن هذه المساء:", "أودّ أن أقول لكم شيئًا واحدًا عن هذه الأمسية:"),
    ("> وهذه المساء، كثير Streambadges —", "> وهذه المساء، ومشاريع كثيرة ومتنوعة —"),
    ("خطوة أولى في  ودعم تطبيقي؛ من reclamation ارس — تبادل الخبرة.",
     "خطوة أولى في تبنّي الأدوات ودعم تطبيقي؛ ومن مدارس أخرى — تبادل الخبرة."),
    ("الاستخدام covered من موارد المدرسة", "الاستخدام مغطى من موارد المدرسة"),
],
}

# --------------------------------------------------------------- generic cleanup
STRIP_BLOCKS = [
    (re.compile("[\uac00-\ud7af]+"), ""),          # Hangul
    (re.compile("[\u3040-\u30ff]+"), ""),          # Kana
    (re.compile("[\u4e00-\u9fff]+"), ""),          # Han
    (re.compile("[\u0400-\u04ff]+"), ""),          # Cyrillic
    (re.compile("[\u0370-\u03ff]+"), ""),          # Greek
]

applied, missed = [], []
for fn, pairs in REPL.items():
    path = os.path.join(PKG, fn)
    txt = io.open(path, encoding="utf-8").read()
    for old, new in pairs:
        if old in txt:
            txt = txt.replace(old, new)
            applied.append("%s :: %s" % (fn, old[:62]))
        else:
            missed.append("%s :: %s" % (fn, old[:62]))
    io.open(path, "w", encoding="utf-8").write(txt)

# strip residual foreign scripts everywhere, logging each removal
strip_log = []
for fn in sorted(os.listdir(PKG)):
    if not fn.endswith(".md"):
        continue
    path = os.path.join(PKG, fn)
    txt = io.open(path, encoding="utf-8").read()
    orig = txt
    for rx, _ in STRIP_BLOCKS:
        txt = rx.sub(lambda m: "", txt)
    if txt != orig:
        # show a compact diff hint: lines that changed
        for a, b in zip(orig.split("\n"), txt.split("\n")):
            if a != b:
                strip_log.append("%s :: %s  ==>  %s" % (fn, a.strip()[:160], b.strip()[:160]))
        io.open(path, "w", encoding="utf-8").write(txt)

log = ["APPLIED: %d" % len(applied), "NOT APPLIED (%d):" % len(missed)]
log += ["  - " + m for m in missed]
log += ["", "SCRIPT-STRIP CHANGED LINES (%d):" % len(strip_log)]
log += ["  - " + s for s in strip_log]
io.open(os.path.join(PKG, "qa_fix_log4.txt"), "w", encoding="utf-8").write("\n".join(log))
print("applied:", len(applied), "| missed:", len(missed), "| stripped lines:", len(strip_log))
