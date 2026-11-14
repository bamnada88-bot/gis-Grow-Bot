# -*- coding: utf-8 -*-
"""Repair the two cells in Canonical Spec §0 that carry mixed-script corruption."""
import io, os, re

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
path = os.path.join(PKG, "Green_Grow_Bot_Canonical_Spec.md")

lines = io.open(path, encoding="utf-8").read().split("\n")
for i, ln in enumerate(lines):
    if "axmind" in ln.lower() or "شعار axmind" in ln:
        lines[i] = "| شعار AXMIND في المواد | `[يحتاج تأكيد]` | تثبيت الصفة ومواضع الشعار | PR |"
        print("fixed logo row at L%d" % (i + 1))
    elif "لم تُجمع" in ln:
        lines[i] = "| موافقات التصوير | لم تُجمع | إرسال نموذج الموافقة | PR + LOG |"
        print("fixed consent row at L%d" % (i + 1))
io.open(path, "w", encoding="utf-8").write("\n".join(lines))
