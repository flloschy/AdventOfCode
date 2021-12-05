import time
timestart = time.perf_counter()
###
points = {}
for line in open("./2021/Day5/input.txt"):
    start, end = line.split(' -> ')
    x1, x2 = min(int(start.split(',')[0]), int(end.split(',')[0])), max(int(start.split(',')[0]), int(end.split(',')[0]))
    y1, y2 = min(int(start.split(',')[1]), int(end.split(',')[1])), max(int(start.split(',')[1]), int(end.split(',')[1]))
    if x1 == x2 or y1 == y2:
        for x in range(x1, x2+1): 
            for y in range(y1, y2+1):
                if (x, y) not in points: points[(x, y)] = 0
                points[(x, y)] += 1

timescrossed = 0
for point in points: 
    if points[point] > 1: timescrossed += 1
print(timescrossed)
###
print(f"Time Taken: {time.perf_counter()-timestart}s")