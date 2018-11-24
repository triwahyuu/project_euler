def compute():
    n = 600851475143
    for i in range(3, int(n**0.5)+1, 2):
        while n%i == 0:
            n //= i
            ans = i
    return ans

if __name__ == "__main__":
    print(compute())