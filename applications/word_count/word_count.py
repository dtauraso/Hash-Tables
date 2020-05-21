
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


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))