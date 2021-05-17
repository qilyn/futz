"""
Implement a one-dimensional chess game that two users can play against 
each other.

# One-dimensional chess

In this version of one-dimensional chess, each colour has a king, a rook, 
and a knight. 

You can use KRN and nrk to represent the pieces:
- k = white king, K = black king
- r = white rook, R = black rook
- n = white knight, N = black knight

The board is one by eight:
KRN  nrk
with white on the left.

# Chess rules:

## Game end
The game can end in two ways:
- winning: one side puts the other in checkmate
- a draw: the current player cannot make any legal moves but is not in check

The king cannot move into check (a space that an enemy piece threatens).
A player cannot make a move that puts their own king into check.

## Movement
- King: one space left or right
- Rook: any number of spaces left or right
- Knight: two squares left or right; it can jump over pieces.

# Extra

- Iterate through all possible games. How many does each colour win and how many draws are there?
- What's the longest* game that ends in a win?

*No, just moving the pieces forward and back again doesn't count. 
"""

class Piece:
    # W_KING = '♔'
    # W_ROOK = '♖'
    # W_KNIGHT = '♘'
    # B_KING = '♚'
    # B_ROOK = '♜'
    # B_KNIGHT = '♞'
    B_KING = 'K'
    B_ROOK = 'R'
    B_KNIGHT = 'N'
    W_KING = 'k'
    W_ROOK = 'r'
    W_KNIGHT = 'n'

    BLACK = {B_KNIGHT, B_KING, B_ROOK}
    WHITE = {W_KNIGHT, W_KING, W_ROOK}

class Board:
    white_turn = True

    E = ' '
    def __init__(self):
        self.pretty_board = [
            Piece.W_KING, Piece.W_ROOK, Piece.W_KNIGHT, 
            self.E, self.E, 
            Piece.B_KNIGHT, Piece.B_ROOK, Piece.B_KING,
        ]

    def __str__(self):
        return (
            (' '.join(self.pretty_board)) + '\n' +
            (' '.join([str(i) for i in range(1,9)]))
        )

    def get_piece(self, piece: str):
        x = self.pretty_board.index(piece)
        print(x)
        return x
    
    def collides_with_own_piece(from_piece, to_piece):
        if ({from_piece, to_piece} | Piece.BLACK) == Piece.BLACK:
            return True        

    # def move_piece(self, from, to):
    #     if 
    def move_knight(self, from, to):
        if (from - to != 2) and (to + from != 2):
            print('Can\'t move there.')
            return False

        self.move_piece(self, from, to)

    def move(self, piece: str, to: int):
        to = to - 1  # decrement for use as array index

assert Board().get_piece('k') == 0
assert Board().get_piece('r') == 1
assert Board().get_piece('n') == 2

assert Board().collides_with_own_piece('k', 'n')

board = Board()
playing = True

while playing:
    print(board)
    result = input('waiting')
    if result == 'q':
        playing = False
    print(result)