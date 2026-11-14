# -*- coding: utf-8 -*-
"""Replace the broken DataValidation line with a quote-order-safe construction."""
import io, sys

P = r"C:\Users\ALSAHABA\Downloads\GIS EVENT\Green_Grow_Bot_Package\build_risk_register.py"
src = io.open(P, encoding="utf-8").read()
lines = src.split("\n")

new = [
    'STATES_AR = "' + "\u0644\u0645 \u064a\u0628\u062f\u0623," +
    "\u062c\u0627\u0631\u064a," + "\u0645\u0646\u062c\u0632," +
    "\u0645\u062a\u0639\u062b\u0631" + '"',
    'dv3 = DataValidation(type="list", formula1=chr(34) + STATES_AR + chr(34), allow_blank=True)',
]

for i, l in enumerate(lines):
    if l.startswith("dv3 = DataValidation"):
        lines[i:i + 1] = new
        break
else:
    sys.stderr.write("target line not found\n")
    sys.exit(1)

out = "\n".join(lines)
io.open(P, "w", encoding="utf-8").write(out)
try:
    compile(out, P, "exec")
    print("COMPILE OK")
except SyntaxError as e:
    print("ERR", e.lineno, e.msg, repr(e.text))
