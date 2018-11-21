## keep dividing, and save the modulo in dict
## if the modulo value is in dict, the rest of the division 
## should be the same as the first division, so it's repeated
def recuring_len(n):
    seen = {0:0}
    m,i = 1,1
    while True:
        if m in seen:
            break
        else:
            seen[m] = i
            m = m*10 % n
            i += 1
    
    if m != 0: return i - seen[m]
    else: return 0

def compute():
    n = max(range(1,1000), key=recuring_len)
    return n

if __name__ == "__main__":
    print(compute())