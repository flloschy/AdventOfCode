
import time
start = time.perf_counter()
####
content = open("./2022/Day10/input.txt", "r").read()
commands = content.splitlines()

V = 1
cycle = 0
out = []
tasks = [0] * (len(commands)+100)
for cmd in commands:
    if cmd == "noop":
        cycle += 1
    else:
        cycle += 2
        tasks[cycle] = int(cmd.split(" ")[1])

for i, task in enumerate(tasks):
    V += task
    out.append("\x1b[47m " if abs(V-(i%40))<=1 else "\x1b[0m ")

for i, x in enumerate(out):
    if i == 40 or \
        i == 80 or \
        i == 120 or \
        i == 160 or \
        i == 200:
        print("\x1b[0m")
    print(x, end='')
    if i == 239: break
print("\x1b[0m\n")

###
print(f"Time Taken: {time.perf_counter()-start}s")
