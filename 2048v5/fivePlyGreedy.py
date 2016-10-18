from Game import *
from copy import deepcopy

"""
it looks ahead two move and chooses the move that maximizes
the score
"""

def start():
    game = game2048()
    game.display()
    op = nextMove(game)
    while op:
        print 'move: ' + str(op)
        game.operation(op)
        game.display()
        print ''
        op = nextMove(game)

def nextMove(game):
    oplistO =['left','right','up','down']
    
    moves =[]
    for x in range(4):
            for y in range(4):
                for z in range(4):
                        for n in range(4):
                            for m in range(4):
                                    moves.append([oplistO[x],oplistO[y],oplistO[z],oplistO[n],oplistO[m]])
        

    '''
    moves  = [['left', 'left'], ['left', 'right'], 
                  ['left', 'up'], ['left', 'down'],
                  ['right', 'left'], ['right', 'right'], 
                  ['right', 'up'], ['right', 'down'],
                  ['up', 'left'], ['up', 'right'], 
                  ['up', 'up'], ['up', 'down'],
                  ['down', 'left'], ['down', 'right'], 
                  ['down', 'up'], ['down', 'down']]
    '''
    validMoves = []
    for movelist in moves:
        Score=0
        gameCopy = deepcopy(game)
        for move in movelist:
            if gameCopy.operation(move) != False:
                Score +=gameCopy.totalScore
                validMoves.append((Score, movelist[0]))
                
    print validMoves
    if validMoves == []:
        return False
    else:
        highScore, bestMove = max(validMoves)
        if highScore !=0:
            return bestMove
        else:
            bestMove = random.choice(validMoves)
         
        
            
    return bestMove

start()
