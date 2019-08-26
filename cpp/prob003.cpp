#include <iostream>
#include <cmath>
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
    std::cout << compute() << std::endl;
    return 0;
}
