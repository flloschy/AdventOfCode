import os
year = 2022

baseCode = """
import time
start = time.perf_counter()
####
content = open("<path>", "r").read()


###
print(f"Time Taken: {time.perf_counter()-start}s")
"""

baseMD = """
# Day <day>
### `- title -`
#### Part 1
> - [My](https://github.com/flloschy) answer was `- answer -` . ([Here](https://github.com/flloschy/AdventOfCode/blob/main/<year>/Day<day>/a.py))

#### Part 2
> - [My](https://github.com/flloschy) answer was `- answer -` . ([Here](https://github.com/flloschy/AdventOfCode/blob/main/<year>/Day<day>/b.py))

###### [Source](https://adventofcode.com/<year>/day/<day>)
"""


if not os.path.exists(f"./{year}"):
    os.mkdir(f"./{year}")
for i in range(1, 26):
    os.mkdir(f"./{year}/Day{i}")
    open(f"./{year}/Day{i}/input.txt", "x")
    with open(f"./{year}/Day{i}/a.py", "x") as afile:
        afile.write(baseCode.replace("<path>", f"./{year}/Day{i}/input.txt"))
    with open(f"./{year}/Day{i}/b.py", "x") as afile:
        afile.write(baseCode.replace("<path>", f"./{year}/Day{i}/input.txt"))
    with open(f"./{year}/Day{i}/Challange.md", "x") as afile:
        afile.write(baseMD.replace(
            "<day>", f"{i}").replace("<year>", f"{year}"))
