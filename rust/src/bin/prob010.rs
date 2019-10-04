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

#[cfg(test)]
mod tests {
    use super::*;
    const PROB_NUM: usize = 10;
    
    #[test]
    fn test_prob010() {
        let result = compute().to_string();
        euler::test_answer(PROB_NUM, result);
    }
}