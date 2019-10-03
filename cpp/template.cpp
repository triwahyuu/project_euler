#include <iostream>
#include <chrono>
#include "utils.h"

int64_t compute()
{
    return 0;
}

int test_answer() {
    std::string answer;
    if(!get_answer(1, &answer)) {
        std::cout << "file not found" << std::endl;
        return 1;
    }

    assert(answer.compare("233168") == 0);
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
    test_answer();
    return 0;
}