import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib import style

import env as en

style.use('fivethirtyeight')
fig = plt.figure(figsize=(10,10))

env = en.init_env(10,10,(5,1),(5,2),(5,3),(5,4))
print(env)
input()
def animate(i, env):
	env = en.tick(env,env.shape[0],env.shape[1])
	plt.matshow(env)
	plt.grid(b=False)

ani = anim.FuncAnimation(fig, animate, interval=100000, fargs=(env,))
plt.show()