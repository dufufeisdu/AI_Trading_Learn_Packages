from copy import deepcopy


def n_queen(n):
    boards = []
    for i in range(n):
        row = [0 for i in range(n)]
        board = [row.copy() for i in range(n)]
        board = find_board(deepcopy(board), n, 0, i)
        if board:
            boards.append(board)
    return boards


def find_board(boards, n, row, col):

    if row == n:
        return boards

    if boards[row][col] == '.':
        return []

    for i in range(n):
        for j in range(n):
            if i == row or j == col or \
               (i - j) == (row - col) or (i + j) == (row + col):
                boards[i][j] = '.'
    boards[row][col] = 'Q'

    for i in range(n):
        board = deepcopy(boards)
        board = find_board(board, n, row + 1, i)
        if board:
            return board


if __name__ == "__main__":
    print(n_queen(8))
