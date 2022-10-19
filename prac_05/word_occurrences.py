word_to_count = {}


words = input("Text: ").split()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
max_length = max(len(word) for word in word_to_count.keys())
for word in word_to_count.keys():
    print(f"{word:{max_length}} : {word_to_count[word]}")