import random

def f():
    t1 = random.randint(0, 47)
    d1 = 49 - t1 - 1
    z11 = t1 % 4
    if z11 == 0:
        z11 = z11 + 4
    z12 = d1 % 4
    if z12 == 0:
        z12 = z12 + 4
    b1 = 49 - 1 - z11 - z12
    t2 = random.randint(0, b1-2)
    d2 = b1 - t2 - 1
    z21 = t2 % 4
    if z21 == 0:
        z21 = z21 + 4
    z22 = d2 % 4
    if z22 == 0:
        z22 = z22 + 4
    b2 = b1 - 1 - z21 - z22
    t3 = random.randint(0, b2-2)
    d3 = b2 - t3 - 1
    z31 = t3 % 4
    if z31 == 0:
        z31 = z31 + 4
    z32 = d3 % 4
    if z32 == 0:
        z32 = z32 + 4
    b3 = b2 - z32 - z31 - 1
    y1 = b3 / 4
    return y1

for i in range(6):
    result = f()
    print("Result", i+1, ": ", result)
