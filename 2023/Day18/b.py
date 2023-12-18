
import time
from shapely.geometry.polygon import Polygon # https://pypi.org/project/shapely/
start = time.perf_counter()
####



content = [[{"0":"R", "1":"D", "2":"L", "3":"U"}[str(line.split(" ")[2][-2])] , int(line.split(" ")[2][2:-2], base=16)] for line in open("./2023/Day18/input.txt", "r").read().splitlines()]

currentX = 0
currentY = 0
corners = []
lowestX = 0
lowestY = 0


for i, l in content:
    corners.append([currentX, currentY])
    if   i == "R": currentX += l
    elif i == "L": currentX -= l
    elif i == "D": currentY += l
    elif i == "U": currentY -= l

    if lowestX > currentX: lowestX = currentX
    if lowestY > currentY: lowestY = currentY
corners.append([currentX, currentY])

if lowestX > 0: lowestX = 0
if lowestY > 0: lowestY = 0

minX = min(corners, key=lambda node: node[0])[0]
maxX = max(corners, key=lambda node: node[0])[0]
minY = min(corners, key=lambda node: node[1])[1]
maxY = max(corners, key=lambda node: node[1])[1]

area = Polygon(corners).area + 1
for c1, c2 in zip(corners, corners[1:]):
    diffX = abs(c1[0] - c2[0])
    diffY = abs(c1[1] - c2[1])
    area += (diffX + diffY) / 2

print(area)
###
print(f"Time Taken: {time.perf_counter()-start}s")
