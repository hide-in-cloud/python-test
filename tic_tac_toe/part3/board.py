"""

"""


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        for r in range(height):
            row = []
            for c in range(width):
                row.append(None)
            self.board.append(row)

    def render(self):
        print("  ", end="")
        for column in range(self.width):
            print(column + 1, end=" ")
        print()
        print(" -------")
        for row in range(self.height):
            output_row = ""
            for column in range(self.width):
                if self.board[row][column] is None:
                    output_row += " "
                else:
                    output_row += self.board[row][column]
            print("%d|%s|" % (row + 1, " ".join(output_row)))
        print(" -------")

    def update(self, co_ords, piece):
        row = co_ords[0]
        column = co_ords[1]
        self.board[row][column] = piece

    def get(self, co_ords):
        return self.board[co_ords[0]][co_ords[1]]
