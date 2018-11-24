from euler import list_prime
import time

N = 1000000
primes = list_prime(N)

## cache for sum of prime upto 'n' index (of prime list)
sum_prime_upto_idx = [2, 5, 10]

def compute():
    max_cons = 0
    for p in primes:
        n = len_cons_prime(p)
        if n > max_cons:
            max_cons = n
            ans = p
    return ans

## returns the length of the longest consecutive prime sum of 'n'
def len_cons_prime(n):
    m_cons = len(sum_prime_upto_idx) - 1
    tot = sum_prime_upto_idx[-1]
    while n > tot:
        m_cons += 1
        tot += primes[m_cons]
        sum_prime_upto_idx.append(tot)
    
    for i in primes:
        if tot > n:
            tot -= i
            m_cons -= 1
        elif tot < n:
            return 0
        else:
            return m_cons

## returns the length of the longest consecutive prime sum of 'n'
def len_cons_prime1(n): 
    # maximum number of consecutive prime sum up to n
    tot = m_cons = 0
    for p in primes:
        tot += p
        m_cons += 1
        if tot >= n:
            break

    for i in primes:
        if tot > n:
            tot -= i
            m_cons -= 1
        elif tot < n:
            return 0
        else:
            return m_cons

if __name__ == "__main__":
    t = time.time()
    print(compute())
    print(time.time() - t)