## well that's easy, just throw it all to python
def compute():
    ans = str(sum(i**i for i in range(1,1001)))
    return ans[-10:] # returns the last 10 digit of the value

if __name__ == "__main__":
    print(compute())