import time
start = time.perf_counter()
###
brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
score = {")": 0, "]": 0, "}": 0, ">": 0}
for line in open("./2021/Day10/input.txt"):
    print("-----")
    line = list(line.removesuffix("\n"))
    while True:
        for i, bracket in enumerate(line):
            if bracket in brackets.keys():
                if i != len(line)-1:
                    if line[i+1] == brackets[bracket]:
                        del line[i:i+2]
                        break
        else:
            break
    print(line)
    for i, bracket in enumerate(line):
        if i+1 != len(line):
            if bracket in brackets.keys():
                if line[i+1] in brackets.values():
                    print(bracket, line[i+1])
                    score[line[i+1]] += scores[line[i+1]]
print(sum(score.values()))
###
print(f"Time Taken: {time.perf_counter()-start}s")