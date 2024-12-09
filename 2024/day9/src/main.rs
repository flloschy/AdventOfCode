use std::{fs::read_to_string};

fn read_lines() -> Vec<String> {
    read_to_string("input.txt")
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn task1() -> i64 {
    let mut result: i64 = 0;
    let mut id = 0;
    let mut toggle = true;
    let mut unpacked = vec![];
    for line in read_lines() {
        for char in line.split("") {
            if char.is_empty() {
                continue;
            }
            let int: i64 = char.parse().unwrap();
            if toggle {
                for _ in 0..int {
                    unpacked.push(id);
                }
                id += 1;
            } else {
                for _ in 0..int {
                    unpacked.push(-1);
                }
            }

            toggle = !toggle;
        }
    }
    loop {
        let mut last_index: i64 = -1;
        let mut first_index: i64 = -1;
        for (index, value) in unpacked.clone().iter().enumerate() {
            if last_index == -1 && *value == -1 {
                last_index = index as i64;
            }
            if value != &-1 {
                first_index = index as i64;
            }
        }
        if last_index - 1 == first_index {
            break;
        }
        let tmp: i64 = unpacked[last_index as usize];
        unpacked[last_index as usize] = unpacked[first_index as usize];
        unpacked[first_index as usize] = tmp;
    }

    for (index, x) in unpacked.iter().enumerate() {
        if *x == -1 {
            break;
        }
        result += index as i64 * x;
    }

    return result;
}

fn task2() -> i64 {
    let mut result: i64 = 0;
    let mut id = 0;
    let mut toggle = true;
    let mut unpacked = vec![];
    let mut max_id = 0;
    for line in read_lines() {
        for char in line.split("") {
            if char.is_empty() {
                continue;
            }
            let int: i64 = char.parse().unwrap();
            if toggle {
                for _ in 0..int {
                    unpacked.push(id);
                }
                max_id = id;
                id += 1;
            } else {
                for _ in 0..int {
                    unpacked.push(-1);
                }
            }

            toggle = !toggle;
        }
    }

    while max_id >= 0 {
        let mut reversed = unpacked.clone();
        reversed.reverse();

        let mut block_start = 0;
        let mut block_length = 0;
        let mut block_found = false;
        for (index, block) in reversed.iter().enumerate() {
            if block == &max_id && !block_found {
                block_found = true;
                block_start = reversed.len() - 1 - index;
            } else if block == &max_id && block_found {
                block_start = reversed.len() - 1 - index;
                block_length += 1
            }
            if block_found && block != &max_id {
                let mut empty_start = 0;
                let mut empty_length = 0;
                let mut empty_found = false;
                for (index2, empty) in unpacked.clone().iter().enumerate() {
                    if index2 > block_start + block_length {break;}
                    if empty == &-1 && !empty_found {
                        empty_found = true;
                        empty_start = index2;
                    } else if empty == &-1 && empty_found {
                        empty_length += 1;
                    } else if empty != &-1 && empty_found {
                        if empty_length >= block_length {
                            for offset in 0..block_length+1 {
                                unpacked[block_start + offset] = -1;
                                unpacked[empty_start + offset] = max_id;
                            }
                            break;
                        }
                        empty_start = 0;
                        empty_length = 0;
                        empty_found = false;
                    }
                }
                break;
            }

        }

        max_id -= 1;
    }


    let mut index = -1;
    for x in unpacked {
        index += 1;
        if x == -1 {
            continue;
        }
        result += index * x;

    }

    return result;
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
