sentence = 'The quick brown fox jumps over the lazy dog'
word_frequencies = {}
words = sentence.split()
for word in words:
    if word in word_frequencies:
        word_frequencies[word] += 1
    else:
        word_frequencies[word] = 1
print(word_frequencies)
