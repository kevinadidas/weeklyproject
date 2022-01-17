import copy 

class GameBoard(object):

	def __init__(self,battleships, width, height):
		self.battleships = battleships
		self.shots = []
		self.width = width
		self.height = height

	# *Update Battleship with any hits
	# *Save the fact that the shot was 
	# a hit or miss
	def take_shot(self, shot_location):
		is_hit = False
		for b in self.battleships:
			idx = b.body_index(shot_location)
			if idx is not None:
				is_hit = True
				b.hits[idx] = True
				break

		self.shots.append(Shot(shot_location, is_hit))

	def is_game_over(self):
		for b in self.battleships:
			if not b.is_destroyed():
				return False
		return True
		#for each battleship, is it destroyed?
		#If yes for all, return True, else False



class Shot(object):

	def __init__(self, location, is_hit):
		self.location = location
		self.is_hit = is_hit

class Battleship(object):

	@staticmethod
	def build(head, length, direction):
		body = []
		for i in range(length):
			if direction == "N":
				el = (head[0], head[1] - i )
			elif direction == "S":
				el = (head[0], head[1] + i )
			elif direction == "W":
				el = (head[0] - i, head[1])
			elif direction == "E":
				el = (head[0] + i, head[1])

			body.append(el)
		
		return Battleship(body)


	def __init__(self, body):
		self.body = body
		# [False, False, True, False]
		self.hits = [False] * len(body)

	def body_index(self, location):
		try:
			return self.body.index(location)
		except ValueError:
			return None

	def is_destroyed(self):
		return all(self.hits)


def render(game_board, show_battleships=False):
	header = "+" + "-" * game_board.width + "+"
	print(header)

	#construct empty board
	board = []
	for _ in range(game_board.width):
		board.append([None for _ in range(game_board.height)])

	if show_battleships:
	#add the battleship to the board
		for b in game_board.battleships: 
			for x, y in b.body:
				board[x][y] = "O"



	#add shots to the board
	for sh in game_board.shots:
		x, y = sh.location
		if sh.is_hit:
			ch = "X"
		else:
			ch = "."
		board[x][y] = ch







	for y in range(game_board.height):
		row = []
		for x in range(game_board.width):
			row.append(board[x][y] or " ")
		print("|" + "".join(row) + "|")


	print(header)





if __name__ == "__main__":

	

	battleships = [
		Battleship.build((1,1), 2, "N"),
		Battleship.build((5,8), 5, "N"),
		Battleship.build((2,3), 4, "E")
	]

	game_boards = [
		GameBoard(battleships, 10, 10),
		GameBoard(copy.deepcopy(battleships), 10, 10),

	]

	player_names = [
	"Frank",
	"Alice",

	]

	offensive_idx = 0

	#for b in battleships:
	#	print(b.body)

	#game_board = GameBoard(battleships, 10, 10)
	#shots = [(1,1), (0,0), (5,7)]
	#for sh in shots:
	#	game_board.take_shot(sh)

	#render(game_board)
	# for sh in game_board.shots:
	# 	print(sh.location)
	# 	print(sh.is_hit)
	# 	print("========")

	# for b in game_board.battleships:
	# 	print(b.body)
	# 	print(b.hits)
	# 	print("========")


	#exit(0)




	#shots = []


	while True:
		#defensive player is the non-offnesive one
		defensive_idx = (offensive_idx + 1) % 2 

		defensive_board = game_boards[defensive_idx]

		print("%s YOUR TURN!" % player_names[offensive_idx])
		inp = input("Where dof you want to shoot?\n" )
		#TODO DEAL WITH UNVALID INPUT
		xstr, ystr = inp.split(",")
		x = int(xstr)
		y = int(ystr)

		defensive_board.take_shot((x,y))
		render(defensive_board)
		#render(10,10,shots)

		if defensive_board.is_game_over():
			print("%s WINS!" % player_names[offensive_idx])
			break

		#offensive olayer becomes previous defensive player
		offensive_idx = defensive_idx

		#if game_has_ended: 
		#	print "YOU WIN"
		#	break



