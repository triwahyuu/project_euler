extern crate euler;

fn compute() -> i32{
    let bound = 1000;
    (1..bound).filter(|x| x % 3 == 0 || x % 5 == 0).sum()
}

fn main() {
    let now = std::time::Instant::now();
    let result = compute();
    println!("{:?}\tin {}us", result, now.elapsed().as_micros());
}


#[cfg(test)]
mod tests {
    use super::*;
    const PROB_NUM: usize = 1;
    
    #[test]
    fn test_prob001() {
        let result = compute().to_string();
        euler::test_answer(PROB_NUM, result);
    }
}