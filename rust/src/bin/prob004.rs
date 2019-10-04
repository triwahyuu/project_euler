extern crate euler;

fn compute() -> i32{
    let mut max_palin = 0;
    for i in (99..1000).rev() {
        for j in (99..1000).rev(){
            let p = i*j;
            if p < max_palin { break }
            
            if euler::is_palindrome(p) {
                max_palin = p;
                break;
            }
        }
    }

    max_palin
}

fn main() {
    let now = std::time::Instant::now();
    let result = compute();
    println!("{:?}\tin {}ms", result, now.elapsed().as_millis());
}


#[cfg(test)]
mod tests {
    use super::*;
    const PROB_NUM: usize = 4;
    
    #[test]
    fn test_prob004() {
        let result = compute().to_string();
        euler::test_answer(PROB_NUM, result);
    }
}