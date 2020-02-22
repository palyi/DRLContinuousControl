<h1>Report</h1>

<h1>Learning Algorithm</h1>
<p>
I used the DDPG method for this source. This is an implementation with one single agent acting with just about the minimum required complexity.
Hyperparameters have been selected as follows:<br>
BUFFER_SIZE = int(1e6)  
BATCH_SIZE = 192        
GAMMA = 0.99            
TAU = 1e-3              
LR_ACTOR = 1e-4         
LR_CRITIC = 1e-3        
WEIGHT_DECAY = 0        
</p>

<h1>Plot of Rewards</h1>
<p>Training took place with arbitrarily choosen hyperparameters. The environment was solved after 1322 episodes:</p>
<br>
![TrainScores](score_per_episode.JPG)
<p>The training showed the following characteristics. After some fine tuning, the training could take place in about 1/3 of the time currently needed (training was realized locally, on a 1080Ti GPU).</p>
<br>
![TrainPlot](plot_of_scores.JPG)

<h1>Ideas for Future Work</h1>
I see two major ideas around this topic. One is to apply a suitable hyperparameter optimizer in order to make the learning process optimal.
A more spectacular direction, on top of the aforementioned, would be to actually construct some physical setup that realizes the moves in a real world scenario.