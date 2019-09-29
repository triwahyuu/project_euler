extern crate euler;

fn compute() -> u32{
    let mut idx = 1;
    let bound = 10001;

    for n in 2.. {
        if euler::is_prime(n) {
            idx += 1;
            if idx == bound {
                return n;
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
