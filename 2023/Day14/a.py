
import time
import numpy as np
start = time.perf_counter()
####

content = [[{ "O": 0, "#": 1, ".": 2}[char] for char in line]for line in open("./2023/Day14/input.txt", "r").read().splitlines()]

rocks = []
newContent = []

height = len(content) -1
width = len(content[0]) -1


for y, line in enumerate(content): 
    newLine = []
    for x, char in enumerate(line): 
        if char == 0: 
            rocks.append([x, y]) 
            newLine.append(2) 
        else: 
            newLine.append(char) 
    newContent.append(newLine) 

newContent = np.array(newContent)

rocks = set((x, y) for [x, y] in rocks)

def physics(ox=0, oy=0):
    moved = True
    while moved:
        moved = False
        for [x, y] in rocks:
            if (oy == -1 and y == 0): continue
            if (oy == 1 and y == height): continue
            if (ox == -1 and x == 0): continue
            if (ox == 1 and x == width): continue
            
            if newContent[y+oy, x+ox] == 2 and not ((x+ox, y+oy) in rocks):
                moved = True
                rocks.remove((x, y))
                rocks.add((x+ox, y+oy))

physics(oy=-1)

newContent2 = []
for y, line in enumerate(newContent):
    newLine = []
    for x, char in enumerate(line):
        if (x, y) in rocks:
            newLine.append(0)
        elif char == 1:
            newLine.append(1)
        else:
            newLine.append(2)
    newContent2.append(newLine)

count = 0
for y, line in enumerate(newContent2):
    value = len(newContent2) - y
    count += line.count(0) * value
print(count)


###
print(f"Time Taken: {time.perf_counter()-start}s")
