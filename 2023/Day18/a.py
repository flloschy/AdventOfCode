
import time
start = time.perf_counter()
####
content = [[line.split(" ")[0], int(line.split(" ")[1])] for line in open("./2023/Day18/input.txt", "r").read().splitlines()]

currentX = 0
currentY = 0
path = []

for i, l in content:
    for _ in range(l):
        path.append([currentX, currentY])
        if   i == "R": currentX += 1
        elif i == "L": currentX -= 1
        elif i == "U": currentY -= 1
        elif i == "D": currentY += 1 

lowestX = min(path, key=lambda node: node[0])[0]
if lowestX < 0:
    path = [[-lowestX+x, y] for x, y in path]
lowestY = min(path, key=lambda node: node[1])[1]
if lowestY < 0:
    path = [[x, -lowestY+y] for x, y in path]
path = [[1+x, 1+y] for x, y in path]
width = max(path, key=lambda node: node[0])[0]
height = max(path, key=lambda node: node[1])[1]


board = [["." for _ in range(width+2)] for _ in range(height+2)]

def string(b):
    return "\n".join(["".join(line) for line in b])

for x, y in path:
    board[y][x] = "#"

def getNeighbors(x, y):
    return [
        [x, y-1] if y-1 in range(height+2) else False,
        [x-1, y] if x-1 in range(width+2) else False,
        [x, y+1] if y+1 in range(height+2) else False,
        [x+1, y] if x+1 in range(width+2) else False
    ]

def filteredNeighbors(x,y):
    neighbors = getNeighbors(x, y)
    newNeighbors = []
    for neighbor in neighbors:
        if neighbor:
            x, y = neighbor
            char = board[y][x]
            if char == ".":
                newNeighbors.append([x, y])
    return newNeighbors


queue = [[0, 0]]

while queue:
    x, y = queue.pop()
    queue.extend(filteredNeighbors(x, y))
    board[y][x] = ","

s = string(board)
print(s)
s = s.replace(".", "#")
print(s.count("#"))



###
print(f"Time Taken: {time.perf_counter()-start}s")
