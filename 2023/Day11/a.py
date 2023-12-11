from itertools import combinations
import time
start = time.perf_counter()
####
content = open("./2023/Day11/input.txt", "r").read().splitlines()

expansions_x = []
expansions_y = []

for y, line in enumerate(content):
    if all(char == "." for char in line):
        expansions_y.append(y)

rotated = list(zip(*content[::-1]))

for x, column in enumerate(rotated):
    if all(char == "." for char in column):
        expansions_x.append(x)

galaxies = []
for x, line in enumerate(content):
    for y, char in enumerate(line):
        if char == "#":
            X = x + sum([1 for expansion_y in expansions_y if expansion_y < x])
            Y = y + sum([1 for expansion_x in expansions_x if expansion_x < y])
            galaxies.append([X, Y])

visited = []
sum_ = 0

for i, galaxy in enumerate(galaxies):
    for galaxy2 in galaxies[i+1:]:
        pair = list(sorted((galaxy, galaxy2)))
        if pair in [visited]: continue
        sum_ += abs(galaxy2[0] - galaxy[0]) + abs(galaxy2[1] - galaxy[1])
        visited.append(pair)

print(sum_)

# print(list_combinations)

###
print(f"Time Taken: {time.perf_counter()-start}s")
