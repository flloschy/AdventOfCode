import time
start = time.perf_counter()
###
crabs = [int(x) for x in open("./2021/Day7/input.txt").read().split(',')]
fuleneeds = []
for height in range(min(crabs), max(crabs)+1):
    fule = 0
    for crab in crabs:
        lastfule = -1
        for dif in range(abs(height-crab)+1):
            fule += lastfule +1
            lastfule += 1
    fuleneeds.append(fule)
print(min(fuleneeds))
###
print(f"Time Taken: {time.perf_counter()-start}s")