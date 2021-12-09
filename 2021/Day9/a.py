import time
start = time.perf_counter()
###
lines = []
for x in open("./2021/Day9/input.txt").read().split('\n'):
    li = []
    for l in x: li.append(int(l))
    lines.append(li)
risk = 0
for i, y in enumerate(lines):
    for i2, x in enumerate(y):
        adjacent = []
        try: adjacent.append(lines[i-1][i2])
        except: pass
        try: adjacent.append(lines[i][i2-1])
        except: pass
        try: adjacent.append(lines[i][i2+1])
        except: pass
        try: adjacent.append(lines[i+1][i2])
        except: pass
        if x < min(adjacent):
            risk += x +1
print(risk)
###
print(f"Time Taken: {time.perf_counter()-start}s")