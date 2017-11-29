import numpy as np

reward_overwrite = np.array([0,-10,-40,-100])
reward_outOfBound = np.array([0,-5,-70,-100])
reward_wrongMove = -1000
reward_correct = 2
Total_shapes = 3


s1 = np.array([[1,1],[1,1]])
s2 = np.array([[1,0],[1,0]])
s3 = np.array([[1,0],[1,1]])
SHAPE_DATA = np.array([s1,s2,s3])
a = np.array([ [0,0,1,1,0,0], \
               [0,0,1,1,0,0], \
               [1,1,1,1,1,1], \
               [1,1,1,1,1,1], \
            ])
b = a
c = a
BOARD_DATA = np.array([a,b,c])
# STEP_DATA =

#INSTRUCTIONS
instructions = ["Choose index of the moves to play.", \
                "Above are the indices of each shape is given, pic the index of the shape to play at current postion",\
                "To move current postion select index showing move <dir> "
            ]

#DIRECTIONS
directions = ["Left","Right","Up","Down"]
# a,b,c are the sample board shapes for training purpose
# s1,s2...,sn are the all shpaes to be used in for solving the problem
