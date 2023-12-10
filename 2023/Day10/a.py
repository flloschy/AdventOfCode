
import time
start = time.perf_counter()
####
content = open("./2023/Day10/input.txt", "r").read().splitlines()
content = [list(line) for line in content]
width, height = range(len(content[0])), range(len(content))



# [top, bottom, left, right]
def getAvailableNeighbors(x, y):
    center = content[y][x]

    top = content[y-1][x] in ["F", "7", "|", "S"] if y-1 in height else False
    bottom = content[y+1][x] in ["J", "L", "|", "S"] if y+1 in height else False
    left = content[y][x-1] in ["F", "L", "-", "S"] if x-1 in width else False
    right = content[y][x+1] in ["J", "7", "-", "S"] if x+1 in width else False

    if center == ".": return [ False, False, False, False ]
    if center == "-": return [ False, False, [x-1, y] if left else False, [x+1, y] if right else False ]

    if center == "|": return [ [x, y-1] if top else False, [x, y+1] if bottom else False, False, False ]
    if center == "J": return [ [x, y-1] if top else False, False, [x-1, y] if left else False, False ]
    if center == "L": return [ [x, y-1] if top else False, False, False, [x+1, y] if right else False ]

    if center == "7": return [ False, [x, y+1] if bottom else False, [x-1, y] if left else False, False]
    if center == "F": return [ False, [x, y+1] if bottom else False, False, [x+1, y] if right else False ]

    if center == "S": return [ [x, y-1] if top else False, [x, y+1] if bottom else False, [x-1, y] if left else False, [x+1, y] if right else False ]

def same(a, b):
    return a[0] == b[0] and a[1] == b[1]

startCell = [0, 0]
end = False
for y, line in enumerate(content):
    for x, char in enumerate(line):
        if char=="S":
            startCell = [x, y]
            end = True
            break
    if end: break


# 0 = top
# 1 = bottom
# 2 = left
# 3 = right


neighbors = getAvailableNeighbors(*startCell)
neighbors.sort(key=lambda x: not x)
pathA = [startCell, neighbors[0]]
pathB = [startCell, neighbors[1]]


while not same(pathA[-1],pathB[-1]):
    neighborsA = getAvailableNeighbors(*pathA[-1])
    neighborsA.remove(pathA[-2])
    neighborsA.sort(key=lambda x: not x)
    pathA.append(neighborsA[0])

    neighborsB = getAvailableNeighbors(*pathB[-1])
    neighborsB.remove(pathB[-2])
    neighborsB.sort(key=lambda x: not x)
    pathB.append(neighborsB[0])

print(len(pathA)-1)



###

print(f"Time Taken: {time.perf_counter()-start}s")
