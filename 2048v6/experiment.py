from Game import *
from copy import deepcopy

def start():
    game = game2048()
    game.display()
    while game.getValidMoves() != []:
        move = nextMove(game)
        print 'move: ' + move
        game.operation(move)
        game.display()

def silentPlay():
    game = game2048()
    while game.getValidMoves() != []:
        move = nextMove(game)
        game.operation(move)
    maxLoc = findMaxLoc(game)
    i,j = maxLoc[0]
    game.display()
    return (game.totalScore, game.v[i][j])

def runMany():
    n = 50
    m = 50
    highScore = 0
    lowScore = 1000000
    meanScore = 0
    n64 = 0
    n128 = 0
    n256 = 0
    n512 = 0
    n1024 = 0
    n2048 = 0
    n4096 = 0
    n8192 = 0
    other = 0
    while n > 0:
        print n
        score, high = silentPlay()
        if high == 64:
            n64 +=1
        if high == 128:
            n128 +=1
        if high == 256:
            n256 +=1
        if high == 512:
            n512 +=1
        if high == 1024:
            n1024 +=1
        if high == 2048:
            n2048 +=1
        if high == 4096:
            n4096 +=1
        if high == 8192:
            n8192 +=1
        meanScore += score
        if score < lowScore:
            lowScore = score
        if score > highScore:
            highScore = score
        n -=1
    meanScore /= m
    print 'low:', lowScore
    print 'mean:', meanScore
    print 'high', highScore
    print '64:', n64
    print '128:', n128
    print '256:', n256
    print '512:', n512
    print '1024:', n1024
    print '2048:', n2048
    print '4096:', n4096
    print '8192:', n8192
    print 'other??', other


def nextMove(game):
    """
    z = game.countZeroes()
    if z > 9:
        d = 2
    elif z > 6:
        d = 3
    else:
        d = 4
        """
    move = expectiMiniMax(game, 3)
    return move

def expectiMiniMax(game, depth):
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
    """ heuristic!  this is where all of deciding magic will
    happen! """
    val = game.countZeroes() +  1 #friendlyNeighbors(game)/2
    maxLocs = findMaxLoc(game)
    if maxOnEdge(game, maxLocs):
        val *= 2
    if verticalEdge(game):
        val *= 2
    if horizontalEdge(game):
        val *= 2
#    if maxInCorner(game):
#        val *= 2
    if minimizeMiddle(game, maxLocs):
        val /= 1.5
    return val

def findMaxLoc(game):
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

def maxOnEdge(game, maxLocs):
    board = game.v
    for loc in maxLocs:
        i, j = loc
        if i == 1 or j == 2 or i == 1 or j == 2:
            return False
    else:
        return True

def maxInCorner(game):
    board = game.v
    maxLocs = findMaxLoc(game)
    for loc in maxLocs:
        i, j = loc
        if (i == 0 and j == 0) or (i == 0 and j == 3) or (i == 3 and j == 0) or (i == 3 and j == 3):
            return True
    return False


def verticalEdge(game):
    b = game.v
    inc = (b[0][0] >= b[1][0] >= b[2][0] >= b[3][0]) and (b[0][3] >= b[1][3] >= b[2][3] >= b[3][3])
    dec = (b[0][0] <= b[1][0] <= b[2][0] <= b[3][0]) and (b[0][3] <= b[1][3] <= b[2][3] <= b[3][3])
    return inc or dec

def horizontalEdge(game):
    b = game.v
    inc = (b[0][0] >= b[0][1] >= b[0][2] >= b[0][3]) and (b[3][0] >= b[3][1] >= b[3][2] >= b[3][3])
    dec = (b[0][0] <= b[0][1] <= b[0][2] <= b[0][3]) and (b[3][0] <= b[3][1] <= b[3][2] <= b[3][3])
    return inc or dec

def minimizeMiddle(game, maxLoc):
    b = game.v
    i,j = maxLoc[0]
    highNum = b[i][j]
    midTiles = [(1,1), (1,2), (2,1), (2,2)]
    for k,l in midTiles:
        if b[k][l] >= highNum/2:
            return True
    else:
        return False
    
def friendlyNeighbors(game):
    b = game.v
    n = 0
    for i in range(3):
        for j in range(3):
            if b[i][j] == b[i+1][j]:
                n += 1
            if b[i][j] == b[i][j+1]:
                n += 1
    return n
    
runMany()
#start()
