
use std::fs::read_to_string;
use regex::Regex;

// fn read_lines() -> Vec<String> {
//     read_to_string("input.txt") 
//         .unwrap()
//         .lines()
//         .map(String::from)
//         .collect()
// }

fn task1() -> i32 {
    let mut result:i32 = 0;
    let re = Regex::new(r"mul\(\d*,\d*\)").unwrap();
    let code = read_to_string("input.txt").unwrap();
    
    for match_ in re.captures_iter(&code) {
        let value= match_.get(0).map(|u| u.as_str()).unwrap();
        let numbers: Vec<i32> = value.replace("mul(", "").replace(")", "").split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        result += numbers[0] * numbers[1];
    }
    return result;
}
fn task2() -> i32 {
    let mut result:i32 = 0;
    let re = Regex::new(r"mul\(\d*,\d*\)|do\(\)|don't\(\)").unwrap();
    let code = read_to_string("input.txt").unwrap();
    
    let mut do_it = true;

    for match_ in re.captures_iter(&code) {
        let value= match_.get(0).map(|u| u.as_str()).unwrap();
        if value == "don't()" {do_it = false;}
        else if value == "do()" {do_it = true;}
        else if do_it {
            let numbers: Vec<i32> = value.replace("mul(", "").replace(")", "").split(",").map(|x| x.parse::<i32>().unwrap()).collect();
            result += numbers[0] * numbers[1];
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
