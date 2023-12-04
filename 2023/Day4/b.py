import time
start = time.perf_counter()
####
content = open("./2023/Day4/input.txt", "r").read().splitlines()
sum_ = 0
for line in content:
    game, nums = line.split(": ")
    winners, numbers = nums.split(" | ")
    winners = [int(num) for num in winners.split(" ") if num != ""]
    numbers = [int(num) for num in numbers.split(" ") if num != ""]
    value = 0
    for winner in winners:
        if winner in numbers:
            value += 1
    sum_ += value**2
print(sum_)

###
print(f"Time Taken: {time.perf_counter()-start}s")
