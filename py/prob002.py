def compute():
    s = 0
    x, y = 1, 2
    while y < 4000000:
        if y%2 == 0:  # if even
            s += y
        x, y = y, x+y
    return s

if __name__ == "__main__":
    print(compute())
