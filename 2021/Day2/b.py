import time
start = time.perf_counter()
###
aim, forward, height = 0, 0, 0
for line in open("./2021/Day2/input.txt"):
    content = str(line.strip()).split(' ')
    if content[0] == "up": 
        aim -= int(content[1])
    elif content[0] == "down":
        aim += int(content[1])
    elif content[0] == "forward": 
        forward += int(content[1])
        height += int(content[1])*aim
print(forward*height)
###
print(f"Time Taken: {time.perf_counter()-start}ms")