
use std::{fs::read_to_string, vec};

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

#[derive(PartialEq, Copy, Clone)]
enum MapType {
    Empty,
    Obstacle,
    Visited
}
#[derive(PartialEq, Copy, Clone)]
enum WalkState {
    Up,
    Right,
    Down,
    Left
}
#[derive(PartialEq, Copy, Clone)]
struct Guard {
    x: i32,
    y: i32,
    state: WalkState
}
#[derive(PartialEq, Copy, Clone)]
struct Result {
    out_of_bounds: bool,
    new_guard: Guard,
}

fn walk(map: &Vec<Vec<MapType>>, guard: Guard) -> Result {
    let x: i32 = guard.x +
        if guard.state == WalkState::Right {1}
        else if guard.state == WalkState::Left {-1}
        else {0};
    let y: i32 = guard.y +
        if guard.state == WalkState::Down {1}
        else if guard.state == WalkState::Up {-1}
        else {0};
    if x < 0 || x > (map.len()-1).try_into().unwrap() || y < 0 || y > (map.len()-2).try_into().unwrap() {
        return Result {
            out_of_bounds: true,
            new_guard: Guard {
                x,
                y,
                state: WalkState::Down
            }
        }
    }
    let can_walk = map[y as usize][x as usize] != MapType::Obstacle;
    let state = if can_walk {guard.state}
                           else if guard.state == WalkState::Up {WalkState::Right}
                           else if guard.state == WalkState::Right {WalkState::Down}
                           else if guard.state == WalkState::Down {WalkState::Left}
                           else {WalkState::Up};

    return Result {
        out_of_bounds: false,
        new_guard: Guard {
            x: if can_walk {x} else {guard.x},
            y: if can_walk {y} else {guard.y},
            state
        }
    };
}

fn task1() -> i32 {
    let mut result:i32 = 1;
    let mut map: Vec<Vec<MapType>> = vec![vec![]];
    let mut y: i32 = 0;
    let mut guard = Guard {x:0, y:0, state: WalkState::Up};
    for line in read_lines() {
        let mut x: i32 = 0;
        map.push(vec![]);
        for char in line.split("") {
            map[y as usize].push(if char == "#" {MapType::Obstacle}
            else if char == "^" {guard.x = x; guard.y = y; MapType::Visited}
            else {MapType::Empty});
            x += 1;
        }
        y += 1;
    }
    loop {
        let state = walk(&map, guard);
        if state.out_of_bounds {break;}
        guard = state.new_guard;
        if map[guard.y as usize][guard.x as usize] != MapType::Visited {result+=1;}
        map[guard.y as usize][guard.x as usize] = MapType::Visited;
        
    }

    return result;
}
fn task2() -> i32 {
    let mut result:i32 = 0;
    let mut base_map: Vec<Vec<MapType>> = vec![vec![]];
    let mut y: i32 = 0;
    let mut guard = Guard {x:0, y:0, state: WalkState::Up};
    for line in read_lines() {
        let mut x: i32 = 0;
        base_map.push(vec![]);
        for char in line.split("") {
            base_map[y as usize].push(if char == "#" {MapType::Obstacle}
            else if char == "^" {guard.x = x; guard.y = y; MapType::Visited}
            else {MapType::Empty});
            x += 1;
        }
        y += 1;
    }
    let start_guard = guard.clone();
    loop {
        let state = walk(&base_map, guard);
        if state.out_of_bounds {break;}
        guard = state.new_guard;
        base_map[guard.y as usize][guard.x as usize] = MapType::Visited;
    }


    for x in 0..base_map.len()-1 {
        for y in 0..base_map.len() {
            if base_map[x][y] != MapType::Visited {continue;}
            let mut test_map = base_map.clone();
            test_map[x][y] = MapType::Obstacle;
            let mut visited: Vec<Guard> = vec![];
            guard = start_guard.clone();
            let mut is_loop = false;
            loop {
                let state = walk(&test_map, guard);
                if state.out_of_bounds {break;}
                guard = state.new_guard;
                if visited.contains(&guard) {is_loop=true; break;}
                visited.push(guard);
            }
            if is_loop {result+=1};
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
