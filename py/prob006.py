def compute():
    sq_sum = sum(i for i in range(1, 101))**2
    sum_sq = sum(i*i for i in range(1, 101))
    return sq_sum - sum_sq

if __name__ == "__main__":
    print(compute())
