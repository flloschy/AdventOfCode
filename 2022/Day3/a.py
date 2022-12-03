
import time
start = time.perf_counter()
####
content = open("./2022/Day3/input.txt", "r").read()
rucksacks = content.splitlines()
points = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
score = 0

for rucksack in rucksacks:
    rucksack = list(rucksack)
    compartment1 = set(rucksack[0:int(len(rucksack)/2)])
    compartment2 = set(rucksack[int(len(rucksack)/2):-1] + [rucksack[-1]])
    duplicates = {}
    for contain in compartment1:
        try: duplicates[contain] += 1
        except: duplicates[contain] = 1
    for contain in compartment2:
        try: duplicates[contain] += 1
        except: duplicates[contain] = 1

    score += points[max(duplicates, key=duplicates.get)]

print(score)


###
print(f"Time Taken: {time.perf_counter()-start}s")
