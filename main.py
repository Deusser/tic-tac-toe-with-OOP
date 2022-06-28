class Board:

    def __init__(self):
        self.board = {
            "1": " ", "2": " ", "3": " ",
            "4": " ", "5": " ", "6": " ",
            "7": " ", "8": " ", "9": " "}

    def print_board(self):
        print(self.board["1"] + "|" + self.board["2"] \
              + "|" + self.board["3"] + "|")
        print("-+" * 3)
        print(self.board["4"] + "|" + self.board["5"] \
              + "|" + self.board["6"] + "|")
        print("-+" * 3)
        print(self.board["7"] + "|" + self.board["8"] \
              + "|" + self.board["9"] + "|")

    def _is_valid_move(self, position):
        if self.board[position] == " ":
            return True
        return False

    def change_board(self, position, type):
        if self._is_valid_move(position):
            self.board[position] = type
            return self.board
        return None

    def is_winner(self, player):
        if self.board["1"] == player.type and self.board["2"] == player.type and self.board["3"] == player.type or \
                self.board["4"] == player.type and self.board["5"] == player.type and self.board[
            "6"] == player.type or \
                self.board["7"] == player.type and self.board["8"] == player.type and self.board[
            "9"] == player.type or \
                self.board["1"] == player.type and self.board["4"] == player.type and self.board[
            "7"] == player.type or \
                self.board["2"] == player.type and self.board["5"] == player.type and self.board[
            "8"] == player.type or \
                self.board["3"] == player.type and self.board["6"] == player.type and self.board[
            "9"] == player.type or \
                self.board["1"] == player.type and self.board["5"] == player.type and self.board[
            "BR"] == player.type or \
                self.board["7"] == player.type and self.board["5"] == player.type and self.board["3"] == player.type:
            return True
        return False


class Player:

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "Игрока с {}".format(self.type)


class Game:

    def __init__(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()

    def print_valid_entries(self):
        print("""
            1  |  2  |  3 
            4  |  5  |  6 
            7  |  8  |  9  """)

    def printing_board(self):
        self.board.print_board()

    def change_turn(self, player):
        if player is self.player1:
            return self.player2
        else:
            return self.player1

    def won_game(self, player):
        return self.board.is_winner(player)

    def modify_board(self, position, type):
        if self.board.change_board(position, type) is not None:
            return self.board.change_board(position, type)
        else:
            position = input("Клетка занята, попробуйте еще раз.")
            return self.board.change_board(position, type)


def play():
    game = Game()
    game.print_valid_entries()
    player = game.player1
    num = 9
    while num > 0:
        num -= 1
        game.printing_board()
        position = input("Ход {}, ваше действие? ".format(player))
        game.modify_board(position, player.type)
        if game.won_game(player):
            print("Игрок {} победил!".format(player))
            break
        else:
            player = game.change_turn(player)
    if num == 0:
        print("Игра закончена, ничья!")


play()
