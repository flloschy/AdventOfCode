
import time
start = time.perf_counter()
####
content = open("./2022/Day10/input.txt", "r").read()
commands = content.splitlines()

V = 1
cycle = 0
strengths = []
tasks = [0] * (len(commands)+100)
for cmd in commands:
    if cmd == "noop":
        cycle += 1
    else:
        cycle += 2
        tasks[cycle] = int(cmd.split(" ")[1])

for i, task in enumerate(tasks):
    if i == 20 or \
        i == 60 or \
        i == 100 or \
        i == 140 or \
        i == 180 or \
        i == 220:
        strengths.append(i*V)
    V += task

print(sum(strengths))
###
print(f"Time Taken: {time.perf_counter()-start}s")
