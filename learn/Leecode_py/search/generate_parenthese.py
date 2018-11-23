class GenParenthese():
    def __init__(self, num):
        self.num = num
        self.all_combine = []

    def generate_p(self, left_num, right_num, parenthes):
        if left_num == self.num:
            for i in range(left_num - right_num):
                parenthes += ')'
            self.all_combine.append(parenthes)
            return
        if left_num == right_num:
            self.generate_p(left_num + 1, right_num, parenthes + '(')
        else:
            self.generate_p(left_num + 1, right_num, parenthes + '(')
            self.generate_p(left_num, right_num + 1, parenthes + ')')


def generate_parenthese(num):
    g = GenParenthese(num)
    g.generate_p(0, 0, '')
    return g.all_combine


if __name__ == "__main__":
    print(generate_parenthese(3))
