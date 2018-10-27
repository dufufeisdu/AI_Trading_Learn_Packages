def distance(w1, w2):
    not_same = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            not_same += 1
    return not_same


def create_adj_matirx(word_dic):
    adj_matrix = []
    for word1 in word_dic:
        line_vec = []
        for word2 in word_dic:
            line_vec.append(int(distance(word1, word2) == 1))
        adj_matrix.append(line_vec)
    return adj_matrix
