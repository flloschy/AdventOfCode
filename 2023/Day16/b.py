import time
import numpy as np
started = time.perf_counter()
####

VERTICAL = 0   #  |
HORIZONTAL = 1 #  -
SLASH = 2      #  /
BACKSLASH = 3  #  \
EMPTY = 4      #  .

mapped = {
    "|": VERTICAL,
    "-": HORIZONTAL,
    "/": SLASH,
    "\\": BACKSLASH,
    ".": EMPTY
}

content = np.array([[mapped[char] for char in line] for line in open("./2023/Day16/input.txt", "r").read().splitlines()])

height = range(len(content))
width = range(len(content[0]))



TOP = 0
LEFT = 1
BOTTOM = 2
RIGHT = 3
a = {
    TOP: RIGHT,
    LEFT: BOTTOM,
    BOTTOM: LEFT,
    RIGHT: TOP
}
b = {
    TOP: LEFT,
    LEFT: TOP,
    BOTTOM: RIGHT,
    RIGHT: BOTTOM
}
value = 0
borders = []
for i in width:
    borders.append([i, -1, BOTTOM])
    borders.append([i, len(height), TOP])
for i in height:
    borders.append([-1, i, RIGHT])
    borders.append([len(width), i, LEFT])

for start in borders:

    beams, charged = [start], set()
    charged.add((start[0], start[1], RIGHT))

    changed = True
    delete = set()
    while changed:
        changed = False
        for i, (currentX, currentY, direction) in enumerate(beams):
            match direction:
                case 0: currentY -= 1
                case 1: currentX -= 1
                case 2: currentY += 1
                case 3: currentX += 1

            if currentX not in width:
                delete.add(i)
                continue
            if currentY not in height:
                delete.add(i)
                continue
            if (currentX, currentY, direction) in charged:
                delete.add(i)
                continue

            changed = True

            charged.add((currentX, currentY, direction))

            match content[currentY, currentX]:
                case 0:
                    if direction == LEFT or direction == RIGHT:
                        delete.add(i)
                        beams.extend([[currentX, currentY, TOP], [currentX, currentY, BOTTOM]])
                case 1:
                    if direction == TOP or direction == BOTTOM:
                        delete.add(i)
                        beams.extend([[currentX, currentY, LEFT], [currentX, currentY, RIGHT]])
                case 2:
                    direction = a[direction]
                case 3:
                    direction = b[direction]
            beams[i] = [currentX, currentY, direction]
        beams = [beam for i, beam in enumerate(beams) if i not in delete]
        delete.clear()

    everyPath = set()
    for x, y, _ in charged:
        everyPath.add((x, y))
    energized = len(everyPath)-1
    if energized > value:
        value = energized
print(value)
###
print(f"Time Taken: {time.perf_counter()-started}s")
