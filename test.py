import gym
import gymfc
import numpy as np
env=gym.make('AttFC_GyroErr-MotorVel_M4_E-v1')
env.render()
ac=np.array([0.1,0.1,0.1,0.1])
while True:
	ob, reward, done, info = env.step(ac)
	print(reward)
	if done:
		env.reset()
		
	
