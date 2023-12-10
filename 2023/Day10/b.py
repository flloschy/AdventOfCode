
import time
start = time.perf_counter()
####
content = [list(line) for line in open("./2023/Day10/input.txt", "r").read().splitlines()]
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

startCell, end = [0, 0], False

for y, line in enumerate(content):
    for x, char in enumerate(line):
        if char=="S":
            startCell = [x, y]
            end = True
            break
    if end: break

neighbors = getAvailableNeighbors(*startCell)
neighbors.sort(key=lambda x: not x)
pathA = [startCell, neighbors[0]]
pathB = [startCell, neighbors[1]]

while not (pathA[-1][0] == pathB[-1][0] and pathA[-1][1] == pathB[-1][1]):
    neighborsA = getAvailableNeighbors(*pathA[-1])
    neighborsB = getAvailableNeighbors(*pathB[-1])
    neighborsA.remove(pathA[-2])
    neighborsB.remove(pathB[-2])
    neighborsA.sort(key=lambda x: not x)
    neighborsB.sort(key=lambda x: not x)
    pathA.append(neighborsA[0])
    pathB.append(neighborsB[0])

path = pathA[1:-1]
pathB.reverse()
path.extend(pathB)

# filter non path tiles out
content = [[char if [x, y] in path else '.' for x, char in enumerate(line)] for y, line in enumerate(content)]

def pairwise(iterable):
    it = iter(iterable)
    a = next(it, None)

    for b in it:
        yield (a, b)
        a = b

# a is always on the left side
def connectedHorizontal(a, b):
    return (a == "S" and b in ["-", "J", "7"]) or (a in ["-", "L", "F", "S"])

# a is always on top
def connectedVertical(a, b):
    return (a == "S" and b in ["|", "J", "L"]) or (a in ["|", "7", "F", "S"])

for y, line in enumerate(content):
    line.append(".")
    newLine = []
    for x, (char, nextChar) in enumerate(pairwise(line)):
        newLine.extend([char, "-"] if connectedHorizontal(char, nextChar) else [char, '.'])
    content[y] = newLine

content.insert(0, ["."]*(len(content[0])))
content.append(["."]*(len(content[0])))
stretchedContent = [["."] + content[0] + ["."]]

for line, nextLine in pairwise(content):
    lineInBetween = []
    for char, nextChar in zip(line, nextLine):
        lineInBetween.append("|" if connectedVertical(char, nextChar) else ".")
    stretchedContent.extend([["."] + lineInBetween + ["."], ["."] + nextLine + ["."]])

stretchedContent.insert(0, ["."]*(len(stretchedContent[0])))
stretchedContent.append(["."]*(len(stretchedContent[0])))

queue = [[0, 0]]
filled = [[char for char in line] for line in stretchedContent]
def getFillable(x, y):
    top = filled[y-1][x] == "." if y-1 in range(len(filled)) else False
    bottom = filled[y+1][x] == "." if y+1 in range(len(filled)) else False
    left = filled[y][x-1] == "." if x-1 in range(len(filled[0])) else False
    right = filled[y][x+1] == "." if x+1 in range(len(filled[0])) else False

    pos = []

    if top and [x, y-1] not in queue:
        pos.append([x, y-1,])
    if bottom and [x, y+1] not in queue:
        pos.append([x, y+1])
    if left and [x-1, y] not in queue:
        pos.append([x-1, y])
    if right and [x+1, y] not in queue:
        pos.append([x+1, y])

    return pos

while queue:
    current = queue.pop(-1)
    for fillable in getFillable(*current):
        filled[fillable[1]][fillable[0]] = " "
        queue.append(fillable)

collapsed = [[char for char in line[1::2]] for line in filled[1::2]]

print(("\n".join("".join(line) for line in collapsed)).count("."))
###

print(f"Time Taken: {time.perf_counter()-start}s")
