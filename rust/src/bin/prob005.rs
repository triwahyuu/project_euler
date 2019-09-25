use std::time::Instant;

fn compute() -> u32 {
    // so this is basically a least common multiple (lcm)
    // https://en.wikipedia.org/wiki/Least_common_multiple
    // this is the answer: 2*3*2*5*7*2*3*11*13*2*17*19

    (2..=20).rev().fold(1, |acc, x| lcm(acc, x))
}

fn gcd(a: u32, b: u32) -> u32 {
    let x = std::cmp::max(a, b);
    let y = std::cmp::min(a, b);
    
    if y == 0 {
        x
    }
    else {
        gcd(y, x % y)
    }
}

fn lcm(a: u32, b: u32) -> u32 {
    (((a * b) as f64) / (gcd(a, b) as f64)) as u32
}

fn main() {
    let now = Instant::now();
    
    let result = compute();
    println!("{:?}\tin {}ms", result, now.elapsed().as_millis());
}
