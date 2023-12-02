import time
start = time.perf_counter()
####
content = open("./2023/Day2/input.txt", "r").read().splitlines()

maximum = { 'red': 12, 'green': 13, 'blue': 14 }; possible = 0
for i, game in enumerate(content):
    sets = game.split(": ")[1].split("; ")
    toMuch = False
    for _set in sets:
        plays = _set.split(", ")
        for play in plays:
            num, color = play.split(" ")
            if int(num) > maximum[color]: toMuch = True
    if not toMuch: possible += i+1
print(possible)

###
print(f"Time Taken: {time.perf_counter()-start}s")
