
import time
start = time.perf_counter()
####
content = open("./2023/Day9/input.txt", "r").read().splitlines()
content = [[[int(num) for num in line.split(" ")]] for line in content]

skip = []
while True:
    for i, values in enumerate(content):
        if i in skip: continue
        original, latest = values[0], values[-1]
        values.append([latest[i+1] - last for i, last in enumerate(latest[:-1])])
        
        if all(value == 0 for value in values[-1]):
            skip.append(i)

    if len(skip) == len(content): break


LastValues = []
for line in content:
    for i, diffs in enumerate(line[:-1]):
        line[i+1].append(line[i+1][-1] + diffs[-1])
    LastValues.append(line[-1][-1])

print(sum(LastValues))


###
print(f"Time Taken: {time.perf_counter()-start}s")