use std::time::Instant;

fn compute() -> u32 {
    // so this is basically a least common multiple (lcm)
    // https://en.wikipedia.org/wiki/Least_common_multiple
    // this is the answer: 2*3*2*5*7*2*3*11*13*2*17*19

    let mut res = 1;
    for i in 1..=15 {
        res = lcm(res, i);
        println!();
    }
    res
}

fn gcd(a: u32, b: u32) -> u32 {
    if a <= 0 || b <= 0 {
        0
    }
    else if a < b{
        gcd(a, b - a)
    }
    else if a > b {
        gcd(a - b, b)
    }
    else {
        a
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
