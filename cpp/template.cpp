#include <iostream>
#include <chrono>
#include "utils.h"

int64_t compute()
{
    return 0;
}

int test_prob000() {
    std::string answer;
    get_answer(1, &answer);

    assert(answer.compare("1234") == 0);
    return 0;
}

int main(int argc, char const *argv[])
{
    auto t1 = std::chrono::high_resolution_clock::now();
    int64_t result = compute();
    auto t2 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();
    std::cout << result << "\tin " << duration << " us\n";
    return test_prob000();
}