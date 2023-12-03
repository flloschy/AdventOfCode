import time
start = time.perf_counter()
####
content = open("./2023/Day3/input.txt", "r").read().splitlines()

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def getNeighbors(y, x):
    chars = []
    for ox in range(-1, 2):
        for oy in range(-1, 2):
            if ox == 0 and oy == 0: continue
            X, Y = x + ox, y + oy
            try:
                char = content[Y][X]
                chars.append(char)
            except IndexError: continue 
    return chars

def isConnectedToSymbol(y, x):
    chars = "".join(getNeighbors(y, x))
    for char in chars:
        if char not in numbers and char != ".":
            return True
    return False

def cleanLine(y):
    chars = []
    nums = []
    for x, char in enumerate(content[y]):
        if char in numbers:
            chars.append(((y, x), char))
        else:
            nums.append(chars.copy())
            chars.clear()
    nums.append(chars)
    return [num for num in nums if len(num) > 0]

def getNumbers(y):
    numbers = []
    for num in cleanLine(y):
        connected = False
        for (y, x), char in num:
            if isConnectedToSymbol(y, x):
                connected = True
                break
        if connected:
            number = "".join([char for (_,_), char in num])
            numbers.append(int(number))
    return numbers

sum_ = 0
for y, _ in enumerate(content):
    nums = getNumbers(y)
    for num in nums:
        sum_ += num
print(sum_)


###
print(f"Time Taken: {time.perf_counter()-start}s")
