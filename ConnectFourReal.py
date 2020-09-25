# Tiffany McBrayer
# Connect Four Mini-Project

from graphics import *
import random, math, time

# This class creates a single square that makes up the whole board for connect four
class CreateSquare:

    def __init__(self, win, bottomX, bottomY):
        topX = bottomX + 50
        topY = bottomY + 50
        base = Rectangle(Point(bottomX, bottomY), Point(topX, topY))
        base.setFill("blue")
        base.draw(win)
        centerPoint = Point((bottomX + 25), (bottomY + 25))
        circle = Circle(centerPoint, 20)
        circle.setFill("white")
        circle.draw(win)

# Creates buttons that I am able to press under each column in graph window to add a tile
class SquareButton:

    def __init__(self, win, centerX, centerY, size, color, label):
        leftX = centerX - size/2
        rightX = centerX + size/2
        topY = centerY - size/2
        bottomY = centerY +size/2
        rect = Rectangle(Point(leftX, bottomY), Point(rightX, topY))
        rect.setFill(color)
        rect.draw(win)
        centerPoint = Point(centerX, centerY)
        text = Text(centerPoint, label)
        text.setSize(9)
        text.draw(win)
        self.x1 =  leftX
        self.x2 = rightX
        self.y1 = topY
        self.y2 = bottomY
        self.graphicsObject = rect
        self.color = color

    def contains(self,point):
        pointX = point.getX()
        pointY = point.getY()
        if (pointX >= self.x1 and pointX <= self.x2 and
            pointY >= self.y1 and pointY <= self.y2):
            return True
        else:
            return False

# This class creates the single tile when a player presses on the button under the row

class CreateTile:

    def __init__(self, win, centerX, centerY, color):
        centerPoint = Point(centerX, centerY)
        circle = Circle(centerPoint, 20)
        circle.setFill(color)
        circle.draw(win)

# This class takes an existing matrix and tells you at which position a symbol is seen 4 times in a row
class Connect:
    
    def __init__(self, matrix, color, row, col):
        self.matrix = matrix
        self.color = color
        self.row = row
        self.col = col
    
    # returns True if four board entries in a row in row self.row equals the letter
    def inBounds(self, row, col):
        numRows = len(self.matrix)
        numColumns = len(self.matrix[0])
        if row >= numRows:
            return False
        elif row < 0:
            return False
        elif col >= numColumns:
            return False
        elif col < 0:
            return False
        else:
            return True
        
    
    def rowWin(self):
        for _ in range(4):
            if self.inBounds(self.row, self.col) != True:
                return False
            else:
                if self.matrix[self.row][self.col] != self.color:
                   return False
                self.col = self.col + 1
        return True
    
    def columnWin(self):
        for _ in range(4):
            if self.inBounds(self.row, self.col) != True:
                return False
            else:
                if self.matrix[self.row][self.col] != self.color:
                   return False
            self.row = self.row + 1
        return True
                

    def upRightDiagonalWin(self):
        for _ in range(4):
            if self.inBounds(self.row, self.col) != True:
                return False
            else:
                if self.matrix[self.row][self.col] != self.color:
                    return False
                self.row = self.row - 1
                self.col = self.col + 1
        return True 

    def upLeftDiagonalWin(self):
        for _ in range(4):
            if self.inBounds(self.row, self.col) != True:
                return False
            else:
                if self.matrix[self.row][self.col] != self.color:
                    return False
                self.row = self.row - 1
                self.col = self.col - 1
        return True
    
