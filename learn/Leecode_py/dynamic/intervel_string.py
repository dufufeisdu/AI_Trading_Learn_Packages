def intervel_string(s, sa, sb):
    if not s:
        return False
    if not sa:
        if s != sb:
            return False
        else:
            return True
    if not sb:
        if s != sa:
            return False
        else:
            return True

    if sa[0] != s[0] and sb[0] != s[0]:
        return False
    else:
        if sa[0] == s[0] and sb[0] == s[0]:
            return intervel_string(s[1:], sa[1:], sb) or intervel_string(s[1:], sa, sb[1:])
        elif sa[0] == s[0]:
            return intervel_string(s[1:], sa[1:], sb)
        else:
            return intervel_string(s[1:], sa, sb[1:])

# mixture of recursion and iteration


def intervel_string_Mix(s, sa, sb):
    if not len(s) != (len(sa) + len(sb)):
        return False
    if not sa:
        if s != sb:
            return False
        else:
            return True
    if not sb:
        if s != sa:
            return False
        else:
            return True
    k = len(s)
    a = 0
    b = 0
    for i in range(k):
        if sa[a] != s[i] and sb[b] != s[i]:
            return False
        if sa[a] == s[i] and sb[b] == s[i]:
            return intervel_string_Mix(s[i + 1:], sa[a + 1:], sb[b:]) or intervel_string_Mix(s[i + 1:], sa[a:], sb[b + 1:])
        elif sa[a] == s[i]:
            a += 1
        else:
            b += 1
    return True


if __name__ == "__main__":
    tests = [['aadbbcbcac', 'aabcc', 'dbbca'],
             ['aadbbbaccc', 'aabcc', 'dbbca']]
    for test in tests:
        print(intervel_string_Mix(*test))
