import os
year = 2021

if not os.path.exists(f"./{year}"):
    os.mkdir(f"./{year}")
for i in range(1, 26):
    os.mkdir(f"./{year}/Day{i}")
    open(f"./{year}/Day{i}/input.txt", "x")
    with open(f"./{year}/Day{i}/a.py", "x") as afile:
        afile.write("""import time\nstart = time.perf_counter()\n###\n\n###\nprint(f"Time Taken: {time.perf_counter()-start}s")""")
    with open(f"./{year}/Day{i}/b.py", "x") as afile:
        afile.write("""import time\nstart = time.perf_counter()\n###\n\n###\nprint(f"Time Taken: {time.perf_counter()-start}s")""")
    open(f"./{year}/Day{i}/Challange.md", "x")