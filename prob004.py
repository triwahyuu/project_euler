
def is_palindrome(n):
    n_len = len(n)
    if (n_len%2 == 0):
        for i in range(n_len//2):
            if not (n[i]==n[n_len-i-1]): return False
        return True
    else: return False

p = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if p < i*j and is_palindrome(str(i*j)): 
            print(i, j, i*j)
            p = i*j
            break

