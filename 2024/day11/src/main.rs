use std::collections::HashMap;
use std::fs::read_to_string;
use std::result;
use std::thread::{self, JoinHandle};
use std::sync::{Arc, Mutex};

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn task1() -> usize {
    let mut line:Vec<i64> = read_lines().get(0).unwrap().split(" ").filter(|f| !f.is_empty()).map(|f| f.parse().unwrap()).collect();


    for _ in 0..25 {
        let mut new_line:Vec<i64> = vec![];
        for stone in line.iter()     {
            if stone == &0  {
                new_line.push(1);
                continue;
            }
            let str_stone = stone.to_string();
            if str_stone.len() % 2 == 0 {
                let half = str_stone.len() / 2;
                let str_split_stone:Vec<&str> = str_stone.split("").filter(|f| !f.is_empty()).collect();
                let first_half:i64 = str_split_stone.get(0..half).unwrap().join("").parse().unwrap();
                let second_half:i64 = str_split_stone.get(half..str_stone.len()).unwrap().join("").parse().unwrap();
            
                new_line.push(first_half);
                new_line.push(second_half);
                continue;
            }
            new_line.push(stone * 2024);
        }
        line = new_line;
    }


    return line.len();
}



fn task2() -> u128 {
    let mut results: u128 = 0;
    let line:Vec<u128> = read_lines().first().unwrap().split(" ").map(|f| f.parse().unwrap()).collect();
    let mut cache: HashMap<[u128; 2], u128> = HashMap::new();
    fn step(value:u128, to_step:u128, counter:u128, cache: &mut HashMap<[u128; 2], u128>) -> u128 {
        if to_step == 0 {
            return counter + 1;
        }
        if let Some(hit) = (*cache).get(&[value, to_step]) {
            return hit.to_owned();
        }
        if value == 0 {
            let resolution: u128 = step(1, to_step-1, counter, cache);
            *cache.entry([value, to_step]).or_insert(resolution) = resolution;
            return resolution
        }
        let str_stone = value.to_string();
        if str_stone.len() % 2 == 0 {
            let half = str_stone.len() / 2;
            let first_half:u128 = str_stone.get(0..half).unwrap().parse().unwrap();
            let second_half:u128 = str_stone.get(half..str_stone.len()).unwrap().parse().unwrap();
            
            let mut resolution: u128 = step(first_half, to_step-1, counter, cache);
            // *cache.entry([first_half, to_step]).or_insert(first_resolution) = first_resolution;

            resolution += step(second_half, to_step-1, counter, cache);
            *cache.entry([value, to_step]).or_insert(resolution) = resolution;

            // *cache.entry([value, to_step]).or_insert(resolution) = resolution;
            return resolution
        }
        let resolution: u128 = step(value*2024, to_step-1, counter, cache);
        *cache.entry([value, to_step]).or_insert(resolution) = resolution;
        return resolution;
    }
    for stone in line {
        results += step(stone, 75, 0, &mut cache)
    }
    return  results;

    
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
