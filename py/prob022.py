import os

def compute():
    txt = open(os.path.join(os.path.dirname(__file__), "prob022_names.txt"), 'r')
    names = txt.read().split(',')
    names.sort()    # sort alphabetically
    
    score = sum(value(names[i])*(i+1) for i in range(len(names)))
    return score

def value(name):
    return sum(ord(c)-64 for c in name)

if __name__ == "__main__":
    print(compute())