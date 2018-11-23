## highest length of words in the text is 14 char, say 10 char in a word
## use Z the value is 260, so let's use triangle number value up to 260
triangle_number = [sum(i for i in range(1,j)) for j in range(1,25)]

def compute():
    txt = open("prob042_words.txt", 'r')
    words = txt.read().split(',')
    ans = sum(1 for w in words if is_triangle(w))
    return ans

def is_triangle(word):
    word_val = sum((ord(i)-64) for i in word)
    if word_val in triangle_number:
        return True
    else:
        return False

if __name__ == "__main__":
    print(compute())