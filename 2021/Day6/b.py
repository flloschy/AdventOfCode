import sys, time
start = time.perf_counter()
###
fishlist = [int(i) for i in open("./2021/Day6/input.txt").read().split(',')]
days = 256
for day in range(1, days+1):
    # Progress Line
    # sys.stdout.write("\033[F")
    # sys.stdout.write("\033[K")
    # print(f"[{'|'*int(((day//4)/(days//4))*100)}{'.'*(100-int(((day//4)/(days//4))*100))}] {day} / {days}")
    for i in range(len(fishlist)):
        fishlist[i] -= 1
        if fishlist[i] == -1:
            fishlist[i] = 6
            fishlist.append(8)

print(len(fishlist))
###
print(f"Time Taken: {time.perf_counter()-start}s")