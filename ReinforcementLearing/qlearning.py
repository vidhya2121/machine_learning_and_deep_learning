# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:54:17 2021

@author: vidhya
"""


import gym
import random

random.seed(1234)

streets = gym.make('Taxi-v3').env
streets.render()

initial_state = streets.encode(2, 3, 2, 0)
print('Initial State ::: ', initial_state)
streets.s = initial_state
streets.render()

print(streets.P[initial_state])

import numpy as np

q_table = np.zeros([streets.observation_space.n, streets.action_space.n])

learning_rate = 0.1
discount_factor = 0.6
exploration = 0.1
epochs = 10000

for taxi_run in range(epochs):
    state = streets.reset()
    done = False
    while not done:
        random_value = random.uniform(0, 1)
        if (random_value < exploration):
            action = streets.action_space.sample()
        else:
            action = np.argmax(q_table[state])
        
        next_state, reward, done, info = streets.step(action)
        
        prev_q = q_table[state, action]
        next_max_q = np.max(q_table[next_state])  
        new_q = (1 - learning_rate) * prev_q + learning_rate * (reward + discount_factor * next_max_q)
        q_table[state,action] = new_q
        state = next_state
        
print('Q Table ::: ', q_table[initial_state])
        
from IPython.display import clear_output
from time import sleep
for trip_num in range(1, 11):
    state = streets.reset()
    done = False
    trip_len = 0
    while not done and trip_len < 25:
        action = np.argmax(q_table[state])
        next_state, reward, done, info = streets.step(action)
        clear_output(wait=True)
        print("Trip number ", trip_num, " Step ", trip_len)
        print(streets.render(mode='ansi'))
        sleep(.5)
        state = next_state
        trip_len += 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        