extern crate euler;
fn compute() -> u64 {
    euler::list_prime(2000000).iter()
        .fold(0u64, |acc, x| acc + *x as u64)
}

fn main() {
    let now = std::time::Instant::now();
    
    let result = compute();
    println!("{:?}\tin {}ms", result, now.elapsed().as_millis());
}
