import time
start = time.perf_counter()
###
a, b, c, count  = 0, 0, 0, 0
for line in open("./2021/Day1/input.txt"):
    count += not (a == 0 or b == 0 or c == 0) and int(line.strip())+a+b > a+b+c
    a, b, c = int(line.strip()), a, b
print(count)
###
print(f"Time Taken: {time.perf_counter()-start}s")