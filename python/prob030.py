## the maximum value: if every digit is 9 and the number of digit is 'n'
## sum of the fifth power digit is 'n*9^5', the maximum possible number of
## digit is 6 digit, which if all values are 9 the sum is around 350k
## which can be further eliminated as the first digit can't be 9
## then with the first digit being 1 and the rest is 9^5, the value is around 290k 
## and 1 is not counted, so started at 2
def compute():
    tot = sum(x for x in range(2,290000) if x == fifth_power_sum(x))
    return tot

def fifth_power_sum(n):
    tot = sum(int(a)**5 for a in str(n))
    return tot

if __name__ == "__main__":
    print(compute())