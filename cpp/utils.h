#ifndef UTILS_H
#define UTILS_H

#include <algorithm>
#include <string>
#include <vector>
#include <numeric>
#include <fstream>
#include <cassert>

int get_answer(uint16_t prob_num, std::string *answer)
{
    int cnt = 0;
    std::vector<std::string> answers_list;

    std::string line;
    std::ifstream myfile("../answers.txt");
    // or use `__FILE__` to get the sources path

    if(myfile.is_open()) {
        while(getline(myfile, line)) {
            answers_list.push_back(line);
            cnt++;
        }
        myfile.close();
    }
    else 
        return 0;
    
    *answer = answers_list[prob_num].substr(4, std::string::npos);
    return (*answer).length();
}

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