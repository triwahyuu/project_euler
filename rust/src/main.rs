use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    // println!("{:?}", args);
    println!("Project Euler in Rust.\n\n");

    match args.len() {
        // no arguments passed
        1 => {
            println!("No problem number argument given.");
        },
        // the problem number argument
        2 => {
            match args[1].parse::<String>() {
                Ok(n) => println!("it's valid: {}", n),
                Err(e) => println!("invalid with error: {}", e)
            }
        },
        _ => {
            println!("What's this?")
        }
    }
}
