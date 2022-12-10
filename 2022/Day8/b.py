
import time
start = time.perf_counter()
####
content = open("./2022/Day8/input.txt", "r").read()
height = len(content.splitlines())
width = len(list(content.splitlines()[0]))
rows = [[[int(three), x, y] for x, three in enumerate(row)] for y, row in enumerate(content.splitlines())]
score = [[0 for _ in range(width)] for _ in range(height)]

def getScore(three):
    h, x, y = three
    up = 0
    down = 0
    left = 0
    right = 0
    # down
    for y2 in range(y+1, height):
        t = rows[y2][x][0]
        if t < h:
            down += 1
        elif t == h or h < t:
            down += 1
            break
    # up
    for y2 in range(y-1, -1, -1):
        t = rows[y2][x][0]
        if t < h:
            up += 1
        elif t == h or h < t:
            up += 1
            break
    # right
    for x2 in range(x+1, width):
        t = rows[y][x2][0]
        if t < h:
            right += 1
        elif t == h or h < t:
            right += 1
            break
    # left
    for x2 in range(x-1, -1, -1):
        t = rows[y][x2][0]
        if t < h:
            left += 1
        elif t == h or h < t:
            left += 1
            break
    return up * down * left * right

scores = []
for row in rows:
    for three in row:
        scores.append(getScore(three))
print(max(scores))
###
print(f"Time Taken: {time.perf_counter()-start}s")
