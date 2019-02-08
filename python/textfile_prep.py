# textfile pre-processing script
txt = open("prob042_words.txt", 'r')
tmp = txt.read().rstrip()
result = open("prob042.txt", 'w')

i = 0
while i < len(tmp)-1:
    if tmp[i] == '"':
        n = ''
        i += 1
        while tmp[i] != '"':
            n += tmp[i]
            i += 1
        result.write(n + ',')
        i += 1
    else: i += 1

txt.close()
result.close()