#include <iostream>
#include <chrono>
#include "euler.h"

#define PROB_NUM    10

uint64_t compute()
{
    std::vector<uint32_t> primes = list_prime(2000000);
    std::vector<uint64_t> primes_int(primes.begin(), primes.end());
    return sum(primes_int);
}


int test_answer(std::string prob_answer) {
    std::string answer;
    if(!get_answer(PROB_NUM, &answer)) {
        std::cout << "file not found" << std::endl;
        return 1;
    }

    assert(answer.compare(prob_answer) == 0);
    return 0;
}

int main(int argc, char const *argv[])
{
    auto t1 = std::chrono::high_resolution_clock::now();
    int64_t result = compute();
    auto t2 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();
    std::cout << result << "\tin " << duration << " us\n";

    // do testing
    test_answer(std::to_string(result));
    return 0;
}
