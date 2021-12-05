import collections
import colorama


colorama.init()


class Bingo:
    class Board:
        Square = collections.namedtuple("Square", "value matched")

        def __init__(self, lines):
            if len(lines) != 5:
                raise ValueError("bad input board")
            self._board = []
            for line in lines:
                row = []
                for value in line.split():
                    row.append(Bingo.Board.Square(value, False))
                self._board.append(row)
            self.last_number = None

        def __repr__(self):
            result = "\n"
            for row in self._board:
                for square in row:
                    color = colorama.Fore.GREEN if square.matched else colorama.Fore.RED
                    result += f"{color}{square.value:>2}{colorama.Style.RESET_ALL} "
                result += "\n"
            return result

        def update(self, value):
            for rindex, row in enumerate(self._board):
                for cindex, square in enumerate(row):
                    if square.value == value:
                        self._board[rindex][cindex] = Bingo.Board.Square(
                            square.value, True
                        )
            self.last_number = value

        def isWon(self):
            for row in self._board:
                if all([square.matched for square in row]):
                    return True
            transposed = zip(*self._board)
            for col in transposed:
                if all([square.matched for square in col]):
                    return True
            return False

        def score(self):
            if not self.isWon():
                return None
            total = 0
            for row in self._board:
                for square in row:
                    if not square.matched:
                        total += int(square.value)
            return total * int(self.last_number)

    def __init__(self, filename):
        with open(filename) as file:
            self.current_move = 0
            self.moves = file.readline().split(",")
            self.boards = []
            remaining_lines = file.readlines()
            while remaining_lines:
                self.boards.append(Bingo.Board(remaining_lines[1:6]))
                remaining_lines = remaining_lines[6:]

    def update(self):
        value = self.moves[self.current_move]
        for board in self.boards:
            board.update(value)
        self.current_move += 1

    def boardWon(self):
        for number, board in enumerate(self.boards):
            if board.isWon():
                return number
        return None

    def winning_score(self):
        while not self.boardWon():
            self.update()
        return self.boards[self.boardWon()].score()


if __name__ == "__main__":
    game = Bingo("input.txt")
    print(game.winning_score())
