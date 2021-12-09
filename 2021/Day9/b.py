import time
start = time.perf_counter()
###
lines = []
for x in open("./2021/Day9/input.txt").read().split('\n'):
    li = []
    for l in x: li.append(int(l))
    lines.append(li)

basinbeginns = {}
for i, y in enumerate(lines):
    for i2, x in enumerate(y):
        if x == 9: continue
        tempx = i2
        tempy = i
        while True:
            c1, c2, c3, c4 = False, False, False, False
            try:
                if tempx+1 < 100 and lines[tempy][tempx+1] < lines[tempy][tempx]: 
                    c1 = True; tempx += 1
            except: pass
            try:
                if tempx-1 > -1 and lines[tempy][tempx-1] < lines[tempy][tempx]: 
                    c2 = True; tempx -= 1
            except: pass
            try:
                if tempy+1 < 100 and lines[tempy+1][tempx] < lines[tempy][tempx]: 
                    c3 = True; tempy += 1
            except: pass
            try:
                if tempy-1 > -1 and lines[tempy-1][tempx] < lines[tempy][tempx]: 
                    c4 = True; tempy -= 1
            except: pass
            if all([not c1, not c2, not c3, not c4]):
                break
        if (tempx, tempy) not in basinbeginns.keys(): basinbeginns.update({(tempx, tempy): 0})
        basinbeginns[(tempx, tempy)] += 1
basinbeginns = sorted(basinbeginns.values(), reverse=True)
print(basinbeginns[0]*basinbeginns[1]*basinbeginns[2])
###
print(f"Time Taken: {time.perf_counter()-start}s")