def reversed_polish_noation(strings):
    stk = []
    for nota in strings:
        if nota in '+-*/':
            a = stk[-1]
            b = stk[-2]
            del stk[-1]
            del stk[-1]
            c = eval(a + nota + b)
            stk.append(str(c))

        else:
            stk.append(nota)

    return stk[0]


if __name__ == '__main__':
    tests = [['1', '2', '+'], ['2', '1', '+',
                               '3', '*'], ['4', '13', '5', '/', '+']]
    for t in tests:
        print(t, '=', reversed_polish_noation(t))
