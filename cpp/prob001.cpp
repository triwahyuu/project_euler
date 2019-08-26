#include <iostream>

int compute()
{
    int sum = 0;
    for(int i = 0; i < 1000; i++)
    {
        if(i%3 == 0 or i%5 == 0)
            sum += i;
    }
    return sum;
}

int main(int argc, char const *argv[])
{
    std::cout << compute() << std::endl;
    return 0;
}