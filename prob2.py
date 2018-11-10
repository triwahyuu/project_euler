seq = [1, 2]
n = 0
s = 2

while n < 4000000:
    n = seq[0] + seq[1]
    seq.append(n)   # append new value
    seq.pop(0)      # remove first array value

    if (n%2) == 0:  # if even
        s = s+n

print(s)
