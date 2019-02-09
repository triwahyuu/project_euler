#include <iostream>
#include "euler.h"

int compute()
{
    int n = 1, idx = 1;
    while(idx < 10001){
        n += 2;
        if(is_prime(n))
            idx++;
    }
    return n;
}

int main(int argc, char const *argv[])
{
    std::cout << compute() << std::endl;
    return 0;
}
