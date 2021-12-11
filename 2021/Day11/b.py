import time

def printit(octos):
    if False: return # Change to 'True' to disable printing
    for octo in octos:
        for n in octo:
            if n == 0: print("<#>", end='')
            else: print(f" {n} ", end='')
        print("")
    print("\n")

start = time.perf_counter()
###
octopuses = [[int(x) for x in line.strip()] for line in open("./2021/Day11/input.txt")]
preparedgrid = [(x, y) for y in range(len(octopuses)) for x in range(len(octopuses[0]))]
flashes = 0
printit(octopuses)
allon = False
eteration = 0
while not allon:
    eteration += 1
    grid = preparedgrid.copy()
    while len(grid) > 0:
        x, y = grid.pop(0)
        octopuses[y][x] += 1
        if octopuses[y][x] == 10:
            for dif in range(-1, 2):
                for dif2 in range(-1, 2):
                    if x+dif == x and y+dif2 == y: continue
                    if x+dif < 0 or y+dif2 < 0: continue
                    try: octopuses[y+dif2][x+dif]
                    except: continue
                    grid.append((x+dif, y+dif2))
    flash = 0
    for x, y in [(x, y) for x, y in preparedgrid.copy() if octopuses[y][x] >= 10]:
        flash += 1
        octopuses[y][x] = 0
    printit(octopuses)
    if flash == len(preparedgrid): allon = True
    flashes += flash
else:
    # print(flashes)
    print(eteration)
###
print(f"Time Taken: {time.perf_counter()-start}s")