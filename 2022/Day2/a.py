
import time
start = time.perf_counter()
####
content = open("./2022/Day2/input.txt", "r").read()
rounds = content.splitlines()
score = 0


# A X = Rock | 1
# B Y = Paper | 2
# C Z = Scissors | 3
# Loose | 0
# Draw | 3
# Win | 6

points = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}


for round in rounds:
    score += points[round]

print(score)

###
print(f"Time Taken: {time.perf_counter()-start}s")
