
import time
start = time.perf_counter()
####
content = open("./2023/Day6/input.txt", "r").read().splitlines()
Time =  [int(num) for num in content[0].split(":")[1].split(" ") if num != ""]
Distance =  [int(num) for num in content[1].split(":")[1].split(" ") if num != ""]

def getBest(raceLength, record):
    def f(holdTime): return holdTime*(raceLength-holdTime)
    solutions = 0
    for holdTime in range(raceLength):
        if f(holdTime) > record: solutions += 1
        elif solutions > 0: break
    return solutions

sum_ = 1
for length, record in zip(Time, Distance):
    sum_ *= getBest(length, record)
print(sum_)

###
print(f"Time Taken: {time.perf_counter()-start}s")
