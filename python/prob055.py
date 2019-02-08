def compute():
    ans = sum(1 for n in range(10000) if is_lychrel(n))
    return ans

def is_lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]: # is palindrome?
            return False
    return True

if __name__ == "__main__":
    print(compute())