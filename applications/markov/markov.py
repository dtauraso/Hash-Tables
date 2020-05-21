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
# "I'll []
for i, word in enumerate(my_words2):
    # print(i)

    # last word will not have anything following it
    if i < len(my_words2) - 1:
        if word in word_table:
            word_table[word].append(my_words2[i + 1])
        else:
            word_table[word] = [my_words2[i + 1]]
# [print(i, word_table[i]) for i in word_table]
# TODO: construct 5 random sentences

start_words = [i for i in word_table
    if i[0] == '\"' or (i[0] >= 'A' and i[0] <= 'Z')
]
# first word doesn't have anything
my_start_words = [  start_words[0],
                    start_words[1],
                    start_words[2],
                    start_words[3],
                    start_words[4]]
# print(my_start_words)

def is_end_word(tracker):
    # print(tracker)
    # if((tracker[len(tracker) - 1] == '.') or (tracker[len(tracker) - 1] == '?') or (tracker[len(tracker) - 1] == '!') or (tracker[len(tracker) - 1] == '\"')):
        
    #     return True
    # else:
    #     print('not end word')
    #     return False
    return  tracker[-1] == '.' or tracker[-1] == '?' or tracker[-1] == '!' or tracker[-1] == '\"'

def make_sentence(start_word):

    tracker = start_word
    sentence = []
    while(not is_end_word(tracker)):
        sentence.append(tracker)
        # print(tracker, word_table[tracker])
        tracker = random.choice(word_table[tracker])
    # add the end word
    sentence.append(tracker)
    # print(sentence)
    return sentence


sentences = [make_sentence(word) for word in my_start_words]

for sentence in sentences:
    print(' '.join(sentence))
    print()
    # find 5 start words

# traverse through each start word till we find an end word and save all the random choices
# we find
