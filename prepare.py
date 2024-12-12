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
    let mut result:i32 = 0;
    for line in read_lines() {
        println!("{}", line);
    }
    return result;
}
fn task2() -> i32 {
    let mut result:i32 = 0;
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

if not os.path.exists(f"./{year}"):
    os.mkdir(f"./{year}")

# for i in range(1, 26):

i = 12
# os.mkdir(f"./{year}/day{i}")
os.system(f"cargo new {os.path.abspath(f'./{year}/day{i}')}")
open(f"./{year}/day{i}/input.txt", "x")
with open(f"./{year}/day{i}/src/main.rs", "w") as afile:
    afile.write(baseCode)