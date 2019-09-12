#include <iostream>
#include <chrono>

int compute()
{
    const int SUM = 1000;
    for(int a = 3; a < SUM; a++){
        for(int b = a+1; b < SUM; b++){
            int c = SUM - a - b;
            if(c < 0)
                break;
            if(a*a + b*b == c*c)
                return a*b*c;
        }
    }
    
    return 0;
}

int main(int argc, char const *argv[])
{
    auto t1 = std::chrono::high_resolution_clock::now();
    int64_t result = compute();
    auto t2 = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    std::cout << result << "\tin " << duration << " ms\n";
    return 0;
}
