use std::collections::HashMap;
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
    let mut rules: HashMap<String, Vec<String>> = HashMap::new();
    for line in read_lines() {
        if line.contains("|") {
            let values:Vec<&str> = line.split("|").collect();
            let value = values[0].to_string();
            let key = values[1].to_string();
            rules.entry(key).or_insert(vec![]).push(value);
        } else if line.contains(",") {
            let pages:Vec<String> = line.split(",").map(String::from).collect();
            let mut index = 0;
            let mut valid = true;
            for page in pages.iter() {
                let before = pages.get(0..index).unwrap().to_vec();
                if rules.contains_key(page) {
                    for rule in rules.get(page).unwrap() {
                        if line.contains(rule) && !before.contains(rule) {
                            valid = false;
                            break;
                        };
                    }
                }
                if !valid {
                    break;
                }
                index += 1;
            }
            if valid {
                result += pages.get(pages.len()/2).unwrap().parse::<i32>().unwrap();
            }
        }
    }
    return result;
}
fn task2() -> i32 {
    let mut result:i32 = 0;
    let mut rules: HashMap<String, Vec<String>> = HashMap::new();
    for line in read_lines() {
        if line.contains("|") {
            let values:Vec<&str> = line.split("|").collect();
            let value = values[0].to_string();
            let key = values[1].to_string();
            rules.entry(key).or_insert(vec![]).push(value);
        } else if line.contains(",") {
            let mut pages:Vec<String> = line.split(",").map(String::from).collect();
            let mut index = 0;
            let mut valid = true;
            for page in pages.iter() {
                let before = pages.get(0..index).unwrap().to_vec();
                if rules.contains_key(page) {
                    for rule in rules.get(page).unwrap() {
                        if line.contains(rule) && !before.contains(rule) {
                            valid = false;
                            break;
                        };
                    }
                }
                if !valid {
                    break;
                }
                index += 1;
            }
            if !valid {
                let mut new_vec: Vec<String> = vec![];
                new_vec.push(pages.pop().unwrap().to_string());
                while pages.len() != 0 {
                    let element = pages.pop().unwrap().to_string();
                    for i in 0..new_vec.len()+1 {
                        let mut tmp = new_vec.clone();
                        tmp.insert(i, element.clone());

                        let mut index2 = 0;
                        let mut valid2 = true;
                        for page in tmp.iter() {
                            let before = tmp.get(0..index2).unwrap().to_vec();
                            if rules.contains_key(page) {
                                for rule in rules.get(page).unwrap() {
                                    if tmp.contains(rule) && !before.contains(rule) {
                                        valid2 = false;
                                        break;
                                    };
                                }
                            }
                            if !valid2 {
                                break;
                            }
                            index2 += 1;
                        }
                        if valid2 {
                            new_vec.insert(i, element.clone());
                            break;
                        }
                    }
                }
                result += new_vec.get(new_vec.len()/2).unwrap().parse::<i32>().unwrap();
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
