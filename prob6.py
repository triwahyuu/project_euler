sum_sq = 0
sq_sum = 0
for i in range(1,101):
    sum_sq = sum_sq+i**2
    sq_sum = sq_sum+i

sq_sum=sq_sum**2
print(sq_sum, sum_sq, sq_sum-sum_sq)