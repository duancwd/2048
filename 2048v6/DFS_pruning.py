from Game import *
from copy import deepcopy


f = file('./test.txt','w+')
def start():
    game = game2048()
    game.display()
    op = nextMove(game)
    bestsum = 0
    bestscore = 0
    while op:
        print 'move: ' + str(op)
        game.operation(op)
        game.display()
        print ''
        op = nextMove(game)
    bestsum = max([max(game.v[0]),max(game.v[1]),max(game.v[2]),max(game.v[3])])
    
    bestscore = game.totalScore   
    game.display()
    
    return [bestsum,bestscore,str(game.v)]

def nextMove(game):
    count = 0
    for n in range(4):
        for m in range(4):
            if game.v[n][m]==0:
                        count +=1
                        
    # This part works when score is over 27000. Try to make 4096 happens more often
    if game.totalScore>27000 and count <3:
        oplistO =['left','right','up','down']
       
    # Look ahead 7 steps
        moves =[]
        for x in range(4):
            for y in range(4):
                for z in range(4):
                        for n in range(4):
                            for m in range(4):
                                for o in range(4):
                                    for a in range(4):
                                        moves.append([oplistO[x],oplistO[y],oplistO[z],oplistO[n],oplistO[m],oplistO[o],oplistO[a]])
        

		# Find move with best score
        validMoves = []
        for movelist in moves:
            Score=0
            gameCopy = deepcopy(game)
            for move in movelist:
                if gameCopy.operation(move) != False:
                    Score +=gameCopy.totalScore
                    validMoves.append((Score, movelist[0]))
                else:
                    break
    #print validMoves
    
    
    	# This part checks if there is any valid move. If there is none, Game Over.
        if validMoves == []:
            return False
        else:
            maxmovelist=[]
            highScore, bestMove = max(validMoves)
            for x in validMoves:
                if x[0]==highScore:
                     maxmovelist.append(x[1])
            for y in maxmovelist:
                gameCopy1 = deepcopy(game)
                gameCopy1.operation(y)
                tempmax = max([max(gameCopy1.v[0]),max(gameCopy1.v[1]),max(gameCopy1.v[2]),max(gameCopy1.v[3])])
                if gameCopy1.v[0][0] == tempmax or gameCopy1.v[0][3] == tempmax or gameCopy1.v[3][0]== tempmax or gameCopy1.v[3][3]== tempmax:
                    bestMove = y
            if highScore !=0:
                return bestMove
            else:
                bestMove = random.choice(validMoves)
    
        return bestMove
        
        
    # If number of blank tiles is more than 5, we look ahead 5 steps
    elif count >5:
        oplistO =['left','right','up','down']
    
        moves =[]
        for x in range(4):
            for y in range(4):
                for z in range(4):
                        for n in range(4):
                            for m in range(4):
                                    moves.append([oplistO[x],oplistO[y],oplistO[z],oplistO[n],oplistO[m]])
        

    	# Get the move with best score
        validMoves = []
        for movelist in moves:
            Score=0
            gameCopy = deepcopy(game)
            for move in movelist:
                if gameCopy.operation(move) != False:
                    Score +=gameCopy.totalScore
                    validMoves.append((Score, movelist[0]))
                else:
                    break
    #print validMoves
    
    	# This part checks if there is any valid move. If there is none, Game Over.
        if validMoves == []:
                         
            return False
        else:
            countlist=[]
            maxmovelist=[]
            highScore, bestMove = max(validMoves)
            for x in validMoves:
                if x[0]==highScore:
                     maxmovelist.append(x[1])
          
            for y in maxmovelist:
                gameCopy1 = deepcopy(game)
                gameCopy1.operation(y)
                count = 0
                for n in range(4):
                    for m in range(4):
                        if gameCopy1.v[n][m]==0:
                            count +=1
                countlist.append([count,y])
            bestcount,bestMove = max(countlist)
            
            if highScore !=0:
                return bestMove
            else:
                bestMove = random.choice(validMoves)
         
        return bestMove
        
        
    # Normal situation, look ahead 5 steps.    
    else:
        oplistO =['left','right','up','down']
    
        moves =[]
        for x in range(4):
            for y in range(4):
                for z in range(4):
                        for n in range(4):
                            for m in range(4):
                                for o in range(4):
                                    moves.append([oplistO[x],oplistO[y],oplistO[z],oplistO[n],oplistO[m],oplistO[o]])
        

    	# Find move with best score
        validMoves = []
        for movelist in moves:
            Score=0
            gameCopy = deepcopy(game)
            for move in movelist:
                if gameCopy.operation(move) != False:
                    Score +=gameCopy.totalScore
                    validMoves.append((Score, movelist[0]))
                else:
                    break
                    
                    
    #print validMoves
    
    	# This part checks if there is any valid move. If there is none, Game Over.
        if validMoves == []:
            return False
        else:
            countlist=[]
            maxmovelist=[]
            highScore, bestMove = max(validMoves)
            for x in validMoves:
                if x[0]==highScore:
                     maxmovelist.append(x[1])
          
            for y in maxmovelist:
                gameCopy1 = deepcopy(game)
                gameCopy1.operation(y)
                count = 0
                for n in range(4):
                    for m in range(4):
                        if gameCopy1.v[n][m]==0:
                            count +=1
                countlist.append([count,y])
            bestcount,bestMove = max(countlist)
            if highScore !=0:
                return bestMove
            else:
                bestMove = random.choice(validMoves)
         
        
            
        return bestMove
        
        

# Main --------------------------------------------    
# Set how many time we want to run the game
x= 1
# List of Scores gained in each game
Slist =[]
# List of Best tile in each game
Rlist =[]
bestsum=0
bestscore=0
twocount = 0
onecount = 0
display = ""

# Run the games
for i in range(x):
     print i
     f.write(str(i)+"\n\r")
     bestsum,bestscore,display= start()
     f.write(str(display)+"\n\r")
     print bestscore
     print bestsum
     Slist.append(bestscore)
     Rlist.append(bestsum)
     if bestsum >=2048:
            twocount +=1
     if bestsum >=1024:
            onecount +=1

# Print the results to file
f.write(str(Slist)+"\n\r")
f.write("times :" +str(x)+"\n\r")
f.write("the best Score : "+ str(max(Slist))+"\n\r")
f.write("the best sum : "+str(max(Rlist))+"\n\r")
f.write("2048 : "+str(twocount)+"/"+str(x)+"\n\r")
f.write("1024 : "+str(onecount)+"/"+str(x)+"\n\r")
f.read()
f.close()

# Print the results to console
print Slist          
print "times :" +str(x)
print "the best Score : "+ str(max(Slist))
print "the best sum : "+str(max(Rlist))
print "2048 : "+str(twocount)+"/"+str(x)
print "1024 : "+str(onecount)+"/"+str(x)
   

