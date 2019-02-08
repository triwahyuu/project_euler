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
    
    std::cout << is_palindrome(1221) << " " << is_palindrome(100) << std::endl;

    return 0;
}
