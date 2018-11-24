# calculate days of the week using Zeller's algorithm
# 1=sunday, 2=monday,..., 0=saturday
# https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Zeller%E2%80%99s_algorithm
def compute():
    return sum(1 for y in range(1901, 2001) for m in range(1, 13) if day(1, m, y) == 1)

## returns the day of the week (date, month, Year)
def day(d, m, Y):
    if m == 1 or m == 2: Y -= 1
    y = Y%100   # the last 2 digit of Y
    c = Y//100  # the first 2 digit of Y
    if m < 3: m += 12
    
    w = (d + ((13*(m+1))//5) + y + (y//4) + (c//4) - 2*c) % 7
    return w

if __name__ == "__main__":
    print(compute())