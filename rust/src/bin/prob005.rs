extern crate euler;

fn compute() -> u32 {
    // so this is basically a least common multiple (lcm)
    // https://en.wikipedia.org/wiki/Least_common_multiple
    // this is the answer: 2*3*2*5*7*2*3*11*13*2*17*19

    (2..=20).rev().fold(1, |acc, x| euler::lcm(acc, x))
}

fn main() {
    let now = std::time::Instant::now();
    let result = compute();
    println!("{:?}\tin {}us", result, now.elapsed().as_micros());
}


#[cfg(test)]
mod tests {
    use super::*;
    const PROB_NUM: usize = 5;
    
    #[test]
    fn test_prob005() {
        let result = compute().to_string();
        euler::test_answer(PROB_NUM, result);
    }
}