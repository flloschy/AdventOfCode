
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
print(elfs[elfs.index(max(elfs))])

###
print(f"Time Taken: {time.perf_counter()-start}s")
