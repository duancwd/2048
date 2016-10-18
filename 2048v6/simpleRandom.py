from Game import *

"""
simpleRandom randomly chooses the next move from a list of valid next moves
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
    validMoves = game.getValidMoves()
    move = random.choice(validMoves)
    return move

start()
