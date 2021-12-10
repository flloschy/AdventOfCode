import time
start = time.perf_counter()
###
brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {"(": 1, "[": 2, "{": 3, "<": 4}
scorelist = []
for line in open("./2021/Day10/input.txt"):
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
    for y in line:
        if y in brackets.values():
            break
    else:
        score = 0
        line.reverse()
        for c in line:
            score*=5
            score+= scores[c]
        scorelist.append(score)
scores = sorted(scorelist)
print(scores[(len(scores)-1)//2])

###
print(f"Time Taken: {time.perf_counter()-start}s")