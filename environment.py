import numpy as np
import random
import * from parameters

class envrinoment():

    def __init__(self):
        board_index = random.randint(0,len(BOARD_DATA))
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
        board_index = random.randint(0,len(BOARD_DATA))
        col = len(BOARD_DATA[board_index][0])
        row = len(BOARD_DATA[board_index])
        self.TARGET_BOARD = BOARD(row,col)
        self.TARGET_BOARD.board = BOARD_DATA[board_index]
        self.CURR_BOARD = BOARD(row,col)
        self.curr_x = 0
        self.curr_y = 0


    def getScore(self):
        score = 0
        for i in range(len(self.CURR_BOARD)):
            for j in range(len(self.CURR_BOARD[0])):
                if self.TARGET_BOARD[i][j]==0:
                    score += self.CURR_BOARD[i][j]*reward_outOfBound[min(3,self.CURR_BOARD[i][j])]
                elif self.TARGET_BOARD[i][j]==1 and self.CURR_BOARD[i][j]==1:
                    score += reward_correct
                elif self.TARGET_BOARD[i][j]==1:
                    # No +ve or -ve reward for the place where no block is inserted as makes no sense to add for those who are not even considered
                    score += max(0,self.CURR_BOARD[i][j]-self.TARGET_BOARD[i][j])*reward_overwrite[min(3,abs(self.CURR_BOARD[i][j]-self.TARGET_BOARD[i][j]))]

        return score

    def step(self,step_index):
        if step_index<=Total_shapes and step_index>0:
            flag = self.CURR_BOARD.updateBoard(self.SHAPE_MAT[step_index-1],self.curr_x,self.curr_y)
            temp_score = getScore()
            if flag:
                return temp_score
            else :
                return temp_score + reward_wrongMove # In case when the chosen shape can't fit in the desired postion
        else:
            temp_score = getScore()
            if step_index == Total_shapes + 1: #for right
                self.curr_x += 1
            elif step_index == Total_shapes + 2: #for left
                self.curr_x -= 1
            elif step_index == Total_shapes + 1: #for up
                self.curr_y += 1
            elif step_index == Total_shapes + 1: #for down
                self.curr_y -= 1
            if self.curr_x < 0 or self.curr_x >= len(self.CURR_BOARD.col) or self.curr_y < 0 or self.curr_y >= len(self.CURR_BOARD.row):
                return temp_score + reward_wrongMove
            else:
                return temp_score

    def target():
        return self.TARGET_BOARD

    def state():
        return self.CURR_BOARD, curr_x, curr_y


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

    def reset(self):
        board_index = random.randint(0,len(BOARD_DATA))
        self.board = BOARD_DATA[board_index]
        self.row = len(self.board)
        self.col = len(self.board_index[0])

    def check(self,shape,posX,posY):
        if posX >= self.col or posX < 0 or posY >= self.row or posY < 0 :
            return False
        if posX < shape.startX or (posX + shape.width - shape.startX > self.col) or (posY + shape.height > self.row):
            return False
        return True

    def updateBoard(self,shape,posX,posY):
        if check(shape,posX,posY):
            posX = posX - shape.startX
            self.board[posX:posX+shape.col,posY:posY+shape.row] += shape
            return True
        else :
            return False

    def getScreen(self):
        return self.board

    def printScreen(self):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j]),
            print

    def __del__(self):
      pass

def getScore(current, target):
    score = 0
    for i in range(len(current)):
        for j in range(len(current[0])):
            if target[i][j]==0:
                score += current[i][j]*reward_outOfBound[min(3,current[i][j])]
            elif target[i][j]==1 and current[i][j]==1:
                score += reward_correct
            elif target[i][j]==1:
                # No +ve or -ve reward for the place where no block is inserted as makes no sense to add for those who are not even considered
                score += max(0,current[i][j]-target[i][j])*reward_overwrite[min(3,abs(current[i][j]-target[i][j]))]

    return score

def initializeShapes():
    shape1 = [[1,1],[1,1]]
    shape2 = [[1,0],[1,0]]
    shape3 = [[1,0],[1,1]]
    ShapeData = []
    ShapeData.append(SHAPE(shape1))
    ShapeData.append(SHAPE(shape2))
    ShapeData.append(SHAPE(shape3))
    return ShapeData

if __name__ == "__main__":
    Shapes = initializeShapes()
    for shape in Shapes:
        shape.printShape()
