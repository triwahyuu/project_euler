pub fn test_answer(prob_num: usize, answer: String) {
    let mut fname = std::env::current_dir().unwrap();
    fname.set_file_name("answers.txt");

    let answers_list: Vec<String> = std::fs::read_to_string(fname).unwrap()
        .split('\n')
        .map(String::from)
        .collect();

    let correct = answers_list[prob_num].get(4..).unwrap().to_string();

    assert_eq!(correct, answer);
}

pub fn fibonacci(n: u32) -> u64{
    let sqrt5 = (5.0f64).sqrt();
    let phi = (1.0 + sqrt5)/2.0;
    let psi = (1.0 - sqrt5)/2.0;
    ((phi.powf((n+2).into()) - psi.powf((n+2).into()))/sqrt5) as u64
}

pub fn is_palindrome(n: i32) -> bool {
    let n: String = n.to_string();
    n == n.chars().rev().collect::<String>()
}

pub fn gcd(a: u32, b: u32) -> u32 {
    let x = std::cmp::max(a, b);
    let y = std::cmp::min(a, b);
    
    if y == 0 {
        x
    }
    else {
        gcd(y, x % y)
    }
}

pub fn lcm(a: u32, b: u32) -> u32 {
    (((a * b) as f64) / (gcd(a, b) as f64)) as u32
}

pub fn is_prime(n: u32) -> bool {
    if n == 3 || n == 3 {
        return true;
    }
    else if n % 2 == 0 || n % 3 == 0 || n <= 1 {
        return false;
    }

    let mut idx = 5;
    while idx * idx <= n {
        if n % idx == 0 || n % (idx+2) == 0 {
            return false;
        }
        idx += 6;
    }
    return true;
}

pub fn list_prime(n: i32) -> Vec<u32> {
    let n = n as usize;
    let mut prime_state: Vec<bool> = (0..=n).map(|x| x >= 2 && (x % 2 != 0 || x == 2)).collect();
    for i in 3..=n {
        if prime_state[i] == true {
            for j in (i*i..=n).step_by(i) {
                prime_state[j] = false;
            }
        }
    }
    
    prime_state.iter().enumerate()
        .filter(|&(_, x)| *x)
        .map(|(n, _)| n as u32)
        .collect()
}