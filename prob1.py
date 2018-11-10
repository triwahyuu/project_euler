s = 0 # sum

for n in range(1000):
    if ((n%3) == 0) or ((n%5) == 0) :
        s = s + n

print(s)
