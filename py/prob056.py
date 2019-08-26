def compute():
    ans = max(sum_digit(a**b) for a in range(100) for b in range(100))
    return ans

def sum_digit(n):
    return sum(int(a) for a in str(n))

if __name__ == "__main__":
    print(compute())