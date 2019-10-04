#include <iostream>
#include <chrono>
#include "euler.h"

#define PROB_NUM    3

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