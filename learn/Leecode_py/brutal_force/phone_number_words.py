word_dic = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def del_None_letter(string):
    deled = '01#*'
    for l in deled:
        if l in string:
            string = string.replace(l, '')
    return string


def phone_words(string):
    string = del_None_letter(string)
    return find_words_wraper(string)


def find_words_wraper(string):
    if not string:
        return ['']
    words_list = phone_words(string[1:])
    res = []
    for i in word_dic[string[0]]:
        w = [i + j for j in words_list]
        res = res + w
    return res


if __name__ == '__main__':
    A = '123*#11#*'
    print(del_None_letter(A))
    # print(phone_words(A))
