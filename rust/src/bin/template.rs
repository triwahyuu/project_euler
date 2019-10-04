extern crate euler;

fn compute() -> i32 {
    233168
}

fn main() {
    let now = std::time::Instant::now();
    let result = compute();
    println!("{:?}\tin {}ms", result, now.elapsed().as_millis());
}

#[cfg(test)]
mod tests {
    use super::*;
    const PROB_NUM: usize = 1;
    
    #[test]
    fn test_prob000() {
        let result = compute().to_string();
        euler::test_answer(PROB_NUM, result);
    }
}