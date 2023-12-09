
import time
start = time.perf_counter()
####
content = open("./2023/Day8/input.txt", "r").read().splitlines()
instructions = list(content[0])
content, nodes = content[2:], {}

for line in content:
    node, directions = line.split(" = ")
    left, right = directions.replace("(","").replace(")","").split(", ")
    nodes[node] = {"L": left, "R": right}

current, turns = "AAA", 0
while current != "ZZZ":
    for instruction in instructions:
        turns += 1
        current = nodes[current][instruction]
        if current == "ZZZ": break
print(turns)

###
print(f"Time Taken: {time.perf_counter()-start}s")
