import numpy as np
import cell

def init_env(h, w, *args):
	if h < 0 or w < 0:
		raise TypeError('the demensions cant be negativ')
	# initialization function

	# create a numpy array of cells (booleans)
	# h is the heigth
	# w is the weigth
	# *args are a tuple of x and y

	env = np.full((h,w), False, dtype=bool)

	for arg in args:
		if type(arg) != tuple: raise TypeError('arguments must a tuple')
		if len(arg) != 2: raise TypeError('arguments must a tuple of 2')
		if type(arg[0]) != int or type(arg[0]) != int : raise TypeError('arguments must be a tuple of ints')
		if arg[0] < 0 or arg[0] >= h: raise TypeError('the first arguments of the tuple must be a int between 0 and height -1')
		if arg[1] < 0 or arg[1] >= w: raise TypeError('the second arguments of the tuple must be a int between 0 and weigth -1')
		
		env[arg[0],arg[1]] = True

	return env

def tick(env, h, w):
	# applying the rules to every cell
	for i in range(h):
		for j in range(w):
			number_of_neighbours = cell.number_of_neighbours(env,i,j)
			if env[i,j] == False:
				if number_of_neighbours == 3:
					env[i,j] = True
			else:
				if number_of_neighbours < 2 or number_of_neighbours > 3:
					env[i,j] = False

	return env


