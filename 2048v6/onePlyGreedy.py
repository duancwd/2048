from Game import *
from copy import deepcopy

"""
onePlyGreedy looks ahead one move and chooses the move that maximizes
the score.  ties are broken favoring up, right, left, down (b/c
alphabetical order)
"""

def start():
    game = game2048()
    game.display()
    while game.getValidMoves() != []:
        move = nextMove(game)
        print 'move: ' + move
        game.operation(move)
        game.display()
        print ''

def nextMove(game):
    moves = game.getValidMoves()
    scores = []
    for move in moves:
        gameCopy = deepcopy(game)
        gameCopy.operation(move)
        scores.append((gameCopy.totalScore, move))
    highScore, bestMove = max(scores)
    return bestMove

start()
