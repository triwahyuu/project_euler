## takes waaaay tooo long and unsolved
from itertools import permutations

cube = {i**3 for i in range(1000)}

def compute():
    for i in range(345, 1000):
        c = i**3
        perm = permutations(str(c), len(str(c)))
        found = set()
        for p in perm:
            n = int(''.join(p))
            if len(str(n)) == len(str(c)) and n in cube:
                found.add(n)
        print(i, found, len(found))
        if len(found) == 4:
            return sorted(found)[0]

if __name__ == "__main__":
    print(compute())