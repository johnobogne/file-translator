dict = {}
words = ['hello', 'hi', 'thank you']
words_dict = {}
for word in words :
    words_dict[word] = words_dict.get(word, word)
print(words_dict)
