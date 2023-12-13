
import time
start = time.perf_counter()
####
content = open("./2023/Day13/input.txt", "r").read().split("\n\n")
maps = [[list(line) for line in map_.splitlines()] for map_ in content]

def stringify(x):
    return " ".join(["".join(y) for y in x])


def count(map_):
    old = 0
    for i in range(len(map_)):
        a, b = map_[:(i+1)], map_[i:][1:]
        l = min(len(a), len(b))
        # print(stringify(map_[(i+1-l):(i+1)])," @ " , stringify(map_[(i+1):(i+1+l)][::-1]))
        if map_[(i+1-l):(i+1)] == map_[(i+1):(i+1+l)][::-1] and len(map_[(i+1):(i+1+l)][::-1]) > 0 :
            old = i+1
            break

    for y in range(len(map_)):
        for x in range(len(map_[0])):
            oldChar = map_[y][x]
            newChar = '.' if oldChar == '#' else '#'
            map_[y][x] = newChar
            for i in range(len(map_)):
                a, b = map_[:(i+1)], map_[i:][1:]
                l = min(len(a), len(b))
                # print(stringify(map_[(i+1-l):(i+1)])," @ " , stringify(map_[(i+1):(i+1+l)][::-1]))
                if map_[(i+1-l):(i+1)] == map_[(i+1):(i+1+l)][::-1] and len(map_[(i+1):(i+1+l)][::-1]) > 0 :
                    if i+1 != old:
                        return i+1
            map_[y][x] = oldChar
    return 0


rows = sum([count(map_) for map_ in maps])


rotated = []
for map_ in maps:
    lines = []
    for x in range(len(map_[0])):
        line = []
        for y in range(len(map_)):
            line.append(map_[y][x])
        lines.append(line)
    rotated.append(lines)

columns = 0
columns = sum([count(map_) for map_ in rotated])
print(columns + 100*rows)
    

###
print(f"Time Taken: {time.perf_counter()-start}s")
