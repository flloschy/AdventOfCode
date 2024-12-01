import os
year = 2024

baseCode = """
use std::fs::read_to_string;

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn task1() -> i32 {
    let result:i32 = 0;
    for line in read_lines() {
        println!("{}", line);
    }
    return result;
}
fn task2() -> i32 {
    let result:i32 = 0;
    for line in read_lines() {
        println!("{}", line);
    }
    return result;
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
"""

baseMD = """
# Day <day>
### `- title -`
#### Part 1
> - [My](https://github.com/flloschy) answer was `- answer -` . ([Here](https://github.com/flloschy/AdventOfCode/blob/main/<year>/day<day>/src/main.rs))

#### Part 2
> - [My](https://github.com/flloschy) answer was `- answer -` . ([Here](https://github.com/flloschy/AdventOfCode/blob/main/<year>/day<day>/src/main.rs))

###### [Source](https://adventofcode.com/<year>/day/<day>/)
"""


if not os.path.exists(f"./{year}"):
    os.mkdir(f"./{year}")

# for i in range(1, 26):

i = 2
# os.mkdir(f"./{year}/day{i}")
os.system(f"cargo new {os.path.abspath(f'./{year}/day{i}')}")
open(f"./{year}/day{i}/input.txt", "x")
with open(f"./{year}/day{i}/src/main.rs", "w") as afile:
    afile.write(baseCode)
with open(f"./{year}/day{i}/Challange.md", "x") as afile:
    afile.write(baseMD
        .replace("<day>", f"{i}")
        .replace("<year>", f"{year}"))
