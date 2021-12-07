# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:14:07 2021

@author: Murat Kerem Kara
"""
# %% Starting Part
import gym
env = gym.make("Taxi-v3").env
env.render() # show 
"""
blue = passenger
purple = destination
yellow/red = empty taxi
green = full taxi
RGBY = location for destination and passenger
"""
env.reset() # reset env and random initial state
# %% 
print("State Space: ", env.observation_space) # 500
print("Action Space: ", env.action_space) # 6
# Taxi row, taxi coloumn, passenger index, destination
state = env.encode(3,1,2,3)
print("State Number: ", state)
env.s = state
env.render()
# %%
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
# probability, next_state, reward, done
env.P[331]
# %%

#1
total_reward_list=[]
for j in range(5):
    env.reset()
    time_step=0
    total_reward=0
    list_visualize=[]
    while True:
        time_step+=1
        
        # Choose action
        action=env.action_space.sample()
        
        # Perform Action and get reward
        state, reward, done, _ = env.step(action) # state = next_state
        
        # Total Reward
        total_reward += reward
        
        # Visualize
        list_visualize.append({"frame": env, 
                               "state": state, "action": action, "reward": reward,
                               "Total Reward": total_reward})
        # env.render()
        
        
        if done:
            total_reward_list.append(total_reward)
            break
# %%
#import time
for i, frame in enumerate(list_visualize):
   # print(frame["frame"].getvalue())
    print("Timestep: ", i+1)
    print("State: ", frame["state"])
    print("Action: ", frame["action"])
    print("Reward: ", frame["reward"])
    print("Total Reward: ", frame["Total Reward"])
    #time.sleep(3)
    
    