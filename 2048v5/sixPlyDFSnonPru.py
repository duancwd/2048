from Game import *
from copy import deepcopy

"""
it looks ahead six moves and chooses the move that maximizes
the score using dfs without pruning
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
    oplist0 =['left','right','up','down']
    validMoves = []
    for x in range (4):
    	gameCopy = deepcopy(game)
    	move = oplist0[x]
        if gameCopy.operation(move) != False:
            validMoves.append((0, move))
    
    moves =[]
    for move in validMoves:
    	gameCopy1 = deepcopy(game)
    	gameCopy1.operation(move[1])
        for y in range(4):
            gameCopy2 = deepcopy(gameCopy1)
            gameCopy2.operation(oplist0[y])
            for z in range(4):
				    gameCopy3 = deepcopy(gameCopy2)
				    gameCopy3.operation(oplist0[z])
				    for n in range(4):
				            gameCopy4 = deepcopy(gameCopy3)
				            gameCopy4.operation(oplist0[n])
				            for m in range(4):
				                    gameCopy5 = deepcopy(gameCopy4)
				                    gameCopy5.operation(oplist0[m])
				                    for k in range(4):
				                            gameCopy6 = deepcopy(gameCopy5)
				                            gameCopy6.operation(oplist0[k])
				                            moves.append((gameCopy6.totalScore, move[1]))
				                                
        
    
    for move in validMoves:
        moves.append(move)
        
    #print moves
    if moves == []:
        return False
    else:
        highScore, bestMove = max(moves)
        if highScore !=0:
            return bestMove
        else:
            bestMove = random.choice(validMoves)
         
        
            
    return bestMove

start()
