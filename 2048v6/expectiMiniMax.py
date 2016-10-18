from Game import *
from copy import deepcopy

""" 
ExpectiMiniMax searches down to a depth, alternating between the
valid moves at a given state and all the possible random tiles spawns
from each valid move.

At the bottom iteration, the program calculates a heuristic value for
each possible state and averages the value (as all possible spawns are
equally likely).  This value is passed back up the tree.  The move
that is most likely lead to a "better" state is chosen.

This implementation uses a combination of seven various heuristics to
compute the "goodness" of a state:
-- number of blank tiles
-- number of combine-able neighbors
-- highest tile on edge
-- highest tile in corner
-- decreasing or increasing horizontal edges
-- decreasing or increasing vertical edges
-- keeping higher tiles out of the middle

"""


def start():
    game = game2048()
    game.display()
    while game.getValidMoves() != []:
        move = nextMove(game)
        print 'move: ' + move
        game.operation(move)
        game.display()

def nextMove(game):
    """ nextMove() specifies the search depth and gets a move from
    expectiMiniMax() """
    z = game.countZeroes()
    """
    if z > 12:
        d = 2
    elif z > 8:
        d = 3
    else:
        d = 4
    """
    d = 3
    move = expectiMiniMax(game, d)
    return move

def expectiMiniMax(game, depth):
    """ expectiMiniMax() is the heart of the AI.  It alternates
    searching between valid moves and all possible random spawn of 2
    (4, being unlikely, is omitted to reduce the branching factor by a
    half).  At the bottom of the tree, the possible states (given a
    move) are averaged. """
    moves = game.getValidMoves()
    bestValue = None
    bestMove = None
    for move in moves:
        gameCopy = deepcopy(game)
        gameCopy.makeMove(move)
        val = chancePlay(gameCopy, depth - 1)
        if val > bestValue:
            bestValue = val
            bestMove = move
    return bestMove

def chancePlay(game, depth):
    """ chancePlay() generates all possibilities of a random
    generation of a 2.  Each state is passed to maxPlay().  When it
    reaches depth 0, the states' heuristic values are averaged and
    returned. """
    zeroes = game.locOfZeroes()
    if depth == 0 or len(zeroes) == 0:
        return value(game)
    val = 0.0
    for i,j in zeroes:
        gameCopy = deepcopy(game)
        gameCopy.v[i][j] = 2
        v = maxPlay(gameCopy, depth)
        val += v
    val /= len(zeroes)
    return val

def maxPlay(game, depth):
    """ maxPlay() generates a new state from each valid move.  Each
    state is passed back to chancePlay(), decrementing depth."""
    moves = game.getValidMoves()
    bestValue = 0
    for move in moves:
        gameCopy = deepcopy(game)
        gameCopy.makeMove(move)
        val = chancePlay(gameCopy, depth - 1)
        if val > bestValue:
            bestValue = val
    return bestValue


def value(game):
    """ value() is the brains of the AI.  It returns a heuristic value
    of each state
    """
    maxLocs = findMaxLoc(game)
    val = game.countZeroes() + friendlyNeighbors(game)/2
    if maxOnEdge(maxLocs):
        val *= 2
    if verticalEdge(game):
        val *= 2
    if horizontalEdge(game):
        val *= 2
    if maxInCorner(maxLocs):
        val *= 2
    if minimizeMiddle(game, maxLocs):
        val /= 1.4
    return val

def findMaxLoc(game):
    """ findMaxLoc() returns a list of the locations of the high tiles
    """
    board = game.v
    tempMax = 0
    maxLoc = []
    for i in range(4):
        for j in range(4):
            if board[i][j] > tempMax:
                tempMax = board[i][j]
                maxLoc = [(i,j)]
            elif board[i][j] == tempMax:
                maxLoc.append((i,j))
    return maxLoc

def maxOnEdge(maxLocs):
    """ maxOnEdge() returns True if all of the hightest tile are on
    edges"""
    for i,j in maxLocs:
        if i == 1 or i == 2 or j == 1 or j == 2:
            return False
    else:
        return True

def maxInCorner(maxLocs):
    """ maxInCorner() returns True if a high tile in a corner """
    for loc in maxLocs:
        i, j = loc
        if (i == 0 and j == 0) or (i == 0 and j == 3) or (i == 3 and j == 0) or (i == 3 and j == 3):
            return True
    return False

def verticalEdge(game):
    """ verticalEdge() returns True if the left and right edges are
    both increasing or both decreasing"""
    b = game.v
    inc = (b[0][0] >= b[1][0] >= b[2][0] >= b[3][0]) and (b[0][3] >= b[1][3] >= b[2][3] >= b[3][3])
    dec = (b[0][0] <= b[1][0] <= b[2][0] <= b[3][0]) and (b[0][3] <= b[1][3] <= b[2][3] <= b[3][3])
    return inc or dec

def horizontalEdge(game):
    """ horizontalEdge() returns True if the top and bottom edges are
    both increasing or both decreasing"""
    b = game.v
    inc = (b[0][0] >= b[0][1] >= b[0][2] >= b[0][3]) and (b[3][0] >= b[3][1] >= b[3][2] >= b[3][3])
    dec = (b[0][0] <= b[0][1] <= b[0][2] <= b[0][3]) and (b[3][0] <= b[3][1] <= b[3][2] <= b[3][3])
    return inc or dec

def minimizeMiddle(game, maxLoc):
    """ minimizeMiddle() returns True if any of the three highest
    tiles are in the middle--to be penalized in value()"""
    b = game.v
    i,j = maxLoc[0]
    highNum = b[i][j]
    midTiles = [(1,1), (1,2), (2,1), (2,2)]
    for k,l in midTiles:
        if b[k][l] >= highNum/4:
            return True
    else:
        return False
    
def friendlyNeighbors(game):
    """ friendlyNeighbors() returns the number of direct neighbors
    that are of the same tile"""
    b = game.v
    n = 0
    for i in range(3):
        for j in range(3):
            if b[i][j] == b[i+1][j]:
                n += 1
            if b[i][j] == b[i][j+1]:
                n += 1
    return n


start()
