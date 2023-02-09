import random

def f():
    t1 = random.randint(1, 47)
    d1 = 49 - t1 - 1
    z11 = t1 % 4
    if z11 == 0:
        z11 += 4
    z12 = d1 % 4
    if z12 == 0:
        z12 += 4
    b1 = 49 - 1 - z11 - z12
    t2 = random.randint(1, b1 - 2)
    d2 = b1 - t2 - 1
    z21 = t2 % 4
    if z21 == 0:
        z21 += 4
    z22 = d2 % 4
    if z22 == 0:
        z22 += 4
    b2 = b1 - 1 - z21 - z22
    t3 = random.randint(1, b2 - 2)
    d3 = b2 - t3 - 1
    z31 = t3 % 4
    if z31 == 0:
        z31 += 4
    z32 = d3 % 4
    if z32 == 0:
        z32 += 4
    b3 = b2 - z32 - z31 - 1
    y1 = b3 / 4
    return y1

results = []
for i in range(6):
    result = f()
    if result == 6:
        results.append("老阴")
    elif result == 7:
        results.append("少阳")
    elif result == 8:
        results.append("少阴")
    elif result == 9:
        results.append("老阳")

print("本卦为：")
for result in results:
    print(result)

new_results = []
for result in results:
    if result == "老阴":
        new_results.append("老阳")
    elif result == "老阳":
        new_results.append("老阴")
    else:
        new_results.append(result)

print("变卦为：")
for result in new_results:
    print(result)
