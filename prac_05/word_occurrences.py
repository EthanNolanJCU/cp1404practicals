"""
Word Occurences
Estimate: 30mins
Actual: 5:33 mins
"""

word_to_count = {}

line = input("Enter line: ").lower
words = line.split()

for word in words:
    if word in word_to_count.keys():
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_word_len = max(len(word) for word in word_to_count.keys())
max_count_len = max(len(str(count)) for count in word_to_count.values())

for word, count in word_to_count.items():
    print(f"{word:<{max_word_len}} : {count:>{max_count_len}}")