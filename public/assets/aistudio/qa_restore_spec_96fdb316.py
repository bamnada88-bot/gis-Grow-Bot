# -*- coding: utf-8 -*-
"""Restore the lines accidentally overwritten in the canonical spec from the
reconstructed original transcript copy."""
import io, os

PKG = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package"
CUR = os.path.join(PKG, "Green_Grow_Bot_Canonical_Spec.md")
ORIG = os.path.join(PKG, "qa_spec_original_full.md")

BAD = "| شعار AXMIND في المواد | `[يح needs تأكيد]` | تثبيت الصفة ومواضع الشعار | PR |"
BAD = "| شعار AXMIND في المواد | `[يحتاج تأكيد]` | تثبيت الصفة ومواضع الشعار | PR |"
OFFSET = 20

cur = io.open(CUR, encoding="utf-8").read().split("\n")
orig = io.open(ORIG, encoding="utf-8").read().split("\n")

fixed = []
for i, ln in enumerate(cur):
    if ln.strip() == BAD.strip():
        j = i - OFFSET
        if 0 <= j < len(orig) and orig[j].strip() and orig[j].strip() != BAD.strip():
            cur[i] = orig[j]
            fixed.append((i + 1, orig[j][:90]))
        else:
            print("NO MATCH for current line", i + 1)

io.open(CUR, "w", encoding="utf-8").write("\n".join(cur))
print("restored lines:", len(fixed))
for n, t in fixed:
    print("  L%d <- %s" % (n, t))
