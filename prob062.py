## calculate cubes of a number, store it. If it already has permutation
## on the list, join them together. The stored value is in sorted form
## let's use set to get faster search time

import itertools

def compute():
    seen_sorted = set()     # store sorted cube
    perm_dict = {}          # store seen value
    for i in itertools.count(100):
        cube = i**3
        sorted_cube = ''.join(sorted(str(cube)))
        if sorted_cube not in seen_sorted:
            seen_sorted.add(sorted_cube)
            perm_dict[sorted_cube] = [i]
        else:
            perm_dict[sorted_cube] += [i]
            if len(perm_dict[sorted_cube]) == 5:
                return (sorted(perm_dict[sorted_cube])[0])**3

if __name__ == "__main__":
    print(compute())