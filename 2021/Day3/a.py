import time
start = time.perf_counter()
###
gammab = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]] # gamma bits
for line in open("./2021/Day3/input.txt"):
    for i, b in enumerate(line.strip()):
        if b == "0": gammab[i][0] += 1
        else: gammab[i][1] += 1

ngammab, nepsilonb = "", "" # new gamma bits ||  new epsilon bits
for b in gammab:
    if b[0] > b[1]: ngammab += "1"; nepsilonb += "0"
    else: ngammab += "0"; nepsilonb += "1"

print(int(ngammab, 2)*int(nepsilonb, 2))
###
print(f"Time Taken: {time.perf_counter()-start}ms")