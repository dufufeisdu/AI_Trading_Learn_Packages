from copy import deepcopy


def word_search(board, word):
    if len(board[0][0]) > 1:
        for i in range(len(board)):
            board[i] = list(board[i][0])

    row = len(board)
    col = len(board[0])
    board_state = [[True for i in range(col)]for j in range(row)]

    is_word_in_borad = False
    for r in range(row):
        for c in range(col):
            is_word_in_borad |= find_path(
                board, deepcopy(board_state), word, r, c)
    return is_word_in_borad


def find_path(board, board_state, word, r, c):
    if not word:
        return True
    if r < 0 or c < 0:
        return False
    if r >= len(board) or c >= len(board[0]):
        return False

    if not board_state[r][c]:
        return False

    if board[r][c] != word[0]:
        return False
    board_state[r][c] = False

    return find_path(board, deepcopy(board_state), word[1:], r + 1, c) \
        or find_path(board, deepcopy(board_state), word[1:], r - 1, c) \
        or find_path(board, deepcopy(board_state), word[1:], r, c + 1) \
        or find_path(board, deepcopy(board_state), word[1:], r, c - 1)


if __name__ == "__main__":
    board = [['ABCE'], ['SFCS'], ['ADEE']]
    words = ['ABCCED', 'SEE', 'ABCB']
    print([word_search(board, word) for word in words])
