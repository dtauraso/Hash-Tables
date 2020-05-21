# Implement me.


ignore_letters = {
    '\"': 1,
    ':': 1,
    ';': 1,
    ',': 1,
    '.': 1,
    '-': 1,
    '+': 1,
    '=': 1,
    '/': 1,
    '\\': 1,
    '|': 1,
    '[': 1,
    ']': 1,
    '{': 1,
    '}': 1,
    '(': 1,
    ')': 1,
    '*': 1,
    '^': 1,
    '&': 1
}

def word_count(s):
    # Implement me.

    if s == '':
        return {}

    frequency_table = {}

    # replace all variations of whitespace with ' '
    words = s.replace('\r', ' ')
    words = words.replace('\n', ' ')
    words = words.replace('\t', ' ')
    words = words.split(' ')

    for word in words:

        new_word = []
        for i, letter in enumerate(word):
            if letter not in ignore_letters:
                new_word.append(letter.lower())

        new_word = ''.join(new_word)
        # print(new_word)
        if len(new_word) > 0:
            if new_word not in frequency_table:
                frequency_table[new_word] = 1
            else:
                frequency_table[new_word] += 1

    # if all the separated words have ignorable chars then
    # the frequency_table will be empty
    return frequency_table


def make_characters(number, character):
    if number == 0:
        return ''
    else:
        return character + make_characters(number - 1, character)

def calculateSpaces(string, original_size):

    # for spacing the word and it's frequency count via hash characters
    # subtract spaces as much as the string is there
    if string == '':
        return make_characters(original_size, ' ')
    return calculateSpaces(string[1:], original_size - 1)

frequency_table = {}
with open("robin.txt") as f:
    words = f.read()
    # f.close()
# print(f.closed)
# print(words)
frequency_table = word_count(words)
# [print(i, frequency_table[i]) for i in frequency_table]
frequency_array = [(i, frequency_table[i]) for i in frequency_table]
# [print(i) for i in frequency_array]

x = sorted(frequency_array, key=lambda e: e[1], reverse=True)

histogram = [(i[0], make_characters(i[1], '#')) for i in x]

# the original number of spaces for printing is 17
[print(i[0], calculateSpaces(i[0], 17), i[1]) for i in histogram]

