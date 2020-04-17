from src.WordHashTable import WordHashTable

import csv

with open("./words.csv") as wordList:
    wordsReader = csv.reader(wordList)
    data = list(wordsReader)

hash_table = WordHashTable()

for word in data:
    hash_table.insert(word[0])


#hash_table.print_table()
hash_table.print_stats()
hash_table.print_bucket_stats()
 