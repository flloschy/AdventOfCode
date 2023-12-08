import time

start = time.perf_counter()
####
content = open("./2023/Day1/input.txt", "r").read().splitlines()


def getDigits(x):
    # inspiration taken by github/BlackDemonFire
    nums = [
        ("one", "o1e"), ("two", "t2o"), ("three", "t3e"),
        ("four", "f4r"), ("five", "f5e"), ("six", "s6x"),
        ("seven", "s7n"), ("eight", "e8t"), ("nine", "n9e"),
    ]

    for s, n in nums:
        x = x.replace(s, n)
    return x


def f(x):
    x = getDigits(x)
    digits = [ch for ch in list(x) if ch.isdigit()]
    return int(f"{digits[0]}{digits[-1]}")


numbers = [f(line) for line in content]
print(sum(numbers))


###
print(f"Time Taken: {time.perf_counter()-start}s")
