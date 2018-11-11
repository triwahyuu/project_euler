n = 600851475143
max_div = 0

while ((n%2) == 0): n = int(n/2)

for i in range(3, int(n**0.5) + 1, 2):
    while (n%i == 0): 
        # print(i, end='')
        max_div = i
        n = int(n/i)

if(n > 2): max_div = n #print(n)
print(max_div)
