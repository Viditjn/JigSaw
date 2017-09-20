import numpy as np

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

    def getScreen(self):
        return self.board

    def printScreen(self):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j]),
            print

def getScore(current, target):
    return np.sum(np.absolute(np.subtract(current,target)))

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
