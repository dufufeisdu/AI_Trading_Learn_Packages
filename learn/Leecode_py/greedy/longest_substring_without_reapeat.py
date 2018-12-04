# set dict = {}
# maxlen = 0
# substr = ''
# for each char in the arr:
# if char not in dict
# insert char
# increase sub_length
# else
# compare sub_length and update maxlen
# reset dict


def longest_substring(strs):
    ele_dict = {}
    maxlen = 0
    substring = ''
    sublen = 0
    left = 0
    i = 0
    while i < len(strs):
        ch = strs[i]
        if ch not in ele_dict:
            ele_dict[ch] = i
            sublen += 1
            i += 1
        else:
            if maxlen < sublen:
                maxlen = sublen
                substring = strs[left:i]
                left = ele_dict[ch] + 1
            sublen = 0
            i = ele_dict[ch] + 1
            ele_dict = {}
    return maxlen, substring


if __name__ == "__main__":
    tests = ['abcabcab', 'aaaaa', 'qpxrgxkltzyx']
    for test in tests:
        print(longest_substring(test))
