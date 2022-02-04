


def make_board():

	board = []

	for i in range(3):
		iboard = []
		board.append(iboard)

		for j in range(3):
			iboard.append([None])

	print(board)




testboard = [[["O"], ["X"], [None]], [[None], ["X"], [None]], [["O"], [None], [None]]]


def render(board):
	print("      ")
	print("  123 ")
	print("  --- ")

	for i in range(len(board)):
		print("%i|" % (i+1), end="")

		for j in board[i]:

			if j == ["X"]:
				print("X", end="")
			elif j == ["O"]:
				print("O", end="")
			else:
				print(" ", end="")

		
		print("|")


	print("  --- ")



def get_move():
	xinput = input("Which column? (1,2 or 3?)")
	yinput = input("Which row? (1,2 or 3?)")
	
	return (int(xinput), int(yinput))

#move = get_move()


def make_move(board, coord, player):

	newboard = board

	if player == 1:

		newboard[coord[0]-1][coord[1]-1] = "X"
		return newboard

	elif player == 2:

		newboard[coord[0]-1][coord[1]-1] = "O"
		return newboard
	else:
		print("Sorry try again")


#print(testboard[2,2])


make_move(testboard, (2,2), 2)
#('1','1')


