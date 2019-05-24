class Board:
    def __init__(self):
        self.grid = [['', '', ''],
                     ['', '', ''],
                     ['', '', '']]
        self.turn = 'X'

    def next_turn(self):
        self.turn = ['X', 'O'][self.turn == 'X']

    def valid_move(self, row, col):
        return (row, col) in self.possible_moves()

    def move(self, row, col):
        if not self.valid_move(row, col):
            raise ValueError("Wrong coordinates"+str((row, col)))
        self.grid[row][col] = self.turn
        self.next_turn()

    def with_move(self, row, col):
        nb = Board()
        for r in range(3):
            for c in range(3):
                nb.grid[r][c] = self.grid[r][c]
        nb.turn = self.turn
        nb.move(row, col)
        return nb

    def winning_move(self, row, col):
        if not self.valid_move(row, col):
            raise ValueError("Wrong coordinates"+str((row, col)))
        self.grid[row][col] = self.turn
        winning = True
        res = 0
        for r in range(0, 3):
            if self.grid[r][col] != self.turn:
                winning = False
        res += winning
        winning = True
        for c in range(0, 3):
            if self.grid[row][c] != self.turn:
                winning = False
        res += winning
        winning = True
        for cell in range(0, 3):
            if self.grid[cell][cell] != self.turn:
                winning = False
        res += winning
        winning = True
        for cell in range(0, 3):
            if self.grid[cell][2-cell] != self.turn:
                winning = False
        res += winning
        self.grid[row][col] = ''
        return res

    def possible_moves(self):
        res = []
        for row in range(3):
            for col in range(3):
                if not self.grid[row][col]:
                    res.append((row, col))
        return res

    def __str__(self):
        return '\n'.join(' '.join((self.grid[row][col]+'.')[0]for col in range(3))for row in range(3))
