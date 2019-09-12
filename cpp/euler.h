// re-implementing python version solution
// of commonly used function
#include <vector>
#include <cmath>
#include <map>
#include "utils.h"

bool is_prime(int n)
{
    if(n <= 1) return false;
    else if(n <= 3) return true;
    else if(n%2 == 0 || n%3 == 0) return false;

    int i = 5;
    while(i*i <= n){
        if(n%i == 0 || n%(i+2) == 0) return false;
        i += 6;
    }
    return true;
}

bool is_palindrome(uint32_t n)
{
    std::string n_str = std::to_string(n);
    return n_str == reversed(n_str);
}

std::vector<bool> list_primality(uint32_t n)
{
    std::vector<bool> state(n+1, true);
    state[0] = false; state[1] = false;
    for(int i = 2; i < std::sqrt(n)+1; i++)
    {
        if(state[i] == true){
            for(int j = i*i; j < n+1; j+=i)
                state[j] = false;
        }
    }
    return state;
}

std::vector<uint32_t> list_prime(uint32_t n)
{
    std::vector<uint32_t> prime;

    std::vector<bool> st = list_primality(n);
    for(int i = 2; i < n+1; i++)
    {
        if(st[i] == true)
            prime.push_back(i);
    }
    return prime;
}

uint32_t gcd(uint32_t a, uint32_t b)
{
    static std::map<std::pair<int,int>, int> cache;
    if(a < b) std::swap(a,b);

    if(cache[std::make_pair(a,b)] != 0) return cache[std::make_pair(a,b)];
    else if(b == 0) return a;
    else{
        uint32_t x = gcd(b, a%b);
        cache[std::make_pair(a,b)] = x;
        return x;
    }
}