extern crate euler;

fn compute() -> u64{
    (1..).map(|n| euler::fibonacci(n))
        .take_while(|&x| x < 4000000)
        .filter(|&x| x%2 == 0)
        .sum()
}

fn main() {
    let now = std::time::Instant::now();
    
    let result = compute();
    println!("{:?}\tin {}us", result, now.elapsed().as_micros());
}
