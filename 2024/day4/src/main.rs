
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
    let lines = read_lines();

    for frame_y in 0..lines.len() {
        for frame_x in 0..lines[frame_y].len() {
            fn valid(x: Vec<String>) -> bool {
                return x.join("") == "XMAS" || x.join("") == "SAMX";
            }

            // horizontal
            if frame_x < lines[frame_y].len()-3 {
                if valid(lines[frame_y].get(frame_x..(frame_x+4)).unwrap().split("").map(|f| f.to_string()).collect()) {
                    result+=1
                }
            }
            // vertical
            if frame_y < lines.len()-3 {
                if valid(lines.get(frame_y..(frame_y+4)).unwrap().into_iter().map(|f: &String| f.chars().nth(frame_x).unwrap().to_string()).collect()) {
                    result+=1
                }
            }

            if frame_x < lines[frame_y].len()-3 && frame_y < lines.len()-3 {
                // right diagonal (\)
                if valid(lines.get(frame_y..(frame_y+4)).unwrap().into_iter().enumerate().map(|(i, f)| f.chars().nth(frame_x + i).unwrap().to_string()).collect()) {
                    result+=1
                }
                // left diagonal (/)
                if valid(lines.get(frame_y..(frame_y+4)).unwrap().into_iter().enumerate().map(|(i, f)| f.chars().nth(frame_x + 3 - i).unwrap().to_string()).collect()) {
                    result+=1
                }
            }
        }
    }

    return result;
}
fn task2() -> i32 {
    let mut result:i32 = 0;
    let lines = read_lines();

    for frame_y in 0..lines.len()-2 {
        for frame_x in 0..lines[frame_y].len()-2 {
            fn valid(x: Vec<String>) -> bool {
                return x.join("") == "MAS" || x.join("") == "SAM";
            }
            if valid(lines.get(frame_y..(frame_y+3)).unwrap().into_iter().enumerate().map(|(i, f)| f.chars().nth(frame_x + i).unwrap().to_string()).collect()) &&  valid(lines.get(frame_y..(frame_y+3)).unwrap().into_iter().enumerate().map(|(i, f)| f.chars().nth(frame_x + 2 - i).unwrap().to_string()).collect()) {
                result+=1
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
