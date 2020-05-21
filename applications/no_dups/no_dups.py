def no_dups(s):
    # Implement me.
    if s == '':
        return ''
    words = s.split()

    frequency_table = {}
    new_words = []
    for word in words:
        if word not in frequency_table:
            frequency_table[word] = 1
            new_words.append(word)
    return ' '.join(new_words)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))