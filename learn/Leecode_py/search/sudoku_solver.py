class Sudoku():
    def __init__(self, arr):
        self.arr = arr
        self.solution = []
        elements = {}
        self.blocks = [[elements.copy() for i in range(3)]for j in range(3)]
        self.horrizons = [elements.copy() for i in range(9)]
        self.verticals = [elements.copy() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if arr[i][j] != '.':
                    self.blocks[i // 3][j // 3].append(int(arr[i][j]) - 1)
                    self.horrizons[i].append([int(arr[i][j]) - 1])
                    self.verticals[j].append([int(arr[i][j]) - 1])

    def update_board(self, i, j, element):
        self.arr[i][j] = element
        self.blocks[i // 3][j // 3] = self.blocks[i // 3][j // 3] - element
        self.horrizons[i] = self.horrizons[i] - element
        self.verticals = self.verticals - element

    def check_board(self):
        pass

    def find_solution(self):
        if self.check_board() == -1:
            return
        if self.check_board() == 1:
            self.solution = self.arr

        for i in range(9):
            for j in range(9):
                if self.arr[i] == '.':
                    avilable_ele = {1, 2, 3, 4, 5, 6, 7,
                                    8, 9} - self.blocks[i // 3][j // 3]
                    avilable_ele = avilable_ele - self.horrizons[i]
                    avilable_ele = avilable_ele - self.verticals[j]
                    arr = self.arr
                    horrizons = self.horrizons
                    blocks = self.blocks
                    verticals = self.verticals
                    for ele in avilable_ele:
                        self.update_board(i, j, ele)
                        self.find_solution()

                        self.blocks = blocks
                        self.arr = arr
                        self.horrizons = horrizons
                        self.verticals = verticals
