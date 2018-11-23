def compute():
    # val = [a for a in range(1,100) if is_dbl_palindrome(a)]
    ans = sum(a for a in range(1,1000000) if is_dbl_palindrome(a))
    return ans

def is_dbl_palindrome(n):
    n_bin = to_binary(n)
    n = str(n)
    if n == reverse(n) and n_bin == reverse(n_bin):
        return True
    else:
        return False

def reverse(c):
    return c[::-1]

def to_binary(n):
    return bin(n)[2::]

if __name__ == "__main__":
    print(compute())