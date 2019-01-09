import re


def substring_concate_all_string(word, diction):
    word_index = {}
    index_word = {}
    all_index = []
    result = []
    for w in diction:
        word_index[w] = [x.start() for x in re.finditer(w, word)]
    for word, index_arr in word_index:
        for index in index_arr:
            index_word[index] = word

    all_index = [all_index + word_index[m] for m in word_index]
    sorted(all_index)
    for index in all_index:
        word_index_copy = word_index.copy()
        index_copy = index
        length = len(diction)

        i = 0
        while i < length:
            current_word = index_word[index_copy]
            next_word = index_word.get(index_copy + len(current_word))
            if word_index_copy[current_word] and next_word:
                word_index_copy[current_word] = False
                index_copy += len(current_word)
                i += 1
            else:
                break
        else:
            result.append(index)

    return result


substring_concate_all_string('barfoobar', ['bar', 'foo'])
