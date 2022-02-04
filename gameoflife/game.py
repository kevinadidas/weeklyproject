import random
import time

DEAD = 0
LIVE = 1

def dead_state(width, height):

	#create a 5x5 board with lists

	#create a list 2x3
		#create a list to store lists inside []
			#insert "height" (3) [ [1], [2], [3]]
				#insert "width" (2) 

				#[ 
					# [ [1] [2] ]
					# [ [1] [2] ]
					# [ [1] [2] ]
	
	#ups =  [[DEAD for _ in range(height)] for _ in range(width)]
	#print(ups)


	return [[DEAD for _ in range(height)] for _ in range(width)]



def random_state(width, height):

	state = dead_state(width, height)

	cell_state = ""
	#randomize this shizz 

	for i in range(0, width):
		for j in range(0, height):
			
			random_number = random.random()
			

			if random_number >= 0.5:
				cell_state = 0
			else:
				cell_state = 1

			
			state[i][j] = cell_state

	return state

def state_width(state):
    """Get the width of a state.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    The width of the input state
    """
    return len(state)

def state_height(state):
    """Get the height of a state.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    The height of the input state
    """
    return len(state[0])


def render(state):
    """Displays a state by printing it to the terminal.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    Nothing - this is purely a display function.
    """
    display_as = {
        DEAD: ' ',
        LIVE: u"\u2588"
    }

    lines = []
    for y in range(0, state_height(state)):
        line = ''
        for x in range(0, state_width(state)):
            line += display_as[state[x][y]] 
        lines.append(line)
    print("\n".join(lines))




def next_cell_value(cell_coords, state):

	""" 
	Get the next value of a single cell in a state
	
	--------
	Params: 
	cell_coords: an (x,y) tuple of the co-ordinates of a cell
	state: the current state of the Game board

	-------
	Returns:
	new state of a cell - LIVE or DEAD
	"""

	width = state_width(state)
	height = state_height(state)
	x = cell_coords[0]
	y = cell_coords[1]
	n_live_neighbors = 0 

	#Iterate around this cell's neighbors 
	for x1 in range((x-1), (x+1)+1): 
		#Make sure we don't go off the edge of the board
		if x1 < 0 or x1 >= width: continue 

		for y1 in range((y-1), (y+1)+1):
			#make sure we dont get off the edge of the board
			if y1 < 0 or y1 >= height: continue
			#make sure we dont count the cell as a neighbor of itself
			if x1 == x and y1 == y: continue 

			if state[x1][y1] == LIVE:
				n_live_neighbors += 1

	if state[x][y] == LIVE: 
		if n_live_neighbors <= 1:
			return DEAD
		elif n_live_neighbors <=3:
			return LIVE
		else:
			return DEAD

	else:
		if n_live_neighbors == 3:
			return LIVE
		else: 
			return DEAD



def next_board_state(init_state):
	"""
	Takes a single step in the game 

	------
	Parameters:
	init_state: initial state of the game

	------
	Returns: 
	the next state of the game board, after taking one step for every 
	cell in the previous state

	"""

	width = state_width(init_state)
	height = state_height(init_state)
	next_state = dead_state(width, height)

	for x in range(0, width):
		for y in range(0, height):
			next_state[x][y] = next_cell_value((x,y), init_state)

	return next_state
	



def run_forever(init_state):
    """Runs the Game of Life forever, starting from the given initial state.
    Parameters
    ----------
    init_state: the Game state to start at
    Returns
    -------
    This function never returns - the program must be forcibly exited!
    """
    next_state = init_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.03)

if __name__ == "__main__":
    init_state = random_state(60, 30)
    # init_state = load_board_state('./toad.txt')
    run_forever(init_state)