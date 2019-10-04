extern crate euler;

fn compute() -> i32 {
    70600674
}

fn main() {
    let now = std::time::Instant::now();
    let result = compute();
    println!("{:?}\tin {}ms", result, now.elapsed().as_millis());
}


#[cfg(test)]
mod tests {
    use super::*;
    const PROB_NUM: usize = 11;
    
    #[test]
    fn test_prob011() {
        let result = compute().to_string();
        euler::test_answer(PROB_NUM, result);
    }
}