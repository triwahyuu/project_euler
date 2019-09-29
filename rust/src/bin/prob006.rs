use std::time::Instant;

fn compute() -> i32{
    let num: i32 = 100;
    ((1..=num).sum::<i32>() * (1..=num).sum::<i32>()) - (1..=num).fold(0, |acc, x| acc + x*x)
}

fn main() {
    let now = Instant::now();
    
    let result = compute();
    println!("{:?}\tin {}us", result, now.elapsed().as_micros());
}
