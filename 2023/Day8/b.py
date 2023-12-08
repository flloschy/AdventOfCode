
import time
from math import gcd
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

currentNodes = []
iterations = []
for key, directions in nodes.items():
    if key.endswith("A"):
        currentNodes.append(key)
        iterations.append(None)


steps = 1
while True:
    end = False
    for instruction in instructions:
        for i, node in enumerate(currentNodes):
            if node == None: continue
            currentNodes[i] = nodes[node][instruction]
            if currentNodes[i].endswith("Z"):
                iterations[i] = steps
                currentNodes[i] = None
        steps += 1
        
        if all(node == None for node in currentNodes):
            end = True
            break
    if end: break

# https://stackoverflow.com/a/42472824
lcm = 1
for i in iterations:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)


###
print(f"Time Taken: {time.perf_counter()-start}s")
