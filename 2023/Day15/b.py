import time
start = time.perf_counter()
####
content = open("./2023/Day15/input.txt", "r").read().split(",")

lenses = {}
for i in range(256):
    lenses[i] = []

for string in content:
    if "=" in string:
        lable, lense = string.split("=")
        value = 0
        for char in lable:
            value = (value + ord(char)) * 17 % 256
        lense = int(lense)
        if any([l==lable for (l, _) in lenses[value]]):
            lenses[value] = [[l, f] if l != lable else [lable, lense] for (l, f) in lenses[value] ]
        else:
            lenses[value].append([lable, lense])
    elif string.endswith("-"):
        lable = string.removesuffix("-")
        value = 0
        for char in lable:
            value = (value + ord(char)) * 17 % 256
        lenses[value] = [lense for lense in lenses[value] if lense[0] != lable]

value = 0
for i in range(256):
    if lenses[i] != []:
        for i2, (lable, lense) in enumerate(lenses[i]):
            strength = (1 + i) * (1+i2) * lense
            value += strength

print(value)
    


###
print(f"Time Taken: {time.perf_counter()-start}s")
