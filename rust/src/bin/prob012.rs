extern crate euler;

fn compute() -> u32 {
    (1..).scan(0, |acc, x| {*acc += x; Some(*acc)})         // return new iterator
        .skip_while(|&triangle| num_factors(triangle) <= 50)
        .next()
        .unwrap()
}

fn num_factors(n: u32) -> u32 {
    let sqrt_n = (n as f64).sqrt() as u32;

    let nfactors = (1..sqrt_n+1).filter(|i| n%i == 0)
        .fold(0, |acc, _| acc + 2u32);

    if n%sqrt_n == 0 {
        return nfactors - 1;
    }
    else {
        return nfactors;
    }
}

fn main() {
    let now = std::time::Instant::now();
    let result = compute();
    println!("{:?}\tin {}ms", result, now.elapsed().as_millis());
}

#[cfg(test)]
mod tests {
    use super::*;
    const PROB_NUM: usize = 12;
    
    #[test]
    fn test_prob012() {
        let result = compute().to_string();
        euler::test_answer(PROB_NUM, result);
    }
}