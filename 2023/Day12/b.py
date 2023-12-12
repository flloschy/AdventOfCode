import itertools
from multiprocessing import Pool
import time
####


def process_line(args):
    i, [string, numbers] = args
    questionMarks = string.count("?") + 1
    goalAmountOfOnes = sum(numbers) - string.count("#") + 1
    string = string.replace(".", "0").replace("#", "1").replace("?", '3')
    string = [int(char) for char in string]
    validCombinations = 0
    for combination in itertools.combinations(range(questionMarks), goalAmountOfOnes):
        line = [0] * questionMarks
        for index in combination:
            line[index] = 1
        if [len(list(group)) for key, group in itertools.groupby(line.pop(0) if char == 3 else char for char in string) if key == 1] == numbers:
            validCombinations += 1
    return validCombinations

def main():
    start = time.perf_counter()
    content = [["." + "?".join((line.split(" ")[0])*5) + ".", [int(num) for num in line.split(" ")[1].split(",")]*5] for line in open("./2023/Day12/input.txt", "r").read().splitlines()]

    with Pool() as pool:
        results = pool.map(process_line, enumerate(content))

    print(sum(results))
    print(f"Time Taken: {time.perf_counter()-start}s")

if __name__ == '__main__':
    main()

###

