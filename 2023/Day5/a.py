
import time
start = time.perf_counter()
####
content = open("./2023/Day5/input.txt", "r").read().splitlines()
seeds = list(map(int, content[0].split(": ")[1].split(" ")))
content = content[2:]
numbers = [str(i) for i in range(10)]


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

def getIndex(range_, number):
    if range_.__contains__(number):
        return number - range_.start
    return False

def getMappedValue(mapped, inValue):
    for sourceRange, destinationRange in mapped:
        i = getIndex(sourceRange, inValue)
        if i:
            return destinationRange[i]
    return inValue

finals = []
for seed in seeds:
    path = [seed]
    for key in maps.keys():
        path.append(getMappedValue(maps[key], path[-1]))
    finals.append(path[-1])

print(min(finals))


###
print(f"Time Taken: {time.perf_counter()-start}s")
