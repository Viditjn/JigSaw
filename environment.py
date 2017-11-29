import random
import pdb
import numpy as np
from parameters import *

class ENVIRONMENT():

    def __init__(self):
        board_index = random.randint(0,len(BOARD_DATA)-1)
        col = len(BOARD_DATA[board_index][0])
        row = len(BOARD_DATA[board_index])
        self.SHAPE_MAT = [SHAPE(SHAPE_DATA[i]) for i in range(Total_shapes)]
        self.TARGET_BOARD = BOARD(row,col)
        self.TARGET_BOARD.board = BOARD_DATA[board_index]
        self.CURR_BOARD = BOARD(row,col)
        self.curr_x = 0
        self.curr_y = 0

    def reset(self):
        del self.TARGET_BOARD
        del self.CURR_BOARD
        col = len(BOARD_DATA[board_index][0])
        board_index = random.randint(0,len(BOARD_DATA)-1)
        row = len(BOARD_DATA[board_index])
        self.TARGET_BOARD = BOARD(row,col)
        self.TARGET_BOARD.board = BOARD_DATA[board_index]
        self.CURR_BOARD = BOARD(row,col)
        self.curr_x = 0
        self.curr_y = 0

    def print_board(self):
        for i in range(self.TARGET_BOARD.row):
            for j in range(self.TARGET_BOARD.col):
                print self.TARGET_BOARD.board[i][j],
            print '\t',
            for j in range(self.CURR_BOARD.col):
                print self.CURR_BOARD.board[i][j],
            print

    def step_reward(self,step_index):
        tempX = self.curr_x
        tempY = self.curr_y
        reward = 0
        flag = 0
        if step_index<=Total_shapes and step_index>=0:
            tempX -= self.SHAPE_MAT[step_index-1].startX
            for i in range(self.SHAPE_MAT[step_index-1].height):
                if flag == 0:
                    for j in range(self.SHAPE_MAT[step_index-1].width):
                        if flag == 0 and self.SHAPE_MAT[step_index-1].data[i][j] == 1:
                            if self.CURR_BOARD.board[tempX+i][tempY+j] == 1 and self.TARGET_BOARD.board[tempX+i][tempY+j] == 1: #Positive score
                                reward += positive_score
                            if self.CURR_BOARD.board[tempX+i][tempY+j] == 1 and self.TARGET_BOARD.board[tempX+i][tempY+j] == 0: #negative misfit score
                                reward += misfit_score
                            if self.CURR_BOARD.board[tempX+i][tempY+j] > 1 : #overfit high negative reward and break
                                reward = overfit_score
                                flag = 1
        else:
            # pdb.set_trace()
            if self.curr_x < 0 or self.curr_x >= self.CURR_BOARD.col \
                or self.curr_y < 0 or self.curr_y >= self.CURR_BOARD.row: # for moving out of the bound
                    reward = wrong_move
            else :
                reward = 0 #correct move
        return reward

    def getScore(self):
        score = 0
        # pdb.set_trace()
        for i in range(self.CURR_BOARD.row):
            for j in range(self.CURR_BOARD.col):
                if self.TARGET_BOARD.board[i][j]==0:
                    score += self.CURR_BOARD.board[i][j]*reward_outOfBound[min(3,self.CURR_BOARD.board[i][j])]
                elif self.TARGET_BOARD.board[i][j]==1 and self.CURR_BOARD.board[i][j]==1:
                    score += reward_correct
                elif self.TARGET_BOARD.board[i][j]==1:
                    # pdb.set_trace()
                    # No +ve or -ve reward for the place where no block is inserted as makes no sense to add for those who are not even considered
                    score += max(0,self.CURR_BOARD.board[i][j]-self.TARGET_BOARD.board[i][j])*reward_overwrite[min(3,abs(self.CURR_BOARD.board[i][j]-self.TARGET_BOARD.board[i][j]))]

        return score

    def step(self,step_index):
        if step_index > Total_shapes + 5:
            return -1,-1,-1
        # for index 0:total_shapes for chosing a shape at pos curr_x,curr_y
        # pdb.set_trace()
        is_done = False
        if step_index<=Total_shapes and step_index>=0:
            flag,self.CURR_BOARD.board = self.CURR_BOARD.updateBoard(self.SHAPE_MAT[step_index-1],self.curr_x,self.curr_y)
            # pdb.set_trace()
            step_score = self.step_reward(step_index)
            temp_score = self.getScore()
            # self.CURR_BOARD = self.CURR_BOARD.getScreen()
            if flag:
                return temp_score,is_done,step_score
            else :
                return temp_score + reward_wrongMove,is_done,step_score # In case when the chosen shape can't fit in the desired postion
        # for moving the curr_positon
        else:
            temp_score = self.getScore()
            if step_index == Total_shapes + 1: #for left
                self.curr_y -= 1
            elif step_index == Total_shapes + 2: #for left
                self.curr_y += 1
            elif step_index == Total_shapes + 3: #for up
                self.curr_x -= 1
            elif step_index == Total_shapes + 4: #for down
                self.curr_x += 1
            elif step_index == Total_shapes + 5: #Do nothing
                pass
            elif step_index == Total_shapes + 6: #EXIT
                is_done = True
            ##

            step_score = self.step_reward(step_index)
            # print step_score
            if self.curr_x < 0 or self.curr_x >= self.CURR_BOARD.col \
                or self.curr_y < 0 or self.curr_y >= self.CURR_BOARD.row: # for moving out of the bound
                return temp_score + reward_wrongMove,is_done,step_score
            else:
                return temp_score,is_done,step_score

    def target():
        return self.TARGET_BOARD

    def state():
        return self.CURR_BOARD, curr_x, curr_y

    def shpaes():
        return self.SHAPE_MAT

    def get_pos(self):
        return self.curr_x,self.curr_y


