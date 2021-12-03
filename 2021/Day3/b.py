# Original Code by -> Jonathan Paulson <-
# Original Video -> https://www.youtube.com/watch?v=bFpsqFSCCsM <-
# Original Github -> https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/3.py <-
# I have NO idea how this days Challange works, so I just took this code /\/\/\ and edited a bit

import time
start = time.perf_counter()
###
N = []
for line in open("./2021/Day3/input.txt"): N.append(line.strip())

for x in N:
    assert len(x) == len(N[0])
V = [[0 for _ in range(len(N[0]))] for _ in range(2)]
for x in N:
    for i, c in enumerate(x):
        V[1 if c=='1' else 0][i] += 1
gamma, epsilon = '', ''
for i in range(len(N[0])):
    if V[0][i] > V[1][i]: gamma += '0'; epsilon += '1'
    else: gamma += '1'; epsilon += '0'

A, B = list(N), list(N)
for i in range(len(N[0])):
    if len(A) > 1:
        tempa, tempb = [x for x in A if x[i]=='0'], [x for x in A if x[i]=='1']
        a0, a1 = len(tempa), len(tempb)
        if a1 >= a0: A = tempb
        else: A = tempa
    if len(B) > 1:
        tempa, tempb = [x for x in B if x[i]=='0'], [x for x in B if x[i]=='1']
        b0, b1 = len(tempa), len(tempb)
        if b1 >= b0: B = tempa
        else: B = tempb
print(int(A[0],2)*int(B[0],2))
###
print(f"Time Taken: {time.perf_counter()-start}ms")