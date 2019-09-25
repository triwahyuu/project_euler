use std::time::Instant;

fn compute() -> u64{
    let mut num: u64 = 600851475143;
    let mut idx = 3;
    let mut highest = 2;
    while idx * idx <= num {
        if num % idx == 0{
            highest = idx;
            num /= idx;
        }
        else {
            idx += 2;
        }
    }
    
    highest = if num != 1 { num } else { highest };
    highest
}

fn main() {
    let now = Instant::now();
    
    let result = compute();
    println!("{:?}\tin {}us", result, now.elapsed().as_micros());
}
