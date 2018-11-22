## BRUTE FORCE
from euler import list_prime, is_prime

primes = list_prime(1000000)
seen = []

def compute():
    ans = sum(n_circ_prime(n) for n in primes)
    return ans

# return the number of circular prime
def n_circ_prime(n):
    if n not in seen:
        n = str(n)
        # create all rotation order
        rot_list = [[n[i - j] for i in range(len(n))] for j in range(len(n))]
        rot = set(int(''.join(x)) for x in rot_list)    # use set, so there is no duplicate

        s = sum(1 for p in rot if is_prime(p))

        if len(rot) == s:
            print(rot)
            seen.extend(rot)
            return s
        else:
            return 0
    else:
        return 0

if __name__ == "__main__":
    print(compute())