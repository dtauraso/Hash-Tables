import random



my_words = []
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    
    # for word in words:

    #     my_words.append(word)
    # print(words)
    # if word not in word_table:
my_words = words.split(' ')
my_words2 = []
for word in my_words:
    for split_words in word.split('\n'):
        if split_words != '':
            my_words2.append(split_words)

# print(my_words2)
# TODO: analyze which words can follow other words
word_table = {}
# current = my_words2[0]
# next_ = my_words2[1]
for i, word in enumerate(my_words2):
    # print(i)

    # last word will not have anything following it
    if i < len(my_words2) - 1:
        if word in word_table:
            word_table[word].append(my_words2[i + 1])
        else:
            word_table[word] = []
[print(i, word_table[i]) for i in word_table]
# TODO: construct 5 random sentences
