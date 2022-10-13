"""
Word Occurences
Estimate: 30mins
Actual: 7:33 mins
"""
from operator import itemgetter

word_to_count = {}

line = input("Enter line: ").lower()
words = line.split()

for word in words:
    if word in word_to_count.keys():
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_word_len = max(len(word) for word in word_to_count.keys())
max_count_len = max(len(str(count)) for count in word_to_count.values())

word_to_count = dict(sorted(word_to_count.items()))

for word, count in word_to_count.items():
    print(f"{word:<{max_word_len}} : {count:>{max_count_len}}")