use std::time::Instant;

fn compute() -> i32{
    100
}

fn main() {
    let now = Instant::now();
    
    let result = compute();
    println!("{:?}\tin {}ms", result, now.elapsed().as_millis());
}
