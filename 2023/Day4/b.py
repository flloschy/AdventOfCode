"""
Honestly, IDK What the hell should be done in this days part 2...
Which is why I used https://github.com/oogles/aoc_2023/blob/main/solutions/day04/solvers.py
as a guideline and basically copied it... sorry...
But I tried to make it my own with using some of the part 1 code
I wrote myself
"""
import time
start = time.perf_counter()
####
content = open("./2023/Day4/input.txt", "r").read().splitlines()
sum_ = 0


counts = {}
def recursion(i):
    if i in counts: return counts[i]
    _, nums = content[i].split(": ")
    winners, numbers = nums.split(" | ")
    winners = [int(num) for num in winners.split(" ") if num != ""]
    numbers = [int(num) for num in numbers.split(" ") if num != ""]

    overlapCount = 0
    for winner in winners:
        if winner in numbers:
            overlapCount += 1

    counter = 1

    for i2 in range(overlapCount):
        counter += recursion(i + i2 + 1)

    counts[i] = counter
    return counter


for i, _ in enumerate(content):
    recursion(i)

print(sum(counts.values()))

###
print(f"Time Taken: {time.perf_counter()-start}s")
