import time
timestart = time.perf_counter()
###
points = {}
# for line in open("./2021/Day5/testcase.txt"):
for line in open("./2021/Day5/input.txt"):
    start, end = line.split(' -> ')
    x1, x2 = int(start.split(',')[0].strip()), int(end.split(',')[0].strip())
    y1, y2 = int(start.split(',')[1].strip()), int(end.split(',')[1].strip())
    dx = x2-x1
    dy = y2-y1
    for i in range(1+max(abs(dx), abs(dy))):
        x = x1+(1 if dx >0 else (-1 if dx<0 else 0))*i
        y = y1+(1 if dy>0 else (-1 if dy<0 else 0))*i
        if (x, y) not in points: 
            points[(x, y)] = 0
        points[(x, y)] += 1
timescrossed = 0
for point in points: 
    if points[point] > 1: timescrossed += 1
print(timescrossed)
###
print(f"Time Taken: {time.perf_counter()-timestart}s")