extern crate euler;

fn compute() -> i32{
    let num: i32 = 100;
    ((1..=num).sum::<i32>() * (1..=num).sum::<i32>()) - (1..=num).fold(0, |acc, x| acc + x*x)
}

fn main() {
    let now = std::time::Instant::now();
    let result = compute();
    println!("{:?}\tin {}us", result, now.elapsed().as_micros());
}


#[cfg(test)]
mod tests {
    use super::*;
    const PROB_NUM: usize = 6;
    
    #[test]
    fn test_prob006() {
        let result = compute().to_string();
        euler::test_answer(PROB_NUM, result);
    }
}