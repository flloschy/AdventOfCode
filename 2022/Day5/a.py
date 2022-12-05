
import time
start = time.perf_counter()
####

def container():
    container = []
    while True:
        i = input(f"Container {len(container)+1}: ")
        if i == "": break
        container += [list(i.upper())]
    return container



content = open("./2022/Day5/input.txt", "r").read()
instructions = [line for line in content.splitlines() if line.startswith("move")]
contents = container()
for instruction in instructions:
    instruction = instruction.split(" ")

    amount = int(instruction[1])
    fromStack = int(instruction[3]) - 1
    toStack = int(instruction[5]) - 1

    items = [contents[fromStack].pop(0) for _ in range(0, amount)]
    for item in items:
        contents[toStack].insert(0, item)

out = ""
for stack in contents:
    out += stack[0]
print(out)
###
print(f"Time Taken: {time.perf_counter()-start}s")
