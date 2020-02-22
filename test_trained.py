from unityagents import UnityEnvironment
import numpy as np
from ddpg_agent import Agent
import random
import torch
from collections import deque
import matplotlib.pyplot as plt

env = UnityEnvironment(file_name='E:\\Development\\DeepReinf\\8_Proj-ContinuousControl\\Reacher.exe')
brain_name = env.brain_names[0]
brain = env.brains[brain_name]
env_info = env.reset(train_mode=False)[brain_name]
num_agents = len(env_info.agents)
print('Number of agents:', num_agents)
action_size = brain.vector_action_space_size
print('Size of each action:', action_size)
states = env_info.vector_observations
state_size = states.shape[1]
print('There are {} agents. Each observes a state with length: {}'.format(states.shape[0], state_size))
print('The state for the first agent looks like:', states[0])

scores_deque = deque(maxlen=100) #number of consecutive episodes to sustain scores greater than or equal with target (30)
historized_scores=[]
random_seed=1
agent = Agent(state_size=state_size, action_size=action_size, random_seed=1)
agent.actor_local.load_state_dict(torch.load('E:\\Development\\DeepReinf\\8_Proj-ContinuousControl\\checkpoint_actor.pth'))
agent.critic_local.load_state_dict(torch.load('E:\\Development\\DeepReinf\\8_Proj-ContinuousControl\\checkpoint_critic.pth'))

while True:
    state=states[0]               # with respect to working with a single agent only 
    action = agent.act(state, add_noise=False)
    env_info=env.step(action)[brain_name]
    next_state = env_info.vector_observations
    reward=env_info.rewards[0]
    done=env_info.local_done[0]
    print(action)
    states=next_state
    if done:
        break
env.close()