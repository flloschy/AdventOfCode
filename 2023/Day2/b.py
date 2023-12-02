import time
start = time.perf_counter()
####
content = open("./2023/Day2/input.txt", "r").read().splitlines()

counter = 0
for i, game in enumerate(content):
    sets = game.split(": ")[1].split("; ")
    count = { 'red': 0, 'green': 0, 'blue': 0 }
    for _set in sets:
        plays = _set.split(", ")
        for play in plays:
            num, color = play.split(" ")
            count[color] = max(count[color], int(num))
    counter += count['red'] * count["green"] * count["blue"]
print(counter)

###
print(f"Time Taken: {time.perf_counter()-start}s")
