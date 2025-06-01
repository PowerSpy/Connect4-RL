import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros((6,7))
        self.turn = 'YELLOW'
        self.winner = None
        self.gameover = False

    def play(self, col):
        # Validate col input inside the game loop, not here
        if self.winner:
            return  # No moves allowed after game ends

        for row in self.board[::-1]:
            if row[col] == 0:
                if self.turn == 'YELLOW':
                    row[col] = 1
                    self.turn = 'RED'
                else:
                    row[col] = 2
                    self.turn = 'YELLOW'
                break

        self.winner = self.check_win()
        if self.winner:
            self.gameover = True

    def check_win(self):
        for row in range(6):
            for col in range(7):
                player = self.board[row][col]
                if player == 0:
                    continue

                # Vertical
                if row < 3:
                    if player == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col]:
                        return player

                # Horizontal
                if col < 4:
                    if player == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3]:
                        return player

                # Diagonal (\)
                if row < 3 and col < 4:
                    if player == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3]:
                        return player

                # Diagonal (/)
                if row < 3 and col > 2:
                    if player == self.board[row + 1][col - 1] == self.board[row + 2][col - 2] == self.board[row + 3][col - 3]:
                        return player

        return None  # No winner

    def __str__(self):
        symbol_map = {
            0: '.',
            1: 'Y',
            2: 'R'
        }
        
        display_rows = []
        for row in self.board:
            display_row = ' | '.join(symbol_map[int(cell)] for cell in row)
            display_rows.append(f"| {display_row} |")

        header = '   '.join(str(i) for i in range(7))
        line_length = len(display_rows[0])
        separator = '-' * line_length
        board_display = '\n'.join(display_rows)

        if self.winner:
            winner_name = 'YELLOW' if self.winner == 1 else 'RED'
            return f"\n{winner_name} won!\n{separator}\n  {header}\n{separator}\n{board_display}\n{separator}"
        else:
            return f"{separator}\n  {header}\n{separator}\n{board_display}\n{separator}\nTurn: {self.turn}"


def get_valid_column(turn):
    while True:
        try:
            col = int(input(f"Play a move ({turn}'s turn): "))
            if 0 <= col <= 6:
                return col
            else:
                print("Invalid column. Choose a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 6.")


board = Board()
while not board.gameover:
    print(board)
    col = get_valid_column(board.turn)
    board.play(col)

print(board)
