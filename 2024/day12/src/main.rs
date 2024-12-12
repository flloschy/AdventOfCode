
use std::{collections::{btree_map::IterMut, HashMap}, fs::{read_to_string, Permissions}};

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn task1() -> usize {
    let mut result:usize = 0;
    let map:Vec<Vec<String>> = read_lines().iter().map(|line| line.split("").map(|f| f.to_string()).filter(|f| !f.is_empty()).collect()).collect();
    let mut groups: Vec<Vec<[usize; 2]>> = vec![];
    let mut visited: Vec<[usize; 2]> = vec![];

    for (y, row) in map.iter().enumerate() {
        for (x, plant) in row.iter().enumerate() {
            if visited.contains(&[x, y]) {continue;}
            let mut collective: Vec<[usize; 2]> = vec![];
            let mut queue: Vec<[usize; 2]> = vec![[x, y]];
            while let Some([x2, y2]) = queue.pop() {
                if visited.contains(&[x2, y2]) {continue;}
                collective.push([x2, y2]);
                visited.push([x2, y2]);
                for [ox, oy] in [[-1, 0], [1, 0], [0, -1], [0, 1]] {
                    let pos_x = (x2 as i32 + ox) as usize;
                    if pos_x > map[0].len() - 1 {continue;}
                    
                    let pos_y = (y2 as i32 + oy) as usize;
                    if pos_y > map.len() - 1 {continue;}

                    let pos = [pos_x, pos_y];
                    if collective.contains(&pos) {continue;}
                    if map[pos_y][pos_x] == *plant {queue.push(pos);}
                }
            }
            groups.push(collective);
        }
    }
    

    for collective in groups {
        let area = collective.len();
        let mut perimeter = 0;
        for [x, y] in collective.clone() {
            for [ox, oy] in [[-1, 0], [1, 0], [0, -1], [0, 1]] {
                let pos_x = (x as i32 + ox);
                if pos_x > map[0].len() as i32  {continue;}

                let pos_y = (y as i32 + oy);
                if pos_y > map.len() as i32  {continue;}

                let pos = [pos_x as usize, pos_y as usize];
                
                if pos_x < 0 || pos_x >= map[0].len() as i32 {perimeter += 1;}
                else if pos_y < 0 || pos_y >= map.len() as i32{perimeter += 1;}
                else if pos_x < map[0].len() as i32 &&
                        pos_y < map.len() as i32 &&
                        !collective.contains(&pos) {perimeter += 1;}
            }
        }
        // println!("{area}*{perimeter}={}", area * perimeter);
        result += area * perimeter

    }

    return result;
}
fn task2() -> i32 {
    let mut result:i32 = 0;
    let map:Vec<Vec<String>> = read_lines().iter().map(|line| line.split("").map(|f| f.to_string()).filter(|f| !f.is_empty()).collect()).collect();
    let mut groups: Vec<Vec<[usize; 2]>> = vec![];
    let mut visited: Vec<[usize; 2]> = vec![];

    for (y, row) in map.iter().enumerate() {
        for (x, plant) in row.iter().enumerate() {
            if visited.contains(&[x, y]) {continue;}
            let mut collective: Vec<[usize; 2]> = vec![];
            let mut queue: Vec<[usize; 2]> = vec![[x, y]];
            while let Some([x2, y2]) = queue.pop() {
                if visited.contains(&[x2, y2]) {continue;}
                collective.push([x2, y2]);
                visited.push([x2, y2]);
                for [ox, oy] in [[-1, 0], [1, 0], [0, -1], [0, 1]] {
                    let pos_x = (x2 as i32 + ox) as usize;
                    if pos_x > map[0].len() - 1 {continue;}
                    
                    let pos_y = (y2 as i32 + oy) as usize;
                    if pos_y > map.len() - 1 {continue;}

                    let pos = [pos_x, pos_y];
                    if collective.contains(&pos) {continue;}
                    if map[pos_y][pos_x] == *plant {queue.push(pos);}
                }
            }
            groups.push(collective);
        }
    }
    

    for collective in groups {
        let area = collective.len() as i32;
        let mut sides: i32 = 0;

        for [x, y] in collective.clone() {
            let bottom_right_corner = ![[x+1, y],[x, y+1]].map(|pos| !collective.contains(&pos)).contains(&false);
            let bottom_left_corner = ![[x-1, y],[x, y+1]].map(|pos| !collective.contains(&pos)).contains(&false);
            let top_right_corner = ![[x+1, y],[x, y-1]].map(|pos| !collective.contains(&pos)).contains(&false);
            let top_left_corner = ![[x-1, y],[x, y-1]].map(|pos| !collective.contains(&pos)).contains(&false);
        
            let bottom_right_inner_corner = collective.contains(&[x+1, y]) && collective.contains(&[x, y+1]) && !collective.contains(&[x+1,y+1]);
            let bottom_left_inner_corner = collective.contains(&[x-1, y]) && collective.contains(&[x, y+1]) && !collective.contains(&[x-1,y+1]);
            let top_right_inner_corner = collective.contains(&[x+1, y]) && collective.contains(&[x, y-1]) && !collective.contains(&[x+1,y-1]);
            let top_left_inner_corner = collective.contains(&[x-1, y]) && collective.contains(&[x, y-1]) && !collective.contains(&[x-1,y-1]);

            
            if bottom_right_inner_corner {sides += 1;}
            if bottom_left_inner_corner {sides += 1;}
            if top_right_inner_corner {sides += 1;}
            if top_left_inner_corner {sides += 1;}
            if bottom_right_corner {sides += 1;}
            if bottom_left_corner {sides += 1;}
            if top_right_corner {sides += 1;}
            if top_left_corner {sides += 1;}

        }
        result += area * sides

    }

    return result;
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
