class Board:
    SIZE = 3

    def __init__(self):
        self.grid = [[''for _ in range(self.SIZE)]for _ in range(self.SIZE)]
        self.turn = 'X'

    def next_turn(self):
        self.turn = ['X', 'O'][self.turn == 'X']

    def valid_move(self, row, col):
        return (0 <= row < self.SIZE)and\
               (0 <= col < self.SIZE)and\
               (self.grid[row][col] == '')

    def move(self, row, col):
        if not self.valid_move(row, col):
            raise ValueError("Wrong coordinates"+str((row, col)))
        self.grid[row][col] = self.turn
        self.next_turn()

    def with_move(self, row, col):
        nb = Board()
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                nb.grid[r][c] = self.grid[r][c]
        nb.turn = self.turn
        nb.move(row, col)
        return nb

    def winning_move(self, row, col):
        if not self.valid_move(row, col):
            raise ValueError("Wrong coordinates"+str((row, col)))
        self.grid[row][col] = self.turn
        res = 0
        winning = all(self.grid[r][col] == self.turn for r in range(self.SIZE))
        res += winning
        winning = all(self.grid[row][c] == self.turn for c in range(self.SIZE))
        res += winning
        winning = all(self.grid[cell][cell] == self.turn for cell in range(self.SIZE))
        res += winning
        winning = all(
            self.grid[cell][self.SIZE - 1 - cell] == self.turn
            for cell in range(self.SIZE)
        )

        res += winning
        self.grid[row][col] = ''
        return res

    def possible_moves(self):
        res = []
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                if not self.grid[row][col]:
                    res.append((row, col))
        return res

    def non_symetric_moves(self):
        moves = self.possible_moves()
        res = []
        for move1 in moves:
            unique = not any(self.with_move(move1[0], move1[1])\
                        .symetric_to(self.with_move(move2[0], move2[1])) for move2 in res)
            if unique:
                res.append(move1)
        return res

    def symetric_to(self, other):
        """

        :param other:
        :return:
        """
        def _rot(grid):
            new_grid = [[''for _ in range(self.SIZE)]for _ in range(self.SIZE)]
            for row in range(self.SIZE):
                for col in range(self.SIZE):
                    new_grid[row][col] = grid[col][row]
            return new_grid

        def _m_y(grid):
            new_grid = [[''for _ in range(self.SIZE)]for _ in range(self.SIZE)]
            for row in range(self.SIZE):
                for col in range(self.SIZE):
                    new_grid[-1-row][col] = grid[row][col]
            return new_grid

        def _m_x(grid):
            new_grid = [[''for _ in range(self.SIZE)]for _ in range(self.SIZE)]
            for row in range(self.SIZE):
                for col in range(self.SIZE):
                    new_grid[row][-1-col] = grid[row][col]
            return new_grid

        def _m_xy(grid):
            return _m_x(_m_y(grid))

        if not self.turn == other.turn:
            return False
        if self.grid == other.grid:
            return True
        for transform in [lambda grid:grid, _m_y, _m_x, _m_xy]:
            if self.grid == transform(other.grid):
                return True
            if self.grid == transform(_rot(other.grid)):
                return True
        return False

    def __str__(self):
        return '\n'.join(' '.join((self.grid[row][col]+'.')[0]
                                  for col in range(self.SIZE))
                         for row in range(self.SIZE))