def main():
    win = GraphWin("Connect 4", 450, 500)
    message = Text(Point(200,50), "Lets play Connect 4")
    message.setSize(24)
    message.draw(win)
    # creating the buttons to press under each column
    b1 = SquareButton(win, 75, 475, 50, "gray", "Place here")
    b2 = SquareButton(win, 125, 475, 50, "gray", "Place here")
    b3 = SquareButton(win, 175, 475, 50, "gray", "Place here")
    b4 = SquareButton(win, 225, 475, 50, "gray", "Place here")
    b5 = SquareButton(win, 275, 475, 50, "gray", "Place here")
    b6 = SquareButton(win, 325, 475, 50, "gray", "Place here")
    b7 = SquareButton(win, 375, 475, 50, "gray", "Place here")
    bquit = SquareButton(win, 425, 25, 50, "red", "Quit")
    
    # create board
    pointX = 50
    pointY = 150
    for _ in range(6):
        for _ in range(7):
            CreateSquare(win, pointX, pointY)
            pointX = pointX + 50
        pointX = 50
        pointY = pointY + 50
        
    # add tile to board
    # color1 and color2 are the two colors made into numbers so they can be put into the matrix as numbers
    # Y variable is the start of where each tile is first located according to the Y-axis
    # the total variable to added by one by every loop
    # if the loop is on an odd number then it places a red tile, even number yellow tile
    # the m varibale keeps track of where the color symbol is placed in the matrix 
    color1 = 1
    color2 = 2
    y1,y2,y3,y4,y5,y6,y7 = 425,425,425,425,425,425,425
    total = 0
    m1,m2,m3,m4,m5,m6,m7 = 5,5,5,5,5,5,5

    # play
    # if a button is pressed this code keeps track of where the tile goes in the graph window
    # also keeps track of where the symbol goes into the matrix 
    while True:
        p = win.getMouse()
        total = total + 1
        if bquit.contains(p):
            win.close()
            return False
        # putting a tile in each column 
        if b1.contains(p):
            if y1 > 150:
                x1 = 75
                if total % 2 != 0:
                    color = color1
                    matrix[m1][0] = color1
                    CreateTile(win, x1, y1, "red")
                else:
                    color = color2
                    matrix[m1][0] = color2
                    CreateTile(win, x1, y1, "yellow")
                y1 = y1 - 50
                m1 = m1 - 1
        if b2.contains(p):
            if y2 > 150:
                x2 = 125
                if total % 2 != 0:
                    color = color1
                    matrix[m2][1] = color1
                    CreateTile(win, x2, y2, "red")
                else:
                    color = color2
                    matrix[m2][1] = color2
                    CreateTile(win, x2, y2, "yellow")
                y2 = y2 - 50
                m2 = m2 - 1
        if b3.contains(p):
            if y3 > 150:
                x3 = 175
                if total % 2 != 0:
                    color = color1
                    matrix[m3][2] = color1
                    CreateTile(win, x3, y3, "red")
                else:
                    color = color2
                    matrix[m3][2] = color2
                    CreateTile(win, x3, y3, "yellow")
                y3 = y3 - 50
                m3 = m3 - 1
        if b4.contains(p):
            if y4 > 150:
                x4 = 225
                if total % 2 != 0:
                    color = color1
                    matrix[m4][3] = color1
                    CreateTile(win, x4, y4, "red")
                else:
                    color = color2
                    matrix[m4][3] = color2
                    CreateTile(win, x4, y4, "yellow")
                y4 = y4 - 50
                m4 = m4 - 1
        if b5.contains(p):
            if y5 > 150:
                x5 = 275
                if total % 2 != 0:
                    color = color1
                    matrix[m5][4] = color1
                    CreateTile(win, x5, y5, "red")
                else:
                    color = color2
                    matrix[m5][4] = color2
                    CreateTile(win, x5, y5, "yellow")
                y5 = y5 - 50
                m5 = m5 - 1
        if b6.contains(p):
            if y6 > 150:
                x6 = 325
                if total % 2 != 0:
                    color = color1
                    matrix[m6][5] = color1
                    CreateTile(win, x6, y6, "red")
                else:
                    color = color2
                    matrix[m6][5] = color2
                    CreateTile(win, x6, y6, "yellow")
                y6 = y6 - 50
                m6 = m6 - 1
        if b7.contains(p):
            if y7 > 150:
                x7 = 375
                if total % 2 != 0:
                    color = color1
                    matrix[m7][6] = color1
                    CreateTile(win, x7, y7, "red")
                else:
                    color = color2
                    matrix[m7][6] = color2
                    CreateTile(win, x7, y7, "yellow")
                y7 = y7 - 50
                m7 = m7 - 1
                
        # checking if there is connect 4 every time the martrix is updated
        numRows = len(matrix) 
        numCol = len(matrix[0])
        for r in range(numRows):
            for c in range(numCol):
                color1Check1 = Connect(matrix, 1, r, c)
                color1Check2 = Connect(matrix, 1, r, c)
                color1Check3 = Connect(matrix, 1, r, c)
                color1Check4 = Connect(matrix, 1, r, c)
                color2Check1 = Connect(matrix, 2, r, c)
                color2Check2 = Connect(matrix, 2, r, c)
                color2Check3 = Connect(matrix, 2, r, c)
                color2Check4 = Connect(matrix, 2, r, c)
                # check the red symbol in the matrix 
                if color1Check1.rowWin() == True:
                    m = Text(Point(200,100), ("Red wins!"))
                    m.setSize(24)
                    m.setFill("red")
                    m.draw(win)
                    return None
                if color1Check2.columnWin() == True:
                    m = Text(Point(200,100), ("Red wins!"))
                    m.setSize(24)
                    m.setFill("red")
                    m.draw(win)
                    return None
                if color1Check3.upRightDiagonalWin() == True:
                    m = Text(Point(200,100), ("Red wins!"))
                    m.setSize(24)
                    m.setFill("red")
                    m.draw(win)
                    return None
                if color1Check4.upLeftDiagonalWin() == True:
                    m = Text(Point(200,100), ("Red wins!"))
                    m.setSize(24)
                    m.setFill("red")
                    m.draw(win)
                    return None
                # check the yellow symbol in the matrix 
                if color2Check1.rowWin() == True:
                    m = Text(Point(200,100), ("Yellow wins!"))
                    m.setSize(24)
                    m.setFill("Yellow")
                    m.draw(win)
                    return None
                if color2Check2.columnWin() == True:
                    m = Text(Point(200,100), ("Yellow wins!"))
                    m.setSize(24)
                    m.setFill("Yellow")
                    m.draw(win)
                    return None 
                if color2Check3.upRightDiagonalWin() == True:
                    m = Text(Point(200,100), ("Yellow wins!"))
                    m.setSize(24)
                    m.setFill("Yellow")
                    m.draw(win)
                    return None
                if color2Check4.upLeftDiagonalWin() == True:
                    m = Text(Point(200,100), ("Yellow wins!"))
                    m.setSize(24)
                    m.setFill("Yellow")
                    m.draw(win)
                    return None
                else:
                    pass
    
    
                
matrix = [["", "", "", "", "", "", ""],
          ["", "", "", "", "", "", ""],
          ["", "", "", "", "", "", ""],
          ["", "", "", "", "", "", ""],
          ["", "", "", "", "", "", ""],
          ["", "", "", "", "", "", ""]]

            
    






    
