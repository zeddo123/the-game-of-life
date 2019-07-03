import env as en
import argparse

parser = argparse.ArgumentParser(description='Conway\'s game of life')
parser.add_argument('-g', '--generations', metavar='N', type=int, help='number of generation to loop over')
parser.add_argument('-s', '--size', metavar='N', type=int, help='size of the board')
parser.add_argument('-t', '--type', type=str, help='type of display', choices=['cli','gui'])

args = parser.parse_args()

if not args.type : args.type = 'cli'
if not args.generations : args.generations = 10
if not args.size : args.size = 10

env = en.init_env(args.size,args.size,(5,1),(5,2),(5,3))

if args.type == 'cli':
	# ---CLI version
	import os
	for i in range(args.generations):
		for i in range(10):
			for j in range(10):
				print('x',end='') if env[i,j] == True else print('.',end='')
			print()
		env = en.tick(env,env.shape[0],env.shape[1])
		input()
		os.system('clear')
else:
	# ---GUI version
	import matplotlib.pyplot as plt
	plt.ion()

	for i in range(args.generations):
		plt.clf()
		plt.matshow(env,fignum=False)
		plt.title('generation number ' + str(i))
		plt.draw()
		plt.pause(1)
		env = en.tick(env,env.shape[0],env.shape[1])

	plt.show()