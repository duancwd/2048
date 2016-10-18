from Game import *
from copy import deepcopy

"""
onePlyGreedy looks ahead one move and chooses the move that maximizes
the score
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
            validMoves.append((gameCopy.totalScore, move))
    print validMoves
    if validMoves == []:
        return False
    else:
        highScore, bestMove = max(validMoves)
        return bestMove

start()
