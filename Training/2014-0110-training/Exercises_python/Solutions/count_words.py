import data1


def count(lines):
    word_dict = {}
    for line in lines:
        words = line.split()
        for word in words:
            word = word.lower()
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict


def test():
    content = data1.Content
    word_dict = count(content)
    words = word_dict.keys()
    words.sort()
    for word in words:
        print 'Word: "%s" -- Count: %d' % (word, word_dict[word], )


test()
