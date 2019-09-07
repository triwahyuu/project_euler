#include <iostream>
#include <chrono>
#include "euler.h"

int compute()
{
    const uint64_t num = 600851475143;

    std::vector<int> factors;
    uint64_t n = num;
    int d = 2;
    while(n > 1){
        if(n%d == 0){
            factors.push_back(d);
            while(n%d == 0) 
                n /= d;
        }
        d++;
    }
    return factors.back();
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
