# -*- coding: utf-8 -*-
"""Third (final) artifact cleanup pass — regex-based, whitespace-tolerant."""
import io, os, re

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"

RULES = {
"Green_Grow_Bot_Canonical_Spec.md": [
    (r"\|\s*\.provider\s*\+\s*مستثمر\s*\|", "| تمويل + مستثمر |"),
    (r"أتعاب\s+muitos\s+الملحق", "أتعاب الملحق"),
    (r"جهات حكومية مهارات \(TIEC", "جهات حكومية وشريكة (TIEC"),
],
"Green_Grow_Bot_Educational_Model.md": [
    (r"مبرر صريح يخاطب\s+discard\s+المبدأ", "مبرر صريح يخاطب المبدأ"),
    (r"\|\s*والمسؤولية\s*\|\s*«المنهج يقول", "| المنهج والمسؤولية | «المنهج يقول"),
    (r"ومعمل\s*الأ\s*cience", "ومعمل العلوم"),
    (r"لا يُفكّ تحت\s*[^\s،؛.]+", "لا يُفكّ تحت إشراف المعلم"),
    (r"ومعمل\s*الأ\s*-science", "ومعمل العلوم"),
],
"Green_Grow_Bot_Event_Runbook.md": [
    (r"يتحركون بعد 60–75 دقيقة\.\s*الطويلة تُهدر المورد الأدق",
     "يتحركون بعد 60–75 دقيقة. هذا الطول يُهدر المورد الأدق"),
    (r"TIEC، وزارة الشباب والرياضة،\s*جهات تطوير المهارات\s*independentemente",
     "TIEC، وزارة الشباب والرياضة، جهات تطوير المهارات"),
    (r"> من ∂Mismatch يقرأ[^\n]*?\*\*f_team، نلتقي في الصف\.\*\*",
     "> من سؤال يقرأ ما تعلّمه طالب — على بعد √ من الواحد والستين — سيبدأ في مكان ما. "
     "**في نهاية المطاف، نلتقي في الصف.**"),
],
"Green_Grow_Bot_Master_Strategy.md": [
    (r"Rubric \+ مراجعة-gallery", "Rubric + مراجعة الأقران"),
],
"Green_Grow_Bot_PR_and_Media.md": [
    (r"### 6\.1 القلع[^\n]*التحول", "### 6.1 القمع ومسار التحويل"),
    (r"### 6\.1 القمع[^\n]*التحول", "### 6.1 القمع ومسار التحويل"),
],
"Green_Grow_Bot_Speaker_Script.md": [
    (r"> وهذه المساء،[^\n]*?\*\*نحن نبدأ بوعد واحد",
     "> وهذه المساء، ومشاريع كثيرة ومتنوعة — **نحن نبدأ بوعد واحد"),
    (r"خطوة أولى في\s*ودعم تطبيقي؛[^\n]*?تبادل الخبرة\.",
     "خطوة أولى في تبنّي الأدوات ودعم تطبيقي؛ ومن مدارس أخرى — تبادل الخبرة."),
    (r"للاستخدام\s+covered\s+من موارد المدرسة", "للاستخدام مغطى من موارد المدرسة"),
    (r"الاستخدام\s+covered\s+من موارد المدرسة", "الاستخدام مغطى من موارد المدرسة"),
],
}

applied, missed = [], []
for fn, rules in RULES.items():
    path = os.path.join(PKG, fn)
    txt = io.open(path, encoding="utf-8").read()
    for rx, new in rules:
        txt, n = re.subn(rx, new, txt)
        if n:
            applied.append("%s :: %s (%d)" % (fn, rx[:55], n))
        else:
            missed.append("%s :: %s" % (fn, rx[:65]))
    io.open(path, "w", encoding="utf-8").write(txt)

# Global: strip any residual Hangul / Cyrillic / CJK blocks and log them
STRAY = re.compile("[\u3000-\u303f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff"
                   "\uff00-\uffef\u0400-\u04ff\uac00-\ud7af]")
residual = []
for fn in RULES:
    path = os.path.join(PKG, fn)
    txt = io.open(path, encoding="utf-8").read()
    for m in STRAY.finditer(txt):
        residual.append("%s :: %r" % (fn, m.group(0)))
    if residual:
        txt = STRAY.sub("", txt)
        io.open(path, "w", encoding="utf-8").write(txt)

log = ["APPLIED: %d" % len(applied), "NOT APPLIED (%d):" % len(missed)]
log += ["  - " + m for m in missed]
log += ["", "RESIDUAL STRAY SCRIPTS STRIPPED: %d" % len(residual)]
log += ["  - " + r for r in residual]
io.open(os.path.join(PKG, "qa_fix_log3.txt"), "w", encoding="utf-8").write("\n".join(log))
print("applied:", len(applied), "| missed:", len(missed), "| stray stripped:", len(residual))
