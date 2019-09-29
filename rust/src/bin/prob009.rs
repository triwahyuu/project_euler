fn compute() -> i32 {
    let total = 1000;
    
    for a in 3..(f64::from(total)/3.0) as i32 {
        for b in a+1..(f64::from(total)/2.0) as i32 {
            let c = total - a - b;

            if c < 0 {
                break;
            }

            if c*c == a*a + b*b {
                return a * b * c;
            }
        }
    }
    
    return 0;
}

fn main() {
    let now = std::time::Instant::now();
    
    let result = compute();
    println!("{:?}\tin {}ms", result, now.elapsed().as_millis());
}
