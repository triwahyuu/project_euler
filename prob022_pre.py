# pre-processing script
txt = open("p022_names.txt", 'r')
tmp = txt.read().rstrip()
names = open("p022.txt", 'w')

i = 0
while i < len(tmp)-1:
    if tmp[i] == '"':
        n = ''
        i += 1
        while tmp[i] != '"':
            n += tmp[i]
            i += 1
        names.write(n + ',')
        i += 1
    else: i += 1

txt.close()
names.close()