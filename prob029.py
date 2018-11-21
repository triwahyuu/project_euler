s = 100
def compute():
    found = []
    for i in range(2,s+1):
        for j in range(2,s+1):
            x = i**j
            if x not in found: 
                found.append(x)
    
    return len(found)

if __name__ == "__main__":
    print(compute())