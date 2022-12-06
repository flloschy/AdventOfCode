
import time
start = time.perf_counter()
####
content = open("./2022/Day6/input.txt", "r").read()

buffer = [" "] * 14
count = 0

for char in list(content):
    count += 1
    buffer.pop(0)
    buffer.append(char)
    if len(set("".join(buffer).replace(" ", ""))) == 14:
        break
print(count)

###
print(f"Time Taken: {time.perf_counter()-start}s")
