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
            item = [int(distance(word1, word2) == 1), -1]
            line_vec.append(item)
        adj_matrix.append(line_vec)
    return adj_matrix


def word_path(sw, ew, word_dic):
    word_dic = [sw] + word_dic
    word_dic.append(ew)
    adj_matrix = create_adj_matirx(word_dic)
    return BFS(adj_matrix)


def BFS(adj_matrix):
    que = []
    size = len(adj_matrix)
    visited = [False for i in range(size)]

    for i in size:
        if adj_matrix[0][i] == 1:
            que.append((i, 1))
            visited[i] = True
    while que:
        poped = que[0]
        level = poped[1]
        del que[0]
        if poped[0] == size - 1:
            return level

        if not visited[poped[0]]:
            visited[poped[0]] = True
            for j in size:
                if adj_matrix[j] == 1 and not visited[j]:
                    que.append((j, level + 1))
    return -1


def find_path(mx, sw, ew, word_dic):
    path = []
    word_dic = sw + word_dic
    word_dic = word_dic + ew
    if mx[-1][-1][1] != -1:
        path.append(word_dic[-1])
        row = len(mx)
        col = len(mx)
        origin_num = mx[row][col][1]
        while origin_num != -1:
            origin_num = mx[row][col][1]
            path.append(word_dic[origin_num])
            col = row
            row = origin_num
    return path
