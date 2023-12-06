
import math
import multiprocessing
import time
start = time.perf_counter()
####
content = open("./2023/Day5/input.txt", "r").read().splitlines()
oldseeds = list(map(int, content[0].split(": ")[1].split(" ")))
newseeds = [range(seed, seed+oldseeds[i+1]) for i, seed in enumerate(oldseeds) if (i+1) % 2 != 0]
content = content[2:]
numbers = [str(i) for i in range(10)]

def merge_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda x: x.start)

    merged = []
    for higher in sorted_ranges:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            if higher.start <= lower.stop:
                upper_bound = max(lower.stop, higher.stop)
                merged[-1] = range(lower.start, upper_bound)
            else:
                merged.append(higher)
    return merged

maps = {}
current = ""
values = []
for line in content:
    if line == "":
        maps[current] = values
    elif line[0] not in numbers:
        current = line.split(" ")[0]
        values = []
    else:
        nums = list(map(int, line.split(" ")))
        destinationRangeStart = nums[0]
        sourceRangeStart = nums[1]
        rangeLength = nums[2]
        
        sourceRangeValues = range(sourceRangeStart, sourceRangeStart+rangeLength)
        destinationRangeValues = range(destinationRangeStart, destinationRangeStart+rangeLength)

        values.append((sourceRangeValues, destinationRangeValues))
maps[current] = values

from bisect import bisect_right
def getMappedValue(mapped:list[tuple[range, range]], inValue:int):
    mapped.sort(key=lambda x: x[0].start)
    i = bisect_right([x[0].start for x in mapped], inValue) - 1
    if 0 <= i < len(mapped) and mapped[i][0].start <= inValue < mapped[i][0].stop:
        return mapped[i][1][inValue - mapped[i][0].start]
    return inValue

def process_seeds(range_):
    smallest = math.inf
    length = len(range_)
    for i, seed in enumerate(range_):
        if i % 100000 == 0: print(range_, ':', i, '/', length, ' - ', round(i/length*100), '%')
        last = seed
        for mapped in maps.values():
            last = getMappedValue(mapped, last)
        smallest = min(smallest,last)
    return smallest

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        results = pool.map(process_seeds, newseeds)
    print(min(results))

###
print(f"Time Taken: {time.perf_counter()-start}s")
