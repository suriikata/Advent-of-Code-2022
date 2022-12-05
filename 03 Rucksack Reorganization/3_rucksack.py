
with open('03 Rucksack Reorganization\input.txt', 'r') as f:
    rucksacks = f.readlines()
    rucksacks = list(map(str.strip, rucksacks))

""" Part I """
def get_priority(letter):
    if letter.isupper() == False:
        priority = ord(letter) - 96             # ascii code for 'a' is by default 97
    else:
        priority = ord(letter) - 38             # ascii code for 'A' is by default 65

    return priority


def get_poncke(rucksacks):
    poncki = []
    for rucksack in rucksacks:
        firstpart, secondpart = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        presek = set(firstpart) & set(secondpart)
        poncki.extend(presek)       # appending more than one value on list

    result = 0
    for poncka in poncki:
        result += get_priority(poncka)

    return result

# print(get_poncke(rucksacks))

""" Part II """

def trojcki(rucksacks):
    poncarji = []
    for index in range(0, len(rucksacks)):
        if index % 3 == 2:
            presek = set(rucksacks[index - 2]) & set(rucksacks[index - 1]) & set(rucksacks[index])
            poncarji.extend(presek)

    result = 0
    for poncarja in poncarji:
        result += get_priority(poncarja)

    return result


print(trojcki(rucksacks))

