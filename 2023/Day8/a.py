
import time
start = time.perf_counter()
####
content = open("./2023/Day8/input.txt", "r").read().splitlines()
instructions = list(content[0])
del content[0]
del content[0]

nodes = {}

for line in content:
    node, directions = line.split(" = ")
    left, right = directions.replace("(","").replace(")","").split(", ")
    nodes[node] = {"L": left, "R": right}

current = "AAA"
turns = 0
while True:
    end = False
    for instruction in instructions:
        turns += 1
        current = nodes[current][instruction]
        if current == "ZZZ":
            end=True
            break
    if end: break
print(turns)

###
print(f"Time Taken: {time.perf_counter()-start}s")
