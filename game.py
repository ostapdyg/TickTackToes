from btree import BoardTree
from board import Board


class Game:
    def __init__(self, player='X'):
        self.board = Board()
        self.winner = ''
        self.player = player

    def mainloop(self):
        while not self.winner:
            print(self.board)
            if self.board.turn == self.player:
                move = input("Your move: ").split()
                move = [int(move[0]), int(move[1])]
            else:
                ai_res = BoardTree(self.board).find_best_move()
                print("AI moves to {} and predicts {}".format(ai_res[1],
                                                              ["a draw",
                                                               "his victory",
                                                               "his loss"]
                                                              [ai_res[0]]))
                move = ai_res[1]
            if self.board.winning_move(move[0], move[1]):
                print("{} wins!".format(["AI", "Player"][self.board.turn ==\
                                                         self.player]))
                self.winner = self.board.turn
            self.board.move(move[0], move[1])

game = Game()
game.mainloop()