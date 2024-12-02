
use std::{fs::read_to_string};

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
        let reports: Vec<&str> = line.split(" ").collect();
        let mut state: i8 = 0; // 0 = undefined; 1 = decreasing; 2 = increasing
        let mut valid = true;
        for i in 0..=reports.len()-2 {
            let a: i32 = reports[i].parse().unwrap();
            let b: i32 = reports[i+1].parse().unwrap();
            
            let delta = a - b;
            
            if delta.abs() > 3 || delta == 0 {
                valid = false;
                break;
            } 

            let direction: i8 = if delta < 0 {1} else {2} as i8;
            if state == 0 {
                state = direction;
            } else if state != direction{
                valid = false;
                break;
            }
        }
        if valid {result += 1;}
    }
    return result;
}

fn task2() -> i32 {
    let mut result:i32 = 0;
    let lines = read_lines();
    for line in lines {
        let reports: Vec<&str> = line.split(" ").collect();
        let mut state: i8 = 0; // 0 = undefined; 1 = decreasing; 2 = increasing
        let mut valid = true;
        for i in 0..=reports.len()-2 {
            let a: i32 = reports[i].parse().unwrap();
            let b: i32 = reports[i+1].parse().unwrap();
            let delta = a - b;
            

            let direction: i8 = if delta < 0 {1} else {2} as i8;
            if state == 0 {
                state = direction;
            } else if state != direction || delta.abs() > 3 || delta == 0 {
                let mut are_any_valid = false;
                for to_remove in 0..=(reports.len()-1) {
                    let mut reports2: Vec<&str> = line.split(" ").collect();
                    reports2.remove(to_remove);
                    let mut state2: i8 = 0; // 0 = undefined; 1 = decreasing; 2 = increasing
                    let mut valid2 = true;
                    for i2 in 0..=reports2.len()-2 {
                        let a2: i32 = reports2[i2].parse().unwrap();
                        let b2: i32 = reports2[i2+1].parse().unwrap();
                        let delta2 = a2 - b2;
                        
                        let direction2: i8 = if delta2 < 0 {1} else {2} as i8;
                        if state2 == 0 {
                            state2 = direction2;
                        }
                        if state2 != direction2 || delta2.abs() > 3 || delta2 == 0 {
                            valid2 = false;
                            break;
                        }
                    }
                    if valid2 {are_any_valid = true}
                }
                if !are_any_valid {valid = false}
            }
        }
        if valid {result += 1;}
    }
    return result;
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
