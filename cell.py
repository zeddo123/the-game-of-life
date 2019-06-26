def number_of_neighbours(env, x, y):
	h = env.shape[0]
	w = env.shape[1]
	number = 0 if env[x,y] == False else -1

	for i in range(x - 1, x + 2):
		for j in range(y - 1, y + 2):
			if i >= 0 and i < h and j >= 0 and j < w:
				if env[i,j] == True:
					number += 1;

	return number