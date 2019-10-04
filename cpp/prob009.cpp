#include <iostream>
#include <chrono>
#include "utils.h"

#define PROB_NUM    9

int compute()
{
    const int SUM = 1000;
    for(int a = 3; a < SUM; a++){
        for(int b = a+1; b < SUM; b++){
            int c = SUM - a - b;
            if(c < 0)
                break;
            if(a*a + b*b == c*c)
                return a*b*c;
        }
    }
    
    return 0;
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