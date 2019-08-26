## suppose product 'x', has factor 'a' and 'b', and total number of digit
## of (a,b,x) is 9. So the maximum value of 'x' is when number of digit of
## 'a' and 'b' is 2 or 3, which would make 'x' has around 5 digit (100^2)
def compute():
    ans = sum(a for a in range(1000,10000) if has_pandigital(a))
    return ans

def has_pandigital(n):
    sqrt_n = int(n**0.5)
    for i in range(1, sqrt_n+1):
        if n%i == 0:
            num = str(n) + str(i) + str(n//i)
            if is_pandigital9(num):
                return True
    
    return False

def is_pandigital9(n): # n is an string
    str_sort = ''.join(sorted(n))
    if str_sort == '123456789':
        return True
    else:
        return False

if __name__ == "__main__":
    # print(has_pandigital(7254))
    print(compute())