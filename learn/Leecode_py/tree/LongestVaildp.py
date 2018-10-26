# Longest vilid ()


def longestValidP(sti):
    stk = []
    validPnum = [0]
    for s in sti:
        if s == '(':
            stk.append(s)
            validPnum.append(validPnum[-1])
        else:
            if len(stk) == 0:
                validPnum.append(0)
            else:
                stk.pop()
                validPnum.append(validPnum[-1] + 2)
    # test
    print('final stack:', stk)
    print('final number array:', validPnum)
    return max(validPnum)


if __name__ == '__main__':
    tests = ['()', '()()', '(())', '((())', ')((((', ')()())']
    for t in tests:
        longestValidP(t)
