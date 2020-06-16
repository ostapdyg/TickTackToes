from btnode import BTNode
from random import shuffle
# 2 for task 3, 9 fr task 4
NUM_BRANCHES = 2



class BoardTree(BTNode):
    PRINTING_LOGS = False

    def __init__(self, board):
        super().__init__(board)

    def build_bin_tree(self):
        """
        Build binary tree with random moves
        :return:
        """
        moves = self.board.non_symetric_moves()
        shuffle(moves)
        for move in moves[:NUM_BRANCHES]:
            self.children.append(BoardTree(self.board.with_move(move[0],
                                                                move[1])))
        for child in self.children:
            child.build_bin_tree()
        return self

    def find_best_move(self, depth=1):
        """
        Build binary tree with random moves
        :return:
        """
        moves = self.board.non_symetric_moves()
        shuffle(moves)
        results = []
        if self.PRINTING_LOGS:
            print('\n'.join('| ' * depth +
                            line for line in
                            str(self.board).split('\n'))
                  )
            print(('| ' * depth) + "Possible moves", self.board.turn, moves)
        for move in tuple(moves[:NUM_BRANCHES]):
            if self.PRINTING_LOGS:
                print(('| ' * depth) + "Considering move:", self.board.turn,
                      str(move))

            if self.board.winning_move(move[0], move[1]):
                result = 1, move, 1, [move]
                if self.PRINTING_LOGS:
                    print(('| ' * depth) + "Winning move for",
                          self.board.turn, str(result))
                return result
            else:
                if len(moves) <= 1:
                    result = 0, move, 0, [move]
                    if self.PRINTING_LOGS:
                        print(('| ' * depth) + "A draw:", str(result))
                    return result

            nb = self.board.with_move(move[0], move[1])

            result = BoardTree(nb).find_best_move(depth+1)

            results.append((-result[0], move, -result[2], result[3]))

        score = 0
        for res in results:
            if res[0] == 1:
                score += res[2]
            if res[0] == -1:
                score -= res[2]

        score = round(score/len(results), 2)
        best_res = max(results, key=lambda r: r[0]+r[2]/100)
        if self.PRINTING_LOGS:
            print('| ' * (depth-1)+"Considered results :\n"+
                  '\n'.join('| ' * (depth - 1) + str(res) for res in results))
            print('| ' * (depth-1)+"Move results :",
                  best_res[0], best_res[1], score, [best_res[1]]+best_res[3])
        return best_res[0], best_res[1], score, [best_res[1]]+best_res[3]





