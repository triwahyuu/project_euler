# well it's easy, just throw it all to python

def compute():
    res = str(2**1000)
    res_int = [int(i) for i in res]
    return sum(res_int)

if __name__ == "__main__":
    print(compute())