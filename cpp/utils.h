#ifndef UTILS_H
#define UTILS_H

#include <algorithm>
#include <string>
#include <vector>
#include <numeric>

std::string reversed(std::string str)
{
    std::reverse(str.begin(), str.end());
    return str;
}

uint32_t reversed(uint32_t num)
{
    return std::stoi(reversed(std::to_string(num)));
}

uint64_t product(std::vector<int> data)
{
    return std::accumulate(std::begin(data), std::end(data), 1, std::multiplies<int>());
}

#endif