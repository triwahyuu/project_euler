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

uint64_t product(std::vector<uint64_t> data)
{
    return std::accumulate(std::begin(data), std::end(data), 1, std::multiplies<uint64_t>());
}

uint64_t sum(std::vector<uint64_t> data)
{
    return std::accumulate(std::begin(data), std::end(data), (uint64_t)0);
}

#endif