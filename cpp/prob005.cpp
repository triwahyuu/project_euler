#include <iostream>
#include "euler.h"

uint32_t lcm(uint32_t a, uint32_t b)
{
    return std::abs(a*b)/gcd(a,b);
}

int compute()
{
    int result = 1;
    for(int i = 20; i > 2; i--)
        result = lcm(i, result);
    return result;
}

int main(int argc, char const *argv[])
{
    std::cout << compute() << std::endl;
    return 0;
}
