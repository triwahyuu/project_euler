## in order for the concatenated number to get as high as possible, the number
## it self needs to be at least has start digit 9 (first concatenated is multiplied
## by 1). So we just need to look for the highest number that can form 1 to 9 
## pandigital number with particular multiplier. The only possible candidate 
## is for 1-to-2 multiplier

def compute():
    mult = [1,2]
    ans = 0
    for n in range(9000,10000):
        res = ''
        for m in mult:
            res += str(n*m)
        if is_pandigital9(res) and int(res) > ans:
            ans = int(res)
    return ans

def is_pandigital9(n): # n is an string
    str_sort = ''.join(sorted(n))
    if str_sort == '123456789':
        return True
    else:
        return False

if __name__ == "__main__":
    print(compute())