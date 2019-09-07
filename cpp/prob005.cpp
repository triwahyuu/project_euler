#include <iostream>
#include <chrono>
#include "euler.h"

uint32_t lcm(uint32_t a, uint32_t b)
{
    return abs(a*b)/gcd(a,b);
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
    auto t1 = std::chrono::high_resolution_clock::now();
    int64_t result = compute();
    auto t2 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();
    std::cout << result << "\tin " << duration << " us\n";
    return 0;
}
