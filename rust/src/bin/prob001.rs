
fn compute() -> i32{
    let bound = 1000;
    (1..bound).filter(|x| x % 3 == 0 || x % 5 == 0).sum()
}

fn main() {
    let now = std::time::Instant::now();

    let result = compute();
    println!("{:?}\tin {}us", result, now.elapsed().as_micros());
}
