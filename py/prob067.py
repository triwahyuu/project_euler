## trying to use dynamic programming, the same as p018
import csv

def compute():
    tr = load_data()
    for r in range(len(tr)-1, 0, -1):
        tmp = [max(tr[r][c] + tr[r-1][c], tr[r][c+1] + tr[r-1][c]) for c in range(len(tr[r]) - 1)]
        del tr[-2:] # remove the last 2 row
        tr.append(tmp)
    
    return tr[0][0]

def load_data():
    data_file = open('prob067_triangle.txt', newline='\n')
    txt = csv.reader(data_file, delimiter=' ')
    row = [r for r in txt]
    return [[int(i) for i in r] for r in row]

if __name__ == "__main__":
    print(compute())