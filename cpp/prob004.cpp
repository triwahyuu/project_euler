#include <iostream>
#include <chrono>
#include "euler.h"

int compute()
{
    uint32_t num = 0;
    
    for(int i = 999; i >= 100; i--){
        for(int j = 999; j >= 100; j--){
            uint32_t x = i*j;
            if(is_palindrome(x) && num < x) num = x;
        }
    }
    return num;
}

int main(int argc, char const *argv[])
{   
    auto t1 = std::chrono::high_resolution_clock::now();
    int64_t result = compute();
    auto t2 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << result << "\tin " << duration << " ms\n";
    return 0;
}