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
    int res = 1;
    for(auto i : x)
    {
    }
    
    int a = 5, b = 3;
    std::swap(a,b);
    std::cout << a << " " << b << std::endl;

    std::map<std::pair<int,int>, int> cache;
    cache[std::make_pair(5,2)] = 10;
    cache[std::make_pair(3,2)] = 6;
    std::cout << cache[std::make_pair(3,3)] << std::endl;

    return 0;
}
