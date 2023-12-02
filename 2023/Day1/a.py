
import time, re
start = time.perf_counter()
####
content = open("./2023/Day1/input.txt", "r").read().splitlines()

def f(x):
    digits = [ch for ch in list(x) if ch.isdigit()]
    return int(f"{digits[0]}{digits[-1]}")

numbers = [f(line) for line in content]
print(sum(numbers))


###
print(f"Time Taken: {time.perf_counter()-start}s")
