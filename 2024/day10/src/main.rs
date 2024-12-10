
use std::{fs::read_to_string, vec};

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

struct QueueItem {
    x: i32,
    y: i32,
    v: u8
}

fn task1() -> i32 {
    let mut result:i32 = 0;
    let map: Vec<Vec<u8>> = read_lines()
        .iter()
        .map(|row| row
            .split("")
            .filter(|column| column != &"")
            .map(|value| value.parse().unwrap())
            .collect())
        .collect();

    for (y, row) in map.iter().enumerate() {
        for (x, value) in row.iter().enumerate() {
            if value != &0 {continue;}

            let mut to_visit:Vec<QueueItem> = vec![QueueItem {x:x.try_into().unwrap(), y:y.try_into().unwrap(), v: value.to_owned()}];
            let mut visited:Vec<[i32; 2]> = vec![]; 

            while let Some(visit) = to_visit.pop() {
                let offsets = [
                    [visit.x, visit.y - 1],
                    [visit.x - 1, visit.y], [visit.x + 1, visit.y],
                    [visit.x, visit.y + 1]
                ];
                for [pos_x, pos_y] in offsets {
                    if pos_x < 0 || pos_x > (map.len() - 1) as i32 {continue;}
                    if pos_y < 0 || pos_y > (map[0].len() - 1) as i32 {continue;}
                    let this_value = map[pos_y as usize][pos_x as usize];
                    if this_value != visit.v + 1 {continue;}
                    if this_value == 9 && !visited.contains(&[pos_x, pos_y]){
                        result+=1;
                        visited.push([pos_x, pos_y]);
                    }
                    to_visit.push(QueueItem {x: pos_x, y: pos_y, v: this_value});
                }
            }

        }
    }
    return result;
}
fn task2() -> i32 {
    let mut result:i32 = 0;
    let map: Vec<Vec<u8>> = read_lines()
        .iter()
        .map(|row| row
            .split("")
            .filter(|column| column != &"")
            .map(|value| value.parse().unwrap())
            .collect())
        .collect();

    for (y, row) in map.iter().enumerate() {
        for (x, value) in row.iter().enumerate() {
            if value != &0 {continue;}

            let mut to_visit:Vec<QueueItem> = vec![QueueItem {x:x.try_into().unwrap(), y:y.try_into().unwrap(), v: value.to_owned()}];
    
            while let Some(visit) = to_visit.pop() {
                let offsets = [
                    [visit.x, visit.y - 1],
                    [visit.x - 1, visit.y], [visit.x + 1, visit.y],
                    [visit.x, visit.y + 1]
                ];
                for [pos_x, pos_y] in offsets {
                    if pos_x < 0 || pos_x > (map.len() - 1) as i32 {continue;}
                    if pos_y < 0 || pos_y > (map[0].len() - 1) as i32 {continue;}
                    let this_value = map[pos_y as usize][pos_x as usize];
                    if this_value != visit.v + 1 {continue;}
                    if this_value == 9 {result+=1;}
                    to_visit.push(QueueItem {x: pos_x, y: pos_y, v: this_value});
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
