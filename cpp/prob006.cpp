#include <iostream>
#include <chrono>

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
    auto t1 = std::chrono::high_resolution_clock::now();
    int64_t result = compute();
    auto t2 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();
    std::cout << result << "\tin " << duration << " us\n";
    return 0;
}
