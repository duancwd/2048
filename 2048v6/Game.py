import random
from copy import deepcopy

""" 
This version of game2048 is slightly different from the one that runs
in 2048v5

Added:
- locOfZeroes()
- getValidMoves()
"""


class game2048:
    def __init__(self):
        """ intializes the game with a score of 0 and a board that
        consists of 2 random tiles (of 2 or 4) and the rest zeros"""
        self.totalScore = 0
        self.v = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
        self.addElement()
        self.addElement()

    def display(self):
        """ prints a user-friendly version of the board """
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[0][0], self.v[0][1], self.v[0][2], self.v[0][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[1][0], self.v[1][1], self.v[1][2], self.v[1][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[2][0], self.v[2][1], self.v[2][2], self.v[2][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[3][0], self.v[3][1], self.v[3][2], self.v[3][3]))
        print('score:{0:4}'.format(self.totalScore))

    def addElement(self):
        """ addElement is called after each move to generate a new
        numbered tile on the board, with P(2)=0.9 and P(4)=0.1 """
        numZeroes = self.countZeroes()
        if numZeroes > 0:
            newNum = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
            k = random.randrange(1, numZeroes+1)
            n = 0
            for i in range(4):
                for j in range(4):
                    if self.v[i][j] == 0:
                        n += 1
                        if n == k:
                            self.v[i][j] = newNum
                            return

    def countZeroes(self):
        """ countZeroes returns the number of blank tiles in a given
        board """
        return len(self.locOfZeroes())

    def locOfZeroes(self):
        """ locOfZeroes returns a list with the coordinates of the
        blank tiles """
        locs = []
        for i in range(4):
            for j in range(4):
                if self.v[i][j] == 0:
                    locs.append([i,j])
        return locs

    def operation(self, op):
        """ operation makes a move then adds the next random tile to
        the board *if* the board has changed"""
        newV = self.makeMove(op)
        if self.v != False:
            self.addElement()

    def makeMove(self, op):
        """ makeMove makes a move by sending each row or column to
        handle """
        vcopy = deepcopy(self.v)
        if op == 'left' or op == 'right':
            for row in range(4):
                self.handle(self.v[row], op)
        else:
            for col in range(4):
                vList = [self.v[row][col] for row in range(4)]
                self.handle(vList, op)
                for row in range(4):
                    self.v[row][col] = vList[row]
        if self.v == vcopy:
            return False

    def handle(self, vList, direction):
        """ handle takes a row of the board and a direction, updates
        the row and adjusts the totalScore"""
        self.align(vList, direction)
        increment = self.addSame(vList, direction)
        self.align(vList, direction)
        self.totalScore += increment
        return increment  #why?

    def align(self,vList, direction):
        """ align takes a direction and pushes all the numbers tiles
        toward that direction"""
        for i in range(vList.count(0)):
            vList.remove(0)
        zeros = [0 for x in range(4-len(vList))]
        if direction == 'left' or direction == 'up':
            vList.extend(zeros)
        else:
            vList[:0] = zeros
   
    def addSame(self,vList, direction):
        """ addSame combines two neighboring like numbers into one """
        increment = 0
        if direction == 'left' or direction == 'up':
            for i in [0,1,2]:
                if vList[i]==vList[i+1] and vList[i+1]!=0:
                    vList[i] *= 2
                    vList[i+1] = 0
                    increment += vList[i]
        else:
            for i in [3,2,1]:
                if vList[i]==vList[i-1] and vList[i-1]!=0:
                    vList[i] *= 2
                    vList[i-1] = 0
                    increment += vList[i]
        return increment

    def getValidMoves(self):
        """ getValidMoves returns a list of valid moves from a given
        state """
        moves = ['left', 'right', 'up', 'down']
        validMoves = []
        for move in moves:
            gameCopy = deepcopy(self)
            if gameCopy.makeMove(move) != False:
                validMoves.append(move)
        return validMoves
