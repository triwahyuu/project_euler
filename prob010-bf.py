# trying to bruteforce ~ takes quite long
from euler import is_prime

tot = 0
for i in range(1, 2000000):
    if is_prime(i): tot = tot+i

print(tot)