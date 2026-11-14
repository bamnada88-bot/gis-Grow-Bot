# -*- coding: utf-8 -*-
"""Fifth pass: final targeted repairs (invisible-mark tolerant)."""
import io, os, re

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"

RULES = {
"Green_Grow_Bot_Event_Runbook.md": [
    (r"(?m)^> من ∂Mismatch.*$",
     "> من سؤال يقرأ ما تعلّمه طالب — على بعد √ من الواحد والستين — سيبدأ في مكان ما. "
     "**في نهاية المطاف، نلتقي في الصف.**"),
],
"Green_Grow_Bot_Educational_Model.md": [
    (r"│ إدارة مشروع│Inv\. │", "│ إدارة مشروع │ │"),
    (r"عدم توصيل المتحكم \|", "عدم توصيل المتحكم بمصدر خارجي |"),
    (r"\| للمعرض: حواجز", "| إدارة السلامة للمعرض: حواجز"),
    (r"المبادرة لا تعد مهنًا ولا جامعات\.",
     "المبادرة لا تَعِد بمهنة ولا بقبول جامعي."),
],
}

applied, missed = [], []
for fn, rules in RULES.items():
    path = os.path.join(PKG, fn)
    txt = io.open(path, encoding="utf-8").read()
    for rx, new in rules:
        txt, n = re.subn(rx, new, txt)
        if n:
            applied.append("%s :: %s (%d)" % (fn, rx[:60], n))
        else:
            missed.append("%s :: %s" % (fn, rx[:70]))
    io.open(path, "w", encoding="utf-8").write(txt)

log = ["APPLIED: %d" % len(applied), "NOT APPLIED (%d):" % len(missed)]
log += ["  - " + m for m in missed]
io.open(os.path.join(PKG, "qa_fix_log5.txt"), "w", encoding="utf-8").write("\n".join(log))
print("applied:", len(applied), "| missed:", len(missed))
