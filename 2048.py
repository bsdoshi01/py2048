# This is a game similar to 2048 game but the user gets to decide what is the size of the grid and the final number where the game is supposed to end

import random
import readchar

def game_initialize():
	game_size = int(input("Enter the size of the grid you would like to use in the game: "))
	game_limit = int(input("Enter the value at which you want to win the game in the above grid: "))
	game_board = [list([0] * game_size) for i in range(game_size)]
	return game_size, game_limit, game_board

def print_board(game_board, game_size):
	for i in range(game_size):
		for j in range(game_size):
			print(game_board[i][j], "  ", end='')
		print()
	print()

def get_user_input():
	print("Make your move as up, down, left, or right by using w, s, a, or d keys : ")
	usr_input = readchar.readkey()
	return usr_input

def board_initialize(game_board, game_size):
	game_board[random.choice(range(game_size))][random.choice(range(game_size))] = 2
	return game_board

def check_zeros(game_board, game_size):
	list_of_zeros_i = []
	list_of_zeros_j = []
	for i in range(game_size):
		for j in range(game_size):
			if game_board[i][j] == 0:
				list_of_zeros_i.append(i)
				list_of_zeros_j.append(j)
	return list_of_zeros_i, list_of_zeros_j

def add_zero_after_move(game_board, game_size, list_of_zeros_i, list_of_zeros_j):
	num_of_possible_zeros = len(list_of_zeros_i)
	if num_of_possible_zeros == 0:
		game_board(game_board, game_size)
	location_of_random_zero = random.randint(1, num_of_possible_zeros) - 1
	game_board[list_of_zeros_i[location_of_random_zero]][list_of_zeros_j[location_of_random_zero]] = 2
	return game_board

'''
def making_a_move(game_board, game_size, usr_input):
	if usr_input == 'w':
		for j in range(game_size):
			flag = False
			while not flag:
				count = 0
				for i in range(game_size):
					if game_board[i][j] == 0:
						count += 1
				if count == game_size:
					flag = True
				if count == game_size-1:
					for i in range(game_size):
						if game_board[i][j]:
							game_board[0][j], game_board[i][j] = game_board[i][j], 0
	return game_board
'''
'''
def making_a_move(game_board, game_size, usr_input):
	if usr_input == 'w':
		for j in range(game_size):
			i, last_zero = 0, 0
			while i < game_size:
				if game_board[i][j] != 0:
					if game_board[i-1][j] == 0 and i > 0:
						game_board[last_zero][j], game_board[i][j] = game_board[i][j], 0
					else:
						k = i + 1
						while k < game_size:
							if game_board[k][j] != 0:
								if game_board[k][j] == game_board[i][j]:
									game_board[i][j] *= 2
									game_board[k][j] = 0
								k = game_size
							else:
								k += 1
				else:
					last_zero = i
				i += 1
	return game_board
'''

def making_a_move(game_board, game_size, usr_input):
	if usr_input == 'w':
		for j in range(game_size):
			i = 0
			while i < game_size:
				if game_board[i][j] != 0 and i != 0:
					k = i - 1
					while k >= 0:
						if game_board[k][j] != 0:
							if game_board[k][j] == game_board[i][j]:
								game_board[k][j] *= 2
								game_board[i][j], k, i = 0, 0, k + 1
							elif game_board[k][j] != game_board[i][j] and k != 0:
								game_board[k+1][j], game_board[i][j] = game_board[i][j], 0
								k, i = 0, k + 2
						if k == 0 and game_board[k][j] == 0:
							game_board[k][j], game_board[i][j], i = game_board[i][j], 0, k + 1
						k -= 1
				i += 1
	return game_board

''' LOGIC:
- walk over the array from the first to the last number
  - for each original number in the array that is not zero
    - look backwards for a target position that does not contain a zero (unless it is position zero)
      - if the target position does not contain the original number use the next position
    - if the target position is different from the original position
      - add the number to the number on the target position
      - replace the original number by zero
'''

def game_over(game_board, game_size):
	print_board(game_board, game_size)
	print("This is the final game layout of your gameplay. You are out of spaces to continue playing further.")
	print("Thank you for playing")

if __name__ == "__main__":	
	game_size, game_limit, game_board = game_initialize()
	game_board = board_initialize(game_board, game_size)
	print_board(game_board, game_size)

	list_of_zeros_i, list_of_zeros_j = check_zeros(game_board, game_size)
	game_board = add_zero_after_move(game_board, game_size, list_of_zeros_i, list_of_zeros_j)
	print_board(game_board, game_size)

	game_over = False
	while not game_over:
		usr_input = get_user_input()
		game_board = making_a_move(game_board, game_size, usr_input)
		list_of_zeros_i, list_of_zeros_j = check_zeros(game_board, game_size)
		add_zero_after_move(game_board, game_size, list_of_zeros_i, list_of_zeros_j)	
		print_board(game_board, game_size)