
import time
start = time.perf_counter()
####
content = open("./2022/Day2/input.txt", "r").read()
rounds = content.splitlines()
score = 0


# X loose
# Y draw
# Z win
# A = Rock | 1
# B = Paper | 2
# C = Scissors | 3

points = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}


for round in rounds:
    score += points[round]

print(score)

###
print(f"Time Taken: {time.perf_counter()-start}s")
