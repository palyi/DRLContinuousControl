<h1>Report</h1>

<h1>Learning Algorithm</h1>
<p>
I used the DDPG method for this source. This is an implementation with one single agent acting with just about the minimum required complexity.
Hyperparameters have been selected as follows:<br><br>
BUFFER_SIZE = int(1e6)  <br>
BATCH_SIZE = 192        <br>
GAMMA = 0.99            <br>
TAU = 1e-3              <br>
LR_ACTOR = 1e-4         <br>
LR_CRITIC = 1e-3        <br>
WEIGHT_DECAY = 0        <br>
</p>

<h1>Plot of Rewards</h1>
<p>Training took place with arbitrarily choosen hyperparameters. The environment was solved after 1322 episodes:</p>
<br>
![TrainScores]('https://github.com/palyi/DRLContinuousControl/blob/master/plot_of_scores.JPG')
<p>The training showed the following characteristics. After some fine tuning, the training could take place in about 1/3 of the time currently needed (training was realized locally, on a 1080Ti GPU).</p>
<br>
![TrainPlot]('https://github.com/palyi/DRLContinuousControl/blob/master/score_per_episode.JPG')

<h1>Ideas for Future Work</h1>
I see two major ideas around this topic. One is to apply a suitable hyperparameter optimizer in order to make the learning process optimal.
A more spectacular direction, on top of the aforementioned, would be to actually construct some physical setup that realizes the moves in a real world scenario.
