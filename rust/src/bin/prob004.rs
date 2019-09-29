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
