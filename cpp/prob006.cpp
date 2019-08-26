#include <iostream>

int compute()
{
    int sum = 0, sq_sum = 0;
    for(int i = 1; i <= 100; i++){
        sum += i;
        sq_sum += i*i;
    }
    return sum*sum - sq_sum;
}

int main(int argc, char const *argv[])
{
    std::cout << compute() << std::endl;
    return 0;
}
