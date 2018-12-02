## SOLVED, takes ~2.8s, any idea how to optimize?
## it could also use permutation, a bit faster but it needs external library
## just calculate the chain, make use of memoization
from euler import factorial
from itertools import permutations

fact = [factorial(n) for n in range(10)]
known_len = {1, 2}
chain_len = {1:1, 2:1}

def compute():
    limit = 10**6
    ans = sum(1 for n in range(3, limit) if chain_length(n) == 60)
    return ans

def chain_length(n):
    if n in known_len:
        return chain_len[n]
    chain = {n}
    val = n
    while True:
        val = sum(fact[int(x)] for x in str(val))

        if val in known_len:
            l = len(chain) + chain_len[val]
            break
        elif val not in chain:
            chain.add(val)
        else:
            l = len(chain)
            break
    perm = [int(''.join(a)) for a in permutations(str(n)) if a[0] != '0']
    for p in perm:
        known_len.add(p)
        chain_len[p] = l
    return chain_len[n]

if __name__ == "__main__":
    print(compute())