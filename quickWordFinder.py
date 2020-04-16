#from src.WordHashTable import WordHashTable as wht

import csv

with open("./words.csv") as wordList:
    wordsReader = csv.reader(wordList)
    data = list(wordsReader)


tester = [None]
total = 0
matched = 0
for word in data:
    hashed = hash(word[0])
    if hashed in tester:
        matched += 1
    else:
        tester.append(hashed)
    total += 1
print(matched, " ", total, " ", total - matched)

uniques = [None]
unique = 0
for word in data:
    if word[0] not in uniques:
        unique += 1
        uniques.append(word[0])
print(unique)
print("done")