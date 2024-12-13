
use std::fs::read_to_string;

fn read_lines() -> Vec<String> {
    read_to_string("input.txt") 
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}


struct Machine {
    a: [f64; 2],
    b: [f64; 2],
    p: [f64; 2],
}

fn task1() -> i32 {
    let mut result:i32 = 0;
    let mut machine = Machine {a:[0.0,0.0], b:[0.0,0.0], p:[0.0,0.0]};
    let mut machines = 0;
    for line in read_lines() {
        if line != "" {
            let offsets = line.get((if line.starts_with("Button"){10} else {7})..).unwrap().split(", ").map(|f| f.get(2..).unwrap().parse::<f64>().unwrap()).collect::<Vec<f64>>();
            let offset = [offsets[0], offsets[1]];

            if line.contains(" A:") {
                machine.a = offset;
            } else if line.contains(" B:") {
                machine.b = offset;
            } else {
                machine.p = offset;
            }
        } else {
            machines += 1;
            let determinant = machine.a[0] * machine.b[1] - machine.a[1] * machine.b[0];
            let a = ((-machine.b[0]) * machine.p[1] + machine.b[1] * machine.p[0]) / determinant;
            let b = (machine.a[0] * machine.p[1] - machine.a[1] * machine.p[0]) / determinant;

            println!("a:{a} b:{b}");
            if a.floor() == a && b.floor() == b && a >= 0.0 && b >= 0.0 {
                // if a > 100.0 || b > 100.0 {continue;}
                result += a as i32 * 3 + b as i32;
            }

        }
    }
    dbg!(machines);
    return result;
}
fn task2() -> i64 {
    let mut result:i64 = 0;
    let mut machine = Machine {a:[0.0,0.0], b:[0.0,0.0], p:[0.0,0.0]};
    let mut machines = 0;
    for line in read_lines() {
        if line != "" {
            let offsets = line.get((if line.starts_with("Button"){10} else {7})..).unwrap().split(", ").map(|f| f.get(2..).unwrap().parse::<f64>().unwrap()).collect::<Vec<f64>>();
            let offset = [offsets[0], offsets[1]];

            if line.contains(" A:") {
                machine.a = offset;
            } else if line.contains(" B:") {
                machine.b = offset;
            } else {
                machine.p = [offset[0] + 10000000000000.0, offset[1] + 10000000000000.0];
            }
        } else {
            machines += 1;
            let determinant = machine.a[0] * machine.b[1] - machine.a[1] * machine.b[0];
            let a = ((-machine.b[0]) * machine.p[1] + machine.b[1] * machine.p[0]) / determinant;
            let b = (machine.a[0] * machine.p[1] - machine.a[1] * machine.p[0]) / determinant;

            println!("a:{a} b:{b}");
            if a.floor() == a && b.floor() == b && a >= 0.0 && b >= 0.0 {
                // if a > 100.0 || b > 100.0 {continue;}
                result += a as i64 * 3 + b as i64;
            }

        }
    }
    dbg!(machines);
    return result;
}

fn main() {
    let result_task1 = task1();
    let result_task2 = task2();

    println!("Result for the first task: {}", result_task1);
    println!("Result for the second task: {}", result_task2);
}
