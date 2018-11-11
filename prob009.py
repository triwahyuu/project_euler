# trying to brute force

tot = 1000
for a in range(1,tot+1):
    for b in range(a,tot+1):
        c = tot - a - b
        if c < 0: break
        if a*a+b*b == c*c: print(a, b, c, a*b*c)
