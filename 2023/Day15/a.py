import time
start = time.perf_counter()
####
content = open("./2023/Day15/input.txt", "r").read().split(",")

sum_ = 0
for string in content:
    value = 0
    for char in string:
        value = (value + ord(char)) * 17 % 256
    sum_ += value
print(sum_)


###
print(f"Time Taken: {time.perf_counter()-start}s")
