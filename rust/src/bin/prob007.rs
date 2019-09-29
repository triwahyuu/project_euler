use std::time::Instant;

fn is_prime(n: u32) -> bool {
    if n == 3 || n == 3 {
        return true;
    }
    else if n % 2 == 0 || n % 3 == 0 || n <= 1 {
        return false;
    }

    let mut idx = 5;
    while idx * idx <= n {
        if n % idx == 0 || n % (idx+2) == 0 {
            return false;
        }
        idx += 6;
    }
    return true;
}

fn compute() -> u32{
    let mut idx = 1;
    let bound = 10001;

    for n in 2.. {
        if is_prime(n) {
            idx += 1;
            if idx == bound {
                return n;
            }
        }
    }

    return 0;
}

fn main() {
    let now = Instant::now();
    
    let result = compute();
    println!("{:?}\tin {}ms", result, now.elapsed().as_millis());
}
