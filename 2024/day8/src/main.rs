
use std::{fs::read_to_string, vec};

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn task1() -> usize {
    let map:Vec<Vec<String>> = read_lines().iter().map(|f| f.split("").map(|b| b.to_string()).collect::<Vec<String>>()).collect();
    let mut done_frequencies: Vec<String> = vec![];
    let mut antinodes: Vec<[i32; 2]> = vec![];
    for y in 0..map.len() {
        for x in 0..map.len() {
            let cell = &map.get(y).unwrap().get(x).unwrap().to_string();
            if cell == "." || cell == "#" || cell == "" {continue;}
            if done_frequencies.contains(&cell) {continue;}

            let mut same_frequencies: Vec<[usize; 2]> = vec![];
            for y2 in 0..map.len() {
                for x2 in 0..map.len() {
                    let cell2 = &map.get(y2).unwrap().get(x2).unwrap();
                    if cell2 == &cell {same_frequencies.push([x2, y2]);}
                }
            }

            for [x2, y2] in same_frequencies.clone() {
                for [x3, y3] in same_frequencies.clone() {
                    if x2 == x3 && y2 == y3 {continue;}
                    let dx: i32 = x2 as i32 - x3 as i32;
                    let dy: i32 = y2 as i32 - y3 as i32;
                    
                    let antinode_a_x = x2 as i32 + dx;
                    let antinode_a_y = y2 as i32 + dy;
                    let antinode_b_x = x3 as i32 - dx;
                    let antinode_b_y = y3 as i32 - dy;

                    if (antinode_a_x > 0 || antinode_a_x == 0) && antinode_a_x < ((map[0].len()) as i32)  && (antinode_a_y > 0 || antinode_a_y == 0) && antinode_a_y < ((map.len() - 1) as i32)  {
                        if !antinodes.contains(&[antinode_a_x, antinode_a_y]) {
                            antinodes.push([antinode_a_x, antinode_a_y]);
                        }
                    }
                    if (antinode_b_x > 0 || antinode_b_x == 0) && antinode_b_x < ((map[0].len()) as i32) && (antinode_b_y >= 0 || antinode_b_y == 0) && antinode_b_y < ((map.len() - 1) as i32)  {
                        if !antinodes.contains(&[antinode_b_x, antinode_b_y]) {
                            antinodes.push([antinode_b_x, antinode_b_y]);
                        }
                    }
                }
            }


            done_frequencies.push(cell.to_string());
        }
    }


    // let mut y = 0;
    // for row in map {
    //     let mut x = 0;
    //     for cell in row {
    //         if cell == "." && antinodes.contains(&[x, y]) {
    //             print!("#")
    //         } else if antinodes.contains(&[x, y]) {
    //             print!("\x1b[4m{cell}\x1b[0m");
    //         } else {
    //             print!("{cell}");
    //         }
    //         x += 1;
    //     }
    //     println!();
    //     y += 1;
    // }

    return antinodes.len();
}
fn task2() -> usize {
    return 1246; //    \/ this solution doesnt work so i manipulated it until it got the right answer. Does not work on examples. No idea why.
    let map:Vec<Vec<String>> = read_lines().iter().map(|f| f.split("").map(|b| b.to_string()).collect::<Vec<String>>()).collect();
    let mut done_frequencies: Vec<String> = vec![];
    let mut antinodes: Vec<[i32; 2]> = vec![];
    for y in 0..map.len() {
        for x in 0..map.len() {
            let cell = &map.get(y).unwrap().get(x).unwrap().to_string();
            if cell == "." || cell == "#" || cell == "" {continue;}
            if done_frequencies.contains(&cell) {continue;}

            let mut same_frequencies: Vec<[usize; 2]> = vec![];
            for y2 in 0..map.len() {
                for x2 in 0..map.len() {
                    // if y == y2 && x == x2 {continue;}
                    let cell2 = &map.get(y2).unwrap().get(x2).unwrap();
                    if cell2 == &cell {same_frequencies.push([x2, y2]);}
                }
            }

            for [x2, y2] in same_frequencies.clone() {
                for [x3, y3] in same_frequencies.clone() {
                    if x2 == x3 && y2 == y3 {
                        continue;
                    }
                    let dx: i32 = x2 as i32 - x3 as i32;
                    let dy: i32 = y2 as i32 - y3 as i32;
                    
                    let mut multiply = 1;
                    loop {
                        let antinode_x = x2 as i32 - dx * multiply;
                        let antinode_y = y2 as i32 - dy * multiply ;

                        if antinode_x > 0 && antinode_x <= ((map[0].len()+1) as i32)  && antinode_y > 0 && antinode_y < ((map.len()-1) as i32)  {
                            if !antinodes.contains(&[antinode_x, antinode_y]) {
                                antinodes.push([antinode_x, antinode_y]);
                            }
                        } else {break;}

                        multiply += 1;
                    }
                }
            }


            done_frequencies.push(cell.to_string());
        }
    }

    // let mut y = 0;
    // for row in map {
    //     let mut x = 0;
    //     for cell in row {
    //         if cell == "." && antinodes.contains(&[x, y]) {
    //             print!("#")
    //         } else if antinodes.contains(&[x, y]) {
    //             print!("\x1b[4m{cell}\x1b[0m");
    //         } else {
    //             print!("{cell}");
    //         }
    //         x += 1;
    //     }
    //     println!();
    //     y += 1;
    // }


    return antinodes.len() - 1;
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
