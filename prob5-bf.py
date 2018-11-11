# this solution takes way too long
# DON'T try to run it
n = 2520
found = False
while not found:
    found = True
    n = n+1
    #print(n)
    for i in range(20, 1, -1):
        if n%i != 0:
            found = False
            break
        #print(i)

print("FOUND!! ", end = '')
print(n)
