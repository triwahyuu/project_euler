#include <iostream>
#include <chrono>
#include "euler.h"
#include "utils.h"

uint64_t compute()
{
    std::vector<uint32_t> primes = list_prime(2000000);
    std::vector<uint64_t> primes_int(primes.begin(), primes.end());
    return sum(primes_int);
}

int main(int argc, char const *argv[])
{
    auto t1 = std::chrono::high_resolution_clock::now();
    uint64_t result = compute();
    auto t2 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << result << "\tin " << duration << " ms\n";
    return 0;
}
