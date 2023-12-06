
import time, math
start = time.perf_counter()
####
content = open("./2023/Day6/input.txt", "r").read().splitlines()
Time =  int(content[0].split(":")[1].replace(" ", ""))
Distance =  int(content[1].split(":")[1].replace(" ", ""))


def firstAttempt():
    solutions = 0
    for holdTime in range(Time):
        if holdTime*(Time-holdTime) > Distance: solutions += 1
        elif solutions > 0: break
    print("first attempt:", solutions)

def secondAttempt():
    root1 = (Time + math.sqrt(Time**2 - 4*Distance)) / 2
    root2 = (Time - math.sqrt(Time**2 - 4*Distance)) / 2

    first_holdTime = math.ceil(min(root1, root2))

    last_holdTime = math.ceil(max(root1, root2))

    print("second attempt:", last_holdTime-first_holdTime)

# firstAttempt()
secondAttempt()


###
print(f"Time Taken: {time.perf_counter()-start}s")
