from Game import *
from copy import deepcopy

"""
decreasingOrders looks ahead one move and chooses the move that try to
make the tiles in decreasing order
"""

def start():
    game = game2048()
    game.display()
    op = nextMove(game)
    while op:
        print 'move: ' + op
        game.operation(op)
        game.display()
        print ''
        op = nextMove(game)

def nextMove(game):
    moves = ['left', 'right', 'up', 'down']
    validMoves = []
    for move in moves:
        gameCopy = deepcopy(game)
        if gameCopy.operation(move) != False:
            moveScore = moveCal(game, move)
            validMoves.append((moveScore, move))
    print validMoves
    if validMoves == []:
        return False
    else:
        highScore, bestMove = max(validMoves)
        return bestMove
        
def moveCal(game, move):
    score = 0
    gameCopy = deepcopy(game)
    score -= game.totalScore
    gameCopy.operation(move)
    score += gameCopy.totalScore
    if decreasing(gameCopy.v):
        score += 100
    if cornerMax(gameCopy.v) == False:
        score -= 200
    return score

def decreasing(v):
    for i in range(1):
        for j in range(3):
            digit1 = v[i][j]
            digit2 = v[i][j+1]
            if digit1 <= digit2 and digit1 != 0:
                return False
            '''    
            digit2 = v[i+1][j]
            if digit1 < digit2 and digit1 != 0:
                return False
            '''
    return True

def cornerMax(v):
    digit1 = v[0][0]
    for i in range(3):
        for j in range(3):
            digit2 = v[i][j+1]
            if digit1 < digit2:
                return False
            digit2 = v[i+1][j]
            if digit1 < digit2:
                return False
    return True


start()
