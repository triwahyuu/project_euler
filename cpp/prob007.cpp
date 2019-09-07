#include <iostream>
#include <chrono>
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
    auto t1 = std::chrono::high_resolution_clock::now();
    int64_t result = compute();
    auto t2 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();
    std::cout << result << "\tin " << duration << " us\n";
    return 0;
}
