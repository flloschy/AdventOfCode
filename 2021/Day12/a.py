import time
start = time.perf_counter()
###
caves = [line.replace("\n", "").split("-") for line in open("./2021/Day12/input.txt").readlines()]

def loop(cur, visted, caves):
    if cur == "end": return 1
    routesfound = 0
    for cave in caves:
        if cave[0] == cur and not (cave[1].islower() and cave[1] in visted):
            routesfound += loop(cave[1], visted + [cave[1]], caves)
        elif cave[1] == cur and not (cave[0].islower() and cave[0] in visted):
            routesfound += loop(cave[0], visted + [cave[0]], caves)
    return routesfound

print(loop("start", ["start"], caves))
###
print(f"Time Taken: {time.perf_counter()-start}s")