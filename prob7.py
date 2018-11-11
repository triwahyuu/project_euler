# finding 10001st prime
import euler

idx = 0
num = 1
while idx<10001:
    num = num+1
    if euler.is_prime(num): idx = idx+1

print(num)