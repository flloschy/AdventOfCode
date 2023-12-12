import time
start = time.perf_counter()
####
content = [["." + line.split(" ")[0] + ".", [int(num) for num in line.split(" ")[1].split(",")]] for line in open("./2023/Day12/input.txt", "r").read().splitlines()]


sum_ = 0

for line in content:
    questionMarks = line[0].count("?") + 1
    currentNumber = int("1" + "0"*(questionMarks-1), 2)
    goalAmountOfOnes = sum(line[1]) - line[0].count("#") + 1
    validCombinations = 0
    while True:
        bits = bin(currentNumber)
        currentNumber += 1
        bl = len(bits) - 2
        if bl > questionMarks: break
        if bl != questionMarks: continue
        if bits.count("1") != goalAmountOfOnes: continue
        workingString = line[0]
        for x, bit in enumerate(bits[3:]):
            positionOfQuestionMark = workingString.index("?", x + 1)
            workingString = workingString[:positionOfQuestionMark] + ("#" if bit == "1" else ".") + workingString[positionOfQuestionMark+1:]
            # tmpStr[tmpStr.index("?", x + 1)] = "#" if bit == "1" else "."
        workingString = [len(s) for s in workingString.split(".") if s != ""]
        if len(workingString) != len(line[1]): continue
        if workingString == line[1]:
            validCombinations += 1
    sum_ += validCombinations
print(sum_)

###
print(f"Time Taken: {time.perf_counter()-start}s")
