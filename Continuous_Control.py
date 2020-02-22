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
env_info = env.reset(train_mode=True)[brain_name]
num_agents = len(env_info.agents)
print('Number of agents:', num_agents)
action_size = brain.vector_action_space_size
print('Size of each action:', action_size)
states = env_info.vector_observations
state_size = states.shape[1]
print('There are {} agents. Each observes a state with length: {}'.format(states.shape[0], state_size))
print('The state for the first agent looks like:', states[0])

def ddpg(n_episodes=2500, max_t=1000):
    scores_deque = deque(maxlen=100) #number of consecutive episodes to sustain scores greater than or equal with target (30)
    historized_scores=[]
    for i_episode in range(1, n_episodes+1):
        env_info = env.reset(train_mode=True)[brain_name]
        states = env_info.vector_observations
        agent.reset()
        episode_score = np.zeros(num_agents)
        for t in range(max_t):
            state=states[0]               # with respect to working with a single agent only 
            action = agent.act(state)
            env_info=env.step(action)[brain_name]
            next_state = env_info.vector_observations
            reward=env_info.rewards[0]
            done=env_info.local_done[0]
            agent.step(state, action, reward, next_state, done,t)
            states=next_state
            episode_score += reward
            if done:
                break
        scores_deque.append(episode_score)
        historized_scores.append(episode_score)
        print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(episode_score)))
        if np.mean(scores_deque)>=30:
            break 
    torch.save(agent.actor_local.state_dict(), 'checkpoint_actor.pth')
    torch.save(agent.critic_local.state_dict(), 'checkpoint_critic.pth')                
    return historized_scores

agent = Agent(state_size=state_size, action_size=action_size, random_seed=1)
scores = ddpg()

# plot results:
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(np.arange(1, len(scores)+1), scores)
plt.ylabel('Score')
plt.xlabel('Episode #')
plt.show()
env.close()