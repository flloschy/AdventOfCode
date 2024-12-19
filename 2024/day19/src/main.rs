
use std::{cmp::min, collections::{HashMap, HashSet}, fs::read_to_string, sync::{Arc, Mutex}, thread};

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn recursion(possible: &Vec<String>, current: String, target: String, count: &mut u32) -> bool {
    if current == target { return true;}
    if *count > 1000 {return false;}
    if current.len() > target.len() {return false;}
    if current.len() == target.len() && current != target {return false;}


    let filtered= possible.iter().filter(|p| target.get(current.len()..min(target.len(), current.len()+p.len())).unwrap() == p.to_string()).map(|f| f.to_string()).collect::<Vec<String>>();
    // filtered.sort_by(|a, b| if a.len() > b.len() {Ordering::Greater} else if b.len() > a.len() {Ordering::Less} else {Ordering::Equal});
    *count += 1;
    for f in filtered {
        let new_current = format!("{current}{f}");
        // dbg!(&new_current);
        if recursion(possible, new_current, target.clone(), count ) {return true;}
    }
    
    return  false;
}

struct Identifier {
    v: String,
    depth: i32
}

fn recursion2(possible: &Vec<String>, current: String, target: String, depth: i32, cache: &mut HashMap<String, u64>) -> u64 {
    if current == target { return 1;}
    let key = format!("{}{}", current, depth);
    if cache.contains_key(&key) {
        return cache.get(&key).unwrap().to_owned();
    }
    // if *count > 5000 {return 0;}
    if current.len() >= target.len() {return 0;}
    if current.len() == target.len() && current != target {return 0;}


    let filtered= possible
        .iter()
        .filter(|p| target
            .get(
                current.len()..min(
                    target.len(), 
                    current.len()+p.len()
                ))
            .unwrap() == p.to_string())
        .map(|f| f.to_string())
        .collect::<Vec<String>>();
    let mut result = 0;
    for f in filtered {
        let new_current = format!("{current}{f}");
        result += recursion2(possible, new_current, target.clone(), depth+1, cache);
    }
    cache.entry(key).or_insert(result);
    return  result;
}


fn task1() -> i32 {
    let mut result:i32 = 0;
    let lines = read_lines();
    let available = &lines[0].split(", ").map(|f| f.to_string());
    let targets = lines.get(2..).unwrap().to_vec();
    
    for target in targets {
        let possible = available
            .clone()
            .filter(|t| {
                for char in t.split("") {
                    if !target.contains(char) {return false;}
                }
                return true;
            })
            .collect::<Vec<String>>();

        result += if recursion(&possible, "".to_string(), target.clone(), &mut 0) {1} else {0};
    }

    return result;
}
fn task2() -> u64 {
    let lines = read_lines();
    let available = &lines[0].split(", ").map(|f| f.to_string());
    let targets = lines.get(2..).unwrap().to_vec();
    
    let counter: Arc<Mutex<u64>> = std::sync::Arc::new(Mutex::new(0));
    let mut threads = vec![];

    for target in targets {
        let possible = available
            .clone()
            .filter(|t| {
                for char in t.split("") {
                    if !target.contains(char) {return false;}
                }
                return true;
            })
            .collect::<Vec<String>>();
        let mut cache: HashMap<String, u64> = HashMap::new();
        let counter = Arc::clone(&counter);
        threads.push(thread::spawn(move || {
            let result = recursion2(&possible, "".to_string(), target.clone(), 0, &mut cache);
            let mut num = counter.lock().unwrap();
            // println!("thread: {target}\n\t{num}");
            *num += result;
        }));


        // result += recursion2(&possible, "".to_string(), target.clone(), &mut 0);
    }
    println!("started {} threrads", threads.len());
    for thrd in threads {
        thrd.join().unwrap();
    }

    return *counter.lock().unwrap();
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
