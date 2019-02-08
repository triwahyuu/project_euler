#include <iostream>

int compute()
{
    int fib[2] = {1,2};
    int sum = 2, n;

    while(n < 4000000){
        n = fib[0] + fib[1];
        fib[0] = fib[1];
        fib[1] = n;
        if(n%2 == 0)
            sum += n;
    }
    return sum;
}

int main(int argc, char const *argv[])
{
    std::cout << compute() << std::endl;
    return 0;
}