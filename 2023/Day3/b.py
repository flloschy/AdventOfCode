import time
start = time.perf_counter()
####
content = open("./2023/Day3/input.txt", "r").read().splitlines()

for y, line in enumerate(content):
    content[y] += "."

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def getNeighbors(y, x):
    chars = []
    for ox in range(-1, 2):
        for oy in range(-1, 2):
            if ox == 0 and oy == 0: continue
            X, Y = x + ox, y + oy
            try:
                char = content[Y][X]
                chars.append(((Y, X), char))
            except IndexError:
                chars.append(((Y, X), ""))
    return chars

def getNumber(y, x):
    if content[y][x] == ".": return
    start = x + 1
    number = []
    while True:
        x = start - 1
        char = content[y][x]
        if char not in numbers:
            start = x + 1
            break
        else:
            start = x

    while True:
        try:
            char = content[y][start]
            if char not in numbers: break
            start += 1 
            number.append(((y, start), char))
        except IndexError:
            continue
    return number

def filteredNeighbors(y, x):
    neighbors = getNeighbors(y, x)
    nums = []
    for (Y, X), char in neighbors:
        if char in numbers:
            number = getNumber(Y, X)
            if number not in nums:
                nums.append(number)
    return [int("".join([char for (_,_), char in num])) for num in nums]

sum_ = 0
for y, _ in enumerate(content):
    for x, _ in enumerate(content[y]):
        if content[y][x] == "*":
            neighbors = filteredNeighbors(y, x)
            if len(neighbors) == 2:
                sum_ += neighbors[0] * neighbors[1]

print(sum_)
###
print(f"Time Taken: {time.perf_counter()-start}s")
