import time
start = time.perf_counter()
###
crabs = [int(x) for x in open("./2021/Day7/input.txt").read().split(',')]
fuleneeds = []
print(range(min(crabs), max(crabs)+1))
for height in range(min(crabs), max(crabs)+1):
    fule = 0
    for crab in crabs:
        fule += abs(height-crab)
    fuleneeds.append(fule)
print(min(fuleneeds))
###
print(f"Time Taken: {time.perf_counter()-start}s")