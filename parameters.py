import numpy as np

reward_overwrite = np.array([0,-10,-40,-100])
reward_outOfBound = np.array([0,-5,-70,-100])
reward_wrongMove = -1000
reward_correct = 2
Total_shapes = 10

SHAPE_DATA = np.array([s1,s2,s3])
BOARD_DATA = np.array([a,b,c])
# STEP_DATA =

# a,b,c are the sample board shapes for training purpose
# s1,s2...,sn are the all shpaes to be used in for solving the problem
