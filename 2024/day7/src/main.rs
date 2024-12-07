use std::{fs::read_to_string};
use bitvec::{prelude::*};

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn task1() -> u64 {
    let mut result:u64 = 0;
    for line in read_lines() {
        let splitted: Vec<String> = line.split(": ").map(|f| f.to_string()).collect();
        let target:u64 = splitted[0].parse().unwrap();
        let values:Vec<u64> = splitted[1].split(" ").map(|f| f.parse::<u64>().unwrap()).collect();
        if values.len() == 2 {
            if (values[0] + values[1]) == target || (values[0] * values[1]) == target {result += target;}
        } else {
            for int in 0..(2_u64).pow(values.len() as u32) {
                let bit_array = int.view_bits::<Lsb0>();
                let mut val = values[0];
                for index in 0..values.len()-1 {
                    let multiply = bit_array[index];
                    let b = values[index+1];
                    if multiply {val *= b;}
                    else {val += b;}
                }
                if val == target {
                    result += target;
                    break;
                }
            }
        }
    }  
    return result;
}

fn task2() -> u64 {
    let mut result:u64 = 0;
    for line in read_lines() {
        let splitted: Vec<String> = line.split(": ").map(|f| f.to_string()).collect();
        let target:u64 = splitted[0].parse().unwrap();
        let values:Vec<u64> = splitted[1].split(" ").map(|f| f.parse::<u64>().unwrap()).collect();
        let mut operations: Vec<u8> = vec![0;values.len()-1];
        loop {
            let mut value = values[0];
            for i in 0..values.len()-1 {
                let b = values[i+1];
                if operations[i] == 0 {
                    value += b;
                } else if operations[i] == 1 {
                    value *= b;
                } else {
                    value = format!("{}{}", value, b).parse().unwrap();
                }
            }

            if value == target {
                result += target;
                break;
            }
            if operations.iter().filter(|p| p.to_le() == 3_u8).collect::<Vec<&u8>>().len() == operations.len() {
                break;
            }
            operations[0] += 1;
            for index in 0..operations.len()-1 {
                if operations[index] > 3 {
                    operations[index] = 0;
                    operations[index + 1] += 1;
                } else {
                    break;
                }
            }
        }
    }  
    return result;
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
