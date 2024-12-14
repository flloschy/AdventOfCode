
use core::num;
use std::{fs::read_to_string, result};

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn custom_mod(x: i32, max: i32) -> i32{
    let n = x % max;
    if n < 0 {return max + n;}
    return n;
}

#[derive(Debug, Clone)]
struct Robot {
    x: i32,
    y: i32,
    vx: i32,
    vy: i32
}
fn task1() -> usize {
    let lines = read_lines();
    let robots = lines
        .iter()
        .map(|line| {
            let numbers = line
                .split(" ")
                .map(|value| value
                    .split("=")
                    .collect::<Vec<&str>>()[1]
                    .split(",")
                    .map(|f| f.parse::<i32>().unwrap())
                    .collect::<Vec<i32>>()
                )                
                .collect::<Vec<Vec<i32>>>();

            return Robot {x: numbers[0][0], y: numbers[0][1], vx: numbers[1][0], vy: numbers[1][1]};
            }
        )
        .map(|robot| {
            return Robot { x: custom_mod(robot.x + robot.vx * 100, 101), y: custom_mod(robot.y + robot.vy * 100, 103), vx: robot.vx, vy: robot.vy};
        });
    return robots.clone().filter(|r| r.x < 50 && r.y < 51).count() *
            robots.clone().filter(|r| r.x < 50 && r.y > 51).count() *
            robots.clone().filter(|r| r.x > 50 && r.y < 51).count() *
            robots.clone().filter(|r| r.x > 50 && r.y > 51).count();
}
fn task2() -> usize {
    let lines = read_lines();
    let mut robots:Vec<Robot> = lines
        .iter()
        .map(|line| {
            let numbers = line
                .split(" ")
                .map(|value| value
                    .split("=")
                    .collect::<Vec<&str>>()[1]
                    .split(",")
                    .map(|f| f.parse::<i32>().unwrap())
                    .collect::<Vec<i32>>()
                )                
                .collect::<Vec<Vec<i32>>>();

            return Robot {x: numbers[0][0], y: numbers[0][1], vx: numbers[1][0], vy: numbers[1][1]};
            }
        ).collect();

    let mut results = 0;
    let mut running = true;
    while running {
        results += 1;
        robots = robots.iter().map(|r| Robot { x: custom_mod(r.x + r.vx, 101), y: custom_mod(r.y + r.vy, 103), vx: r.vx, vy: r.vy}).collect();

        for y in 40..60 {
            if robots.clone().iter().filter(|r| r.y == y).count() >= 31 {
                for x in 40..60 {
                    running = true;
                    if robots.clone().iter().filter(|r| r.x == x).count() >= 31 {
                        running = false;
                        break;
                    }
                }
                
                break;
            }
        }
        dbg!(results);
    };
    return results;
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
