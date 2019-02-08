## trying to use Dickson's method
## https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
## how to stop them?
## or maybe use fibonacci sequence is faster (method 2)
## (2*h[n+1]*h[n+2], h[n]*h[n+3], 2*h[n+1]*h[n+2]+h[n]^2)
## total len = 4*h[n+1]*h[n+2] + h[n]*(h[n]+h[n+3])
import itertools

def compute():
    triples = []
    limit = 100
    for r in range(2,100,2):
        val = r*r//2
        for i in range(1, int(val**0.5)+1):
            if val%i == 0:
                s,t = i, val//i
                a,b,c = r+s,r+t,r+s+t
                # if a+b+c > limit:
                #     break
                triples.append((a,b,c,r))
        # if 5*r+2 > limit:
        #     break
    return triples

# def compute():
#     triples = []
#     for r in range(2, 100, 2):
#         val = r*r//2
#         factors = factor_pairs(val)
#         for i in factors:
#             s,t = i
#             triples.append((r+s,r+t,r+s+t))
#     return triples

# def factor_pairs(n):
#     pairs = [(1, n)]
#     for i in range(2, int(n**0.5)+1):
#         if n%i == 0:
#             pairs.append((i, n//i))
#     return pairs

if __name__ == "__main__":
    print(compute())