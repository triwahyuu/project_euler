## well it's easy, just throw it all to python

def compute():
    return sum(int(i) for i in str(2**1000))

if __name__ == "__main__":
    print(compute())