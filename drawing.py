import os
import env as en

env = en.init_env(10,10,(5,1),(5,2),(5,3))

while True:
	for i in range(10):
		for j in range(10):
			print('x',end='') if env[i,j] == True else print('.',end='')
		print()
	env = en.tick(env,env.shape[0],env.shape[1])
	input()
	os.system('clear')