
import time
start = time.perf_counter()
####
content = open("./2022/Day7/input.txt", "r").read()
sizeSystem = {}
currentDir = []
for line in content.splitlines():
    if line.startswith("$ cd"):
        if line.endswith(".."):
            currentDir.pop(-1)
        else:
            currentDir.append(line.split(" ")[-1])
    elif line.startswith("$ ls"):
        continue
    else:
        if line.startswith("dir "):
            continue
        else:
            size, name = line.split(" ")
            
            for i, dir in enumerate(currentDir):
                try:
                    sizeSystem["/".join(currentDir[0:i] + [dir]).replace("//", "/")] += int(size)
                except:
                    sizeSystem["/".join(currentDir[0:i] + [dir]).replace("//", "/")] = int(size)
totalSize = 0
dirs = []
for dir in sizeSystem.keys():
    size = sizeSystem[dir]
    if size <= 100000:
        dirs.append(size)
print(sum(dirs))

###
print(f"Time Taken: {time.perf_counter()-start}s")
