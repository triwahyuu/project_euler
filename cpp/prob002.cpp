#include <iostream>
#include <chrono>

int compute()
{
    int fib[2] = {1,2};
    int sum = 2, n;

    while(n < 4000000){
        n = fib[0] + fib[1];
        fib[0] = fib[1];
        fib[1] = n;
        if(n%2 == 0)
            sum += n;
    }
    return sum;
}

int main(int argc, char const *argv[])
{
    auto t1 = std::chrono::high_resolution_clock::now();
    int64_t result = compute();
    auto t2 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();
    std::cout << result << "\tin " << duration << " us\n";
    return 0;
}