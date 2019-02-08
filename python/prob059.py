import csv

def compute():
    cipher_text = load_data()
    best_key = max(((x,y,z)
                    for x in range(97, 123)
                    for y in range(97, 123)
                    for z in range(97, 123)),
                    key=lambda cipher_key: get_score(decrypt(cipher_text, cipher_key)))
    ans = sum(decrypt(cipher_text, best_key))
    return ans

def get_score(txt):
    score = 0
    for c in txt:
        if 0x41 <= c <= 0x5A:   # if upper case ASCII, good (A-Z)
            score += 1
        elif 0x61 <= c <= 0x7A: # if lower case ASCII, best (a-z)
            score += 2
        elif c <= 0x1F or c == 0x7F:    # if control char, worst
            score -= 10
    return score

def decrypt(cipher, key):
    return [c ^ key[n % len(key)] for (n,c) in enumerate(cipher)]

def load_data():
    data_file = open('prob059_cipher.txt')
    row = csv.reader(data_file, delimiter=',')
    c = [r for r in row]
    return [int(a) for a in c[0]]

if __name__ == "__main__":
    print(compute())