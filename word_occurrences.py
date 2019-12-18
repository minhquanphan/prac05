words = input("Text:").split(" ")
words.sort()
word_to_occurrences = {}

for word in words:
    if word not in word_to_occurrences:
        word_to_occurrences[word] = 1
    else:
        word_to_occurrences[word] += 1

max_word_length = max(len(word) for word in words)
for key in word_to_occurrences:
    print("{:{}} : {}".format(key, max_word_length, word_to_occurrences[key]))