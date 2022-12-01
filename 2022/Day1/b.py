
import time
start = time.perf_counter()
####
content = open("./2022/Day1/input.txt", "r").read()
elfs = content.split("\n\n")
for i, elf in enumerate(elfs):
    calories = elf.split("\n")
    total = 0
    for calorie in calories:
        total += int(calorie)
    elfs[i] = total
elfs.sort(reverse=True)
print( elfs[0] + elfs[1] + elfs[2])

###
print(f"Time Taken: {time.perf_counter()-start}s")
