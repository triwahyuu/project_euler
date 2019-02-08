#include <iostream>
#include <vector>
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
    std::cout << compute() << std::endl;
    return 0;
}