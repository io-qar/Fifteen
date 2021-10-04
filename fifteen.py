from random import shuffle
from tkinter import Canvas, Tk

class Model:
    def __init__(self, b_size, s_size):
		self.BOARD_SIZE = 3
		self.SQUARE_SIZE = 80
		self.EMPTY_SQUARE = BOARD_SIZE ** 2
		
	def is_solvable(self):
		num_inversions = controllerBoard.get_inv_count()
		if self.BOARD_SIZE % 2 != 0:
			return num_inversions % 2 == 0
		else:
			empty_square_row = self.BOARD_SIZE - (board.index(self.EMPTY_SQUARE) // self.BOARD_SIZE)
			if empty_square_row % 2 == 0:
				return num_inversions % 2 != 0
			else:
				return num_inversions % 2 == 0
        
    def info(self):
		return "Ваше поле:" + str(self.BOARD_SIZE) + " на " + str(self.BOARD_SIZE) + ", и имеет размер " + str(self.SQUARE_SIZE)
	
class Controller:
	def get_inv_count(self):
		inversions = 0
		inversion_board = board[:]
		inversion_board.remove(modelBoard.EMPTY_SQUARE)

		for i in range(len(inversion_board)):
			first_item = inversion_board[i]
			for j in range(i+1, len(inversion_board)):
				second_item = inversion_board[j]
				if first_item > second_item:
					inversions += 1
		return inversions
	
    def get_empty_neighbor(self, cl_index):
		empty_index = board.index(modelBoard.EMPTY_SQUARE)
		abs_value = abs(empty_index - cl_index)
		if abs_value == modelBoard.BOARD_SIZE:
			return empty_index
		elif abs_value == 1:
			max_index = max(cl_index, empty_index)
			if max_index % modelBoard.BOARD_SIZE != 0:
				return empty_index
		return cl_index

	def click(self, event):
		x, y = event.x, event.y

		x //= modelBoard.SQUARE_SIZE
		y //= modelBoard.SQUARE_SIZE

		board_index = x + (y * modelBoard.BOARD_SIZE)
		empty_index = controllerBoard.get_empty_neighbor(board_index)
		board[board_index], board[empty_index] = board[empty_index], board[board_index]
		viewBoard.draw_board()
		if board == correct_board:
			viewBoard.show_victory_plate()

class View:
	def draw_board(self):
		c.delete('all')
		for i in range(modelBoard.BOARD_SIZE):
			for j in range(modelBoard.BOARD_SIZE):
				index = str(board[modelBoard.BOARD_SIZE * i + j])
				if index != str(modelBoard.EMPTY_SQUARE):
					c.create_rectangle(
						j * modelBoard.SQUARE_SIZE, i * modelBoard.SQUARE_SIZE,
						j * modelBoard.SQUARE_SIZE + modelBoard.SQUARE_SIZE,
						i * modelBoard.SQUARE_SIZE + modelBoard.SQUARE_SIZE,
						fill = '#43ABC9',
						outline = '#FFFFFF'
					)
					c.create_text(
						j * modelBoard.SQUARE_SIZE + modelBoard.SQUARE_SIZE / 2,
						i * modelBoard.SQUARE_SIZE + modelBoard.SQUARE_SIZE / 2,
						text = index,
						font = "Arial {} italic".format(int(modelBoard.SQUARE_SIZE / 4)),
						fill = '#FFFFFF'
					)
                    
	def show_victory_plate(self):
		c.create_rectangle(
			modelBoard.SQUARE_SIZE / 5,
			modelBoard.SQUARE_SIZE * modelBoard.BOARD_SIZE / 2 - 10 * modelBoard.BOARD_SIZE,
			modelBoard.BOARD_SIZE * modelBoard.SQUARE_SIZE - modelBoard.SQUARE_SIZE / 5,
			modelBoard.SQUARE_SIZE * modelBoard.BOARD_SIZE / 2 + 10 * modelBoard.BOARD_SIZE,
			fill = '#000000',
			outline = '#FFFFFF'
		)
		c.create_text(
			modelBoard.SQUARE_SIZE * modelBoard.BOARD_SIZE / 2,
			modelBoard.SQUARE_SIZE * modelBoard.BOARD_SIZE / 1.9,
			text = "Victory!",
			font = "Helvetica {} bold".format(int(10 * modelBoard.BOARD_SIZE)),
			fill = '#DC143C'
		)

	def show_error_plate(self):
		c.create_rectangle(
			modelBoard.SQUARE_SIZE / 5,
			modelBoard.SQUARE_SIZE * modelBoard.BOARD_SIZE / 2 - 10 * modelBoard.BOARD_SIZE,
			modelBoard.BOARD_SIZE * modelBoard.SQUARE_SIZE - modelBoard.SQUARE_SIZE / 5,
			modelBoard.SQUARE_SIZE * modelBoard.BOARD_SIZE / 2 + 10 * modelBoard.BOARD_SIZE,
			fill = '#000000',
			outline = '#FFFFFF'
		)
		c.create_text(
			modelBoard.SQUARE_SIZE * modelBoard.BOARD_SIZE / 2,
			modelBoard.SQUARE_SIZE * modelBoard.BOARD_SIZE / 1.9,
			text = "FATAL ERROR!",
			font = "Helvetica {} bold".format(int(10 * modelBoard.BOARD_SIZE)),
			fill = '#DC143C'
		)

modelBoard = Model(3, 80)
controllerBoard = Controller()
viewBoard = View()
    
root = Tk()
c = Canvas(
	root,
	width = modelBoard.BOARD_SIZE * modelBoard.SQUARE_SIZE,
	height = modelBoard.BOARD_SIZE * modelBoard.SQUARE_SIZE,
	bg = '#808080'
)

c.pack()
c.bind('<Button-1>', controllerBoard.click)
c.pack()

board = list(range(1, modelBoard.EMPTY_SQUARE + 1))
correct_board = board[:]
shuffle(board)

while not modelBoard.is_solvable():
    shuffle(board)
	
viewBoard.draw_board()
root.mainloop()
