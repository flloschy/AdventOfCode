
import time
start = time.perf_counter()
####


content = open("./2022/Day4/input.txt", "r").read()
pairs = content.splitlines()
count = 0
for pair in pairs:
    a, b = pair.split(",")
    a, b = a.split("-"), b.split("-")
    a1, a2, b1, b2 = int(a[0]), int(a[1]), int(b[0]), int(b[1])
    a = [x for x in range(a1, a2)]
    b = range(b1, b2)
    if (b1 <= a1 <= b2) or (b1 <= a2 <= b2) or \
       (a1 <= b1 <= a2) or (a1 <= b2 <= a2):
        count += 1
print(count)
###
print(f"Time Taken: {time.perf_counter()-start}s")
