from src.WordHashTable import WordHashTable

import csv

with open("./words.csv") as word_list:
    wordsReader = csv.reader(word_list)
    data = list(wordsReader)
word_list.close()

hash_table = WordHashTable()

for word in data:
    hash_table.insert(word[0])


#hash_table.print_table()
hash_table.print_stats()
#hash_table.print_bucket_stats()
print(hash_table.has("boat"))
 