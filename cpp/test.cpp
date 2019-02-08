// testing playground
#include <iostream>
#include <vector>
#include "euler.h"

std::vector<int> test(){
    std::vector<int> x(5,2);
    return x;
}

int main(int argc, char const *argv[])
{
    std::cout << "TESTING!!"<< std::endl;
    
    std::vector<unsigned int> x = list_prime(10);
    for(auto i : x)
    {
        // std::cout << i << std::endl;
    }
    
    int a = 5, b = 3;
    std::swap(a,b);
    std::cout << a << " " << b << std::endl;

    std::cout << std::abs(-5) << std::endl;

    return 0;
}
