
# coding: utf-8

# In[19]:

import random
import os
import time


# User controlled variables and other hyper-parameters

# In[2]:

GAMMA = 0.9

#All possible actions defined
ACTION_UP = 'up'
ACTION_DOWN = 'down'
ACTION_LEFT = 'left'
ACTION_RIGHT = 'right'

#Number of episodes to consider
NUMBER_OF_EPISODES = 2

#Start and end of any episode
START_STATE = '00'
END_STATE = '15'

#Defining colors for highlighting important aspects
GREEN = lambda x: '\x1b[32m{}\x1b[0m'.format(x)
BLUE = lambda x: '\x1b[34m{}\x1b[0m'.format(x)
RED = lambda x: '\x1b[31m{}\x1b[0m'.format(x)


# The following section defines the MDP

# In[3]:

all_states = ['00', '01', '02', '03',
          '04', '05', '06', '07',
          '08', '09', '10', '11',
          '12', '13', '14', '15']

immediate_state_rewards = {'00': -1,'01': -1,'02': -1,'03': -1,
                           '04': -1,'05': -1,'06': -1,'07': -1,
                           '08': -1,'09': -1,'10': -1,'11': -1,
                           '12': -1,'13': -1,'14': -1,'15': 0 }

all_transitions =  {
'00': {ACTION_UP : '00', ACTION_RIGHT : '01', ACTION_DOWN: '04', ACTION_LEFT: '00'},
'01': {ACTION_UP : '01', ACTION_RIGHT : '02', ACTION_DOWN: '05', ACTION_LEFT: '00'},
'02': {ACTION_UP : '02', ACTION_RIGHT : '03', ACTION_DOWN: '06', ACTION_LEFT: '01'},
'03': {ACTION_UP : '03', ACTION_RIGHT : '03', ACTION_DOWN: '07', ACTION_LEFT: '02'},
'04': {ACTION_UP : '00', ACTION_RIGHT : '05', ACTION_DOWN: '08', ACTION_LEFT: '04'},
'05': {ACTION_UP : '01', ACTION_RIGHT : '06', ACTION_DOWN: '09', ACTION_LEFT: '04'},
'06': {ACTION_UP : '02', ACTION_RIGHT : '07', ACTION_DOWN: '10', ACTION_LEFT: '05'},
'07': {ACTION_UP : '03', ACTION_RIGHT : '07', ACTION_DOWN: '11', ACTION_LEFT: '06'},
'08': {ACTION_UP : '04', ACTION_RIGHT : '09', ACTION_DOWN: '12', ACTION_LEFT: '08'},
'09': {ACTION_UP : '05', ACTION_RIGHT : '10', ACTION_DOWN: '13', ACTION_LEFT: '08'},
'10': {ACTION_UP : '06', ACTION_RIGHT : '11', ACTION_DOWN: '14', ACTION_LEFT: '09'},
'11': {ACTION_UP : '07', ACTION_RIGHT : '11', ACTION_DOWN: '15', ACTION_LEFT: '10'},
'12': {ACTION_UP : '08', ACTION_RIGHT : '13', ACTION_DOWN: '12', ACTION_LEFT: '12'},
'13': {ACTION_UP : '09', ACTION_RIGHT : '14', ACTION_DOWN: '13', ACTION_LEFT: '12'},
'14': {ACTION_UP : '10', ACTION_RIGHT : '15', ACTION_DOWN: '14', ACTION_LEFT: '13'},
'15': {ACTION_UP : '15', ACTION_RIGHT : '15', ACTION_DOWN: '15', ACTION_LEFT: '15'},
}


# General-purpose functions

# In[20]:

def printGridWorld(states_in_episode = [], actions_in_episode = []):
    for state in all_states:
        if (int(state) % 4) == 0:
            print("\n")
        if state in states_in_episode:
            state = state.replace(state, GREEN(state))
        print(state, "\t", end = '')
        
    print('\n', 'All Actions until this time')
    
    for action in actions_in_episode:
        print(action, "\t", end = '')


# Functions for random sampling

# In[5]:

def chooseActionForRandomSampling(random_throw):
    if random_throw < 0.25:
        return ACTION_UP
    elif random_throw < 0.5:
        return ACTION_RIGHT
    elif random_throw < 0.75:
        return ACTION_DOWN
    else:
        return ACTION_LEFT

def generateRandomlySampledEpisode():
    current_state = START_STATE
    states_in_episode = [current_state]
    actions_in_episode = []
    while current_state != END_STATE:
        random_throw = random.uniform(0, 1)
        action = chooseActionForRandomSampling(random_throw)
        actions_in_episode.append(action)
        os.system('clear')
        printGridWorld(states_in_episode, actions_in_episode)
        time.sleep(0.1)
        current_state = all_transitions.get(current_state).get(action)
        states_in_episode.append(current_state)
    return states_in_episode, actions_in_episode


# Functions for importance sampling

# In[6]:

def chooseActionForImportanceSampling(random_throw):
    if random_throw < 0.5:
        return ACTION_RIGHT
    else:
        return ACTION_DOWN

def generateImportanceSampledEpisode():
    current_state = START_STATE
    states_in_episode = [current_state]
    actions_in_episode = []
    while current_state != END_STATE:
        random_throw = random.uniform(0, 1)
        action = chooseActionForImportanceSampling(random_throw)
        actions_in_episode.append(action)
        current_state = all_transitions.get(current_state).get(action)
        states_in_episode.append(current_state)
    return states_in_episode, actions_in_episode


# In[21]:

printGridWorld(all_states)


# In[22]:

for episode_iterator in range(NUMBER_OF_EPISODES):
    states_in_episode, actions_in_episode = generateRandomlySampledEpisode()
    print("EPISODE NUMBER ", episode_iterator)
    print(states_in_episode)
    print(actions_in_episode)
    print('')


# In[8]:

for episode_iterator in range(NUMBER_OF_EPISODES):
    states_in_episode, actions_in_episode = generateImportanceSampledEpisode()
    print("EPISODE NUMBER ", episode_iterator)
    print(states_in_episode)
    print(actions_in_episode)
    print('')


# In[ ]:



