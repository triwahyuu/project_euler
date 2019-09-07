#include <iostream>
#include <chrono>

int64_t compute()
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
    auto t1 = std::chrono::high_resolution_clock::now();
    int64_t result = compute();
    auto t2 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();
    std::cout << result << "\tin " << duration << " us\n";
    return 0;
}