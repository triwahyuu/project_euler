use std::time::Instant;

fn fibonacci(n: u32) -> u32{
    let sqrt5 = (5f64).sqrt();
    let phi = (1f64 + sqrt5)/2f64;
    let psi = (1f64 - sqrt5)/2f64;
    ((phi.powf((n+2).into()) - psi.powf((n+2).into()))/sqrt5) as u32
}

fn compute() -> u32{
    (1..).map(|n| fibonacci(n))
        .take_while(|&x| x < 4000000)
        .filter(|&x| x%2 == 0)
        .sum()
}

fn main() {
    let now = Instant::now();
    
    let result = compute();
    println!("{:?}\tin {}us", result, now.elapsed().as_micros());
}
