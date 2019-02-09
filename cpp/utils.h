#include <algorithm>
#include <string>
#include <vector>

std::string reversed(std::string str)
{
    std::string s = str;
    std::reverse(s.begin(), s.end());
    return s;
}

uint32_t reversed(uint32_t num)
{
    std::string s = std::to_string(num);
    int n = std::stoi(reversed(s));
    return n;
}

uint64_t product(std::vector<int> data)
{
    uint64_t res = 1;
    int n = data.size();
    for(int i = 0; i < n; i++){
        res *= data[i];
    }
    return res;
}