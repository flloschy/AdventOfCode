import time

#    dddd
# e         a
# e         a
#    ffff
# g         b
# g         b
#    cccc

start = time.perf_counter()
###
c = 0
for line in open("./2021/Day8/input.txt"):
    for n in line.strip().split(' | ')[1].split(' '):
        if len(n) == 2 or len(n) == 4 or len(n) == 3 or len(n) == 7:
            c += 1

print(c)
###
print(f"Time Taken: {time.perf_counter()-start}s")


import time


#    dddd
# e         a
# e         a
#    ffff
# g         b
# g         b
#    cccc

# 1 = cf
# 2= acdeg
# 3 = acdfg
# 4 = bcdf
# 5 = abdfg
# 6 = abdefg
# 7 = acf
# 8 = abcdefg
# 9 = abcdfg
# 0 = abcefg
start = time.perf_counter()
###
def number(line:str):
    le = len(line)
    print("------", le, line)
    if le == 2: return 1
    if le == 3: return 7
    if le == 4: return 4
    if le == 5:
        if line.__contains__("e"): return 2
        if line.__contains__("c"): return 3
        return 5
    if le == 6: 
        if line.__contains__("c") and line.__contains__("d"): return 6
        if not line.__contains__("d"): return 0
        return 9
    return 8

c = 0
for line in open("./2021/Day8/input.txt"):
    for n in line.strip().split(' | ')[1].split(' '):
        if len(n) == 2 or len(n) == 4 or len(n) == 3 or len(n) == 7:
            print(n, "<--")
            c += 1
        else: print(n)

print(c)
###
print(f"Time Taken: {time.perf_counter()-start}s")