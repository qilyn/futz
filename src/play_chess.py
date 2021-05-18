"""
Implement a one-dimensional chess game that two users can play against
each other.

# Overview

In this version of one-dimensional chess, each colour has a king, a rook,
and a knight.

You can use KRN and nrk to represent the pieces:
- k = white king, K = black king
- r = white rook, R = black rook
- n = white knight, N = black knight

The board is one by eight:
knr  RNK
with white on the left.

# Recap of chess rules:

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

- How many games does each colour win? How many are draws?
- What's the longest* game that ends in a win?

*No, just moving the pieces forward and back again doesn't count.
"""

board = ['k', 'n', 'r', ' ', ' ', 'N', 'R', 'K']