class SHAPE():

    def __init__(self,shape):
        self.data = shape
        self.startX = np.argmax(shape[0]==1)
        self.width = len(shape[0])
        self.height = len(shape)

    def rotate(self,No_of_rot):
        return np.rot90(shape,k=No_of_rot,axes=(0,1))

    def printShape(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                print(self.data[i][j]),
            print

class BOARD():

    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.board = np.array([[0 for i in range(col)] for j in range(row)])

    # def get_pos(self):
    #     return self.row,self.col

    def reset(self):
        board_index = random.randint(0,len(BOARD_DATA))
        self.board = BOARD_DATA[board_index]
        self.row = len(self.board)
        self.col = len(self.board_index[0])

    def check(self,shape,posX,posY):
        if posX >= self.col or posX < 0 or posY >= self.row or posY < 0 :
            return False
        if (posX + shape.width - shape.startX > self.col) or (posY + shape.height > self.row):
            return False
        return True

    def updateBoard(self,shape,posX,posY):
        if self.check(shape,posX,posY):
            posX = posX - shape.startX
            # pdb.set_trace()
            self.board[posX:posX+shape.width,posY:posY+shape.height] += shape.data
            self.board[self.board > 1] = 2 # Because the overfit has same score if it has one overfit or more
            posX = posX + shape.startX
            return True,self.board
        else :
            return False,self.board

    def getScreen(self):
        return self.board

    def printScreen(self):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j]),
            print

    def __del__(self):
      pass


def initializeShapes():
    shape1 = [[1,1],[1,1]]
    shape2 = [[1,0],[1,0]]
    shape3 = [[1,0],[1,1]]
    ShapeData = []
    ShapeData.append(SHAPE(shape1))
    ShapeData.append(SHAPE(shape2))
    ShapeData.append(SHAPE(shape3))
    return ShapeData

def play():
    env = ENVIRONMENT()
    startMessage(env.SHAPE_MAT)
    print "Instructions : "
    i = 0
    for instruction in instructions:
        print '\t' +str(i) + " : ",
        print instruction
        i+=1
    flagPlay = True
    while flagPlay:
        move_index = raw_input(" Select a shape and position to play : ")
        temp_score,is_done,step_score = env.step(int(move_index))
        print env.get_pos()
        print temp_score,is_done,step_score
        env.print_board()

def startMessage(Shapes):
    i = 1
    for shape in Shapes:
        print "Move Index " + str(i) + " : "
        shape.printShape()
        i+=1
    for direction in directions:
        print "Move Index " + str(i) + " : ",
        print direction
        i+=1

if __name__ == "__main__":
    play()
    # Shapes = initializeShapes()
