# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:31:59 2021

@author: Murat Kerem Kara
"""

import gym
import numpy as np
import random
import matplotlib.pyplot as plt

env = gym.make("Taxi-v3").env

# Q table
q_table=np.zeros([env.observation_space.n, env.action_space.n])

# hyper parameter
alpha = 0.1
gamma = 0.9
epsilon = 0.1

# plotting metrix
reward_list = []
dropouts_list = []


episode_number=10000
for i in range(1,episode_number):
    # initialize enviroment
    state = env.reset()
    
    reward_count = 0
    dropouts = 0
    
    while True:
        # exploit vs explore to find action
               # %10 = explore , %90 = exploit
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])            
                                   
        
        # action process and take reward / observation
        next_state, reward, done, _ = env.step(action)
        
        
        # Q learning fuction
        old_value = q_table[state, action]  # define old_value
        next_max = np.max(q_table[next_state]) # define next_max
        
        
        next_value = (1-alpha)*old_value + alpha*(reward + gamma*next_max)
        
        
        # Q table update 
        q_table[state, action] = next_value
        
        # update state
        state = next_state
        
        # find wrong dropouts
        if reward == -10:
            dropouts+=1
        
        if done:
            break
        
        reward_count += reward
    if i%10 == 0:   
        dropouts_list.append(dropouts)
        reward_list.append(reward_count)
        print("Episode: {}, reward {}, wrong dropout {}".format(i,reward_count,dropouts))
        
# %%

fig, axs = plt.subplots(1,2)
axs[0].plot(reward_list)
axs[0].set_xlabel("episode")
axs[0].set_ylabel("reward")

axs[1].plot(reward_list)
axs[1].set_xlabel("episode")
axs[1].set_ylabel("dropouts")

axs[0].grid(True)
axs[1].grid(True)

plt.show()

# %% q table

"""
 Actions:
    There are 6 discrete deterministic actions:
    - 0: move south
    - 1: move north
    - 2: move east
    - 3: move west
    - 4: pickup passenger
    - 5: drop off passenger
"""

# taxi raw, taxi, column, passenger index, destination
env.s = env.encode(0,0,3,4)
env.render()
        
        
        