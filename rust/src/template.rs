fn compute() -> i32{
    100
}

fn main() {
    let now = std::time::Instant::now();
    
    let result = compute();
    println!("{:?}\tin {}ms", result, now.elapsed().as_millis());
}
