# !/usr/bin/env python
from project import *
# from load import *
# from switchboard import *
a = Lighting(100, 0.95, 10, "LUZ1", "IDT1")
b = Lighting(200, 0.95, 15, "LUZ2", "IDT2")
c = Lighting(10, 1, 30, "LUZ3", "IDT3")
ckt1 = Circuit()
ckt1.add(a, b, c)
ckt2 = ckt1.copy()
sw1 = SwitchBoard()
sw1.add(ckt1, ckt2)
sw2 = sw1.copy()
print(ckt1)
print(ckt2)
pjt1 = Project()
pjt1.add(sw1, sw2)
pjt2 = pjt1.copy()
