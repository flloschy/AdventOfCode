use std::{fs::read_to_string};

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
        
}

fn task1() -> i32 {
    let mut left: Vec<i32> = vec![];
    let mut right: Vec<i32> = vec![];
    for line in read_lines() {
        let values: Vec<_> = line.split("   ").collect();
        left.push(values[0].parse().unwrap());
        right.push(values[1].parse().unwrap());
    }
    left.sort();
    right.sort();

    let mut sum: i32 = 0;

    for i in 0..=left.len()-1 {
        sum += (left[i] - right[i]).abs();
    }

    return sum;
}
fn task2() -> i32 {
    let mut left: Vec<i32> = vec![];
    let mut right: Vec<i32> = vec![];
    for line in read_lines() {
        let values: Vec<_> = line.split("   ").collect();
        left.push(values[0].parse().unwrap());
        right.push(values[1].parse().unwrap());
    }
    left.sort();
    right.sort();

    let mut sum = 0;
    for i in 0..=left.len()-1 {
        sum += left[i] * right.iter().filter(|&n| *n == left[i]).count() as i32;
    }

    return sum;
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
