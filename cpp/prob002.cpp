#include <iostream>

int main(int argc, char const *argv[])
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

    std::cout << sum << std::endl;
    return 0;
}