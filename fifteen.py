from random import shuffle
from tkinter import Canvas, Tk

BOARD_SIZE = 3
SQUARE_SIZE = 80
EMPTY_SQUARE = BOARD_SIZE ** 2

def is_solvable():
    num_inversions = get_inv_count()
    if BOARD_SIZE % 2 != 0:
        return num_inversions % 2 == 0
    else:
        empty_square_row = BOARD_SIZE - (board.index(EMPTY_SQUARE) // BOARD_SIZE)
        if empty_square_row % 2 == 0:
            return num_inversions % 2 != 0
        else:
            return num_inversions % 2 == 0

def draw_board():
    c.delete('all')
   	for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            index = str(board[BOARD_SIZE * i + j])
            if index != str(EMPTY_SQUARE):
                c.create_rectangle(
					j * SQUARE_SIZE, i * SQUARE_SIZE,
                    j * SQUARE_SIZE + SQUARE_SIZE,
                    i * SQUARE_SIZE + SQUARE_SIZE,
                    fill = '#43ABC9',
                    outline = '#FFFFFF'
				)
                c.create_text(
					j * SQUARE_SIZE + SQUARE_SIZE / 2,
                    i * SQUARE_SIZE + SQUARE_SIZE / 2,
                    text = index,
                    font = "Arial {} italic".format(int(SQUARE_SIZE / 4)),
                    fill = '#FFFFFF')

class Model:
	...
	
class Controller:
	...
	
class View:
	...

root = Tk()
c = Canvas(
	root,
	width = modelBoard.BOARD_SIZE * modelBoard.SQUARE_SIZE,
	height = modelBoard.BOARD_SIZE * modelBoard.SQUARE_SIZE,
	bg = '#808080'
)

c.pack()
c.bind('<Button-1>', click)
c.pack()
root.mainloop()

board = list(range(1, EMPTY_SQUARE + 1))
correct_board = board[:]
shuffle(board)

while not is_solvable():
    shuffle(board)
	
draw_board()
root.mainloop()
