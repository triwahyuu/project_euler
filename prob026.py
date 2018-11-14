## there a thing called 'cyclic numbers'
## https://en.wikipedia.org/wiki/Cyclic_number#Form_of_cyclic_numbers
## which we can directly calculate the number of recuring cycle

## still wrong, maybe here is the solution
## https://en.wikipedia.org/wiki/Repeating_decimal#Fractions_with_prime_denominators

from euler import list_prime

def compute():
    b = 10
    prime = list_prime(1000)
    max_dig = 0
    max_num = 0     # the number which has highest recuring digit
    for p in prime:
        rec_num = (b**(p-1)-1)//p   # the recuring cycle number
        dig = len(str(rec_num))     # the number of recuring cycle
        if dig > max_dig:
            max_dig = dig
            max_num = p
    return max_num

if __name__ == "__main__":
    print(compute())