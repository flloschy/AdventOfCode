import time
start = time.perf_counter()
###
caves = [line.replace("\n", "").split("-") for line in open("./2021/Day12/input.txt").readlines()]


def loop(current, visited, caves, twice=False):
    if current == "end": return 1
    routesfound = 0
    for cave in caves:
        cave[0], cave[1] = cave
        if cave[0] == current:
            if not (cave[1].islower() and cave[1] in visited) :
                routesfound += loop(cave[1], visited + [cave[1]], caves, twice)
            elif not twice and cave[1] != "start":
                routesfound += loop(cave[1], visited + [cave[1]], caves, True)
        if cave[1] == current:
            if not (cave[0].islower() and cave[0] in visited) :
                routesfound += loop(cave[0], visited + [cave[0]], caves, twice)
            elif not twice and cave[0] != "start":
                routesfound += loop(cave[0], visited + [cave[0]], caves, True)
    return routesfound

print(loop("start", ["start"], caves))
###
print(f"Time Taken: {time.perf_counter()-start}s")