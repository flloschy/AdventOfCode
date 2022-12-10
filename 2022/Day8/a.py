
import time
start = time.perf_counter()
####
content = open("./2022/Day8/input.txt", "r").read()
height = len(content.splitlines())
width = len(list(content.splitlines()[0]))
rows = [[[int(three), x, y] for x, three in enumerate(row)] for y, row in enumerate(content.splitlines())]
columns = [[[rows[x][y][0], y, x] for x in range(width)] for y in range(height)]

visible = [[False for _ in range(width)] for _ in range(height)]

for row in rows + rows[::-1]:
    highest = -1
    for three in row:
        h, x, y = three
        if x == 0 or y == 0 or x == width-1 or y == height-1:
            highest = h
            visible[y][x] = True
            continue
        if highest < h:
            highest = h
            visible[y][x] = True
    highest = -1
    for three in row[::-1]:
        h, x, y = three
        if x == 0 or y == 0 or x == width-1 or y == height-1:
            highest = h
            visible[y][x] = True
            continue
        if highest < h:
            highest = h
            visible[y][x] = True

for col in columns + columns[::-1]:
    highest = -1
    for three in col:
        h, x, y = three
        if x == 0 or y == 0 or x == width-1 or y == height-1:
            highest = h
            visible[y][x] = True
            continue
        if highest < h:
            highest = h
            visible[y][x] = True
    highest = -1
    for three in col[::-1]:
        h, x, y = three
        if x == 0 or y == 0 or x == width-1 or y == height-1:
            highest = h
            visible[y][x] = True
            continue
        if highest < h:
            highest = h
            visible[y][x] = True



        
count = 0
for row in visible:
    for three in row:
        if three:
            count += 1
print(count)
print(count == 1877)

###
print(f"Time Taken: {time.perf_counter()-start}s")
