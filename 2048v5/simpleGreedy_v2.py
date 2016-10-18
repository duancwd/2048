from Game import *
from copy import deepcopy


def start():
    game = game2048()
    game.display()
    op = simplyGreedy(game)
    while op:
        print 'move: ' + str(op)
        game.operation(op)
        game.display()
        print ''
        op = simplyGreedy(game)



def simplyGreedy(game):
        gamecopy = deepcopy(game)
        op = ''
        maxnumb = 0
        # THIS NEEDS TO BE TWO FOR LOOPS
        oplist = [['left', 'left'], ['left', 'right'], 
                  ['left', 'up'], ['left', 'down'],
                  ['right', 'left'], ['right', 'right'], 
                  ['right', 'up'], ['right', 'down'],
                  ['up', 'left'], ['up', 'right'], 
                  ['up', 'up'], ['up', 'down'],
                  ['down', 'left'], ['down', 'right'], 
                  ['down', 'up'], ['down', 'down']]
        copylist = []
        copylist.extend(game.v)
        copylist1 = []
        copylist1 = deepcopy(copylist)
        #print copylistall
        #print'original'
        #print copylist
        bestmove = []
        tempScore = []
        lasttime = gamecopy.totalScore
        for i in range(16):
                #print'original'
                #print copylist1
                #tempScore = []
                oplist2 = oplist[i]
                gamecopy.v = []
                gamecopy.v = deepcopy(copylist1)
                #print'originalMidbefore'
               # print gamecopy.v
                for j in range(2):
                    op = oplist2[j]
                    gamecopy.operation(op)
               # print'originalMidafter'
               # print gamecopy.v
                tempScore.append(gamecopy.totalScore)
                #print 'before'
                #print gamecopy.totalScore
                gamecopy.totalScore = lasttime
                #print 'after'
                #print gamecopy.totalScore
                
                
        maxnumb = max(tempScore)
                
        for j in range(16):
                if maxnumb == tempScore[j]:
                        bestmove=oplist[j]
       # print'originalag'
       # print copylist
        return bestmove
                                
                
start()


