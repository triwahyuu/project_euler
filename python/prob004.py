def compute():
    max_p = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            p = i*j
            if max_p < p and is_palindrome(p):
                max_p = p
                break
    return max_p

def is_palindrome(n):
    reverse = ''.join(reversed(str(n)))
    return str(n) == reverse

if __name__ == "__main__":
    print(compute())