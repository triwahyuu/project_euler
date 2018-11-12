
def compute():
    txt = open("p022.txt", 'r')
    names = txt.read().split(',')
    names.pop()     # delete unnecesary last value
    names.sort()    # sort alphabetically
    
    score = 0
    for i in range(len(names)):
        score += value(names[i]) * (i+1)
    
    return score

def value(name):
    s = 0
    for c in name:
        s += ord(c)-64 # convert char to ascii then map value
    return s

if __name__ == "__main__":
    print(compute())