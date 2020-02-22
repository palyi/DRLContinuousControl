
<h2>Project Details</h2>

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/MjjcNHc4Naw/0.jpg)](http://www.youtube.com/watch?v=MjjcNHc4Naw)

<h3>Environment</h3>
<p>
In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.
</p>

<h3>State Space</h3>
<p>
The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. 
</p>

<h3>Action Space</h3>
<p>
Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.
</p>

<h3>Task</h3>
The task is episodic, and in order to solve the environment, your agent must get an average score of +30 over 100 consecutive episodes.

<h3>Solution Criteria</h3>
<p>
The environment is considered solved, when the average (over 100 episodes) of those average scores is at least +30.
</p>

<h2>Getting Started</h2>
<p>
In order to run the agent, you need to add the files of the Unity environment in its folder. The python source will reference the .exe file to start generating the virtual world with the robotic arm and the target ball.
</p>
<h2>Instructions to Run and Train the Agent</h2>
<p>
There are two modes you can run the code in this repository:
- To train the agent, you need to run Continuous-Control.py. As a result of the training, you will have checkpoint_actor.pth and checkpoint_critic.pth files updated.
- In order to watch the trained agent working, you should run test_trained.py.
- To check out the metrics of the training and the results, see the file report.md in this repository.
</p>
