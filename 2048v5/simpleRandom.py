from Game import *

"""
simpleRandom randomly chooses the next move from a list of valid next moves
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
            validMoves.append(move)
    print validMoves
    if validMoves == []:
        return False
    else:
        return random.choice(validMoves)

start()
