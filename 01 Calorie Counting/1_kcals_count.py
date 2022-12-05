
with open('01 Calorie Counting\input.txt', 'r') as f:
    data = f.readlines()

def puciga(spucancki):
    listic = []
    result = 0
    for spucanc in spucancki:
        if spucanc == '':
            listic.append(result)
            result = 0
            continue
        result += int(spucanc)

    listic.append(result)         # robni pogojnik
    #print(max(listic)
    listic.sort(reverse=True)
    print(sum(listic[:3]))

spucancki = [line.rstrip()for line in data]
# spucancki = ['3', '1', '', '6', '', '5']
puciga(spucancki)







