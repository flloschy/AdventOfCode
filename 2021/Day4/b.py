import time
start = time.perf_counter()
###
filecontent = open("./2021/Day4/input.txt").read().split("\n")
bingonumbers = filecontent[0].split(',')
filecontent.remove(filecontent[0])

########## set up board data
boards = []
tempboard = []
for line in filecontent:
    if line != '':
        tempboard.append({
            line.split()[0]: False,
            line.split()[1]: False,
            line.split()[2]: False,
            line.split()[3]: False,
            line.split()[4]: False
        })
    else:
        boards.append(tempboard)
        tempboard = []
del tempboard
##########

finalscore = 0

boardswon = []

for num in bingonumbers:
    for board in boards:
        if board in boardswon: continue
        for n in board:
            for key in n.keys():
                if not n[key] and key == num:
                    n[key] = True

        horizontals = [[], [], [], [], []]
        verticals = [[], [], [], [], []]
        for i1, n in enumerate(board):
            for i2, key in enumerate(n.keys()):
                if n[key]:
                    verticals[i1].append(None)
                    horizontals[i2].append(None)

        for current, vert in enumerate(verticals):
            if len(vert) == 5:
                total = 0
                for n in board:
                    for key in n.keys():
                        if not n[key]:
                            total += int(key)
                finalscore = total*int(num)
                boardswon.append(board)
                break

        for current, hori in enumerate(horizontals):
            if len(hori) == 5:
                total = 0
                for n in board:
                    for key in n.keys():
                        if not n[key]:
                            total += int(key)
                finalscore = total*int(num)
                boardswon.append(board)
                break

print(finalscore)
###
print(f"Time Taken: {time.perf_counter()-start}s")