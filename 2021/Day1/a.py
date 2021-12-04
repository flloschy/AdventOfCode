import time
start = time.perf_counter()
####
last, count = 0, 0
for line in open("./2021/Day1/input.txt"):
    count += int(line.strip()) > last
    last = int(line.strip())
print(count-1)
###
print(f"Time Taken: {time.perf_counter()-start}s")