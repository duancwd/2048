from Game import *
from copy import deepcopy

def start():
        g = game2048()
        gamecopy = deepcopy(g)
        g.display()
        flag = True
        while flag==True:
            flag = g.judge()
            op = simplyGreedy(g,gamecopy)
            print ('operation is: ' +op)
            if g.validMove(op)==True:
                    print 'operation is: ' + op
                    g.operation(op)
            else:
                    op = random.choice(['left', 'right', 'up', 'down'])
                    print 'operation is : ' + op
                    g.operation(op)
                    
            flag = g.judge()
            g.display()



def simplyGreedy(g,gamecopy):
        op = ''
        maxnumb = 0
        oplist = ['left', 'right', 'up', 'down']
        copylist = []
        copylist.extend(g.v)
        copylist1 = []
        copylist1 = deepcopy(copylist)
        #print copylistall
        #print'original'
        #print copylist
        bestmove = ''
        tempScore = []
        lasttime = gamecopy.totalScore
        for i in range(4):
                #print'original'
                #print copylist1
                #tempScore = []
                op = oplist[i]
                gamecopy.v = []
                gamecopy.v = deepcopy(copylist1)
                #print'originalMidbefore'
               # print gamecopy.v
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
                
        for j in range(4):
                if maxnumb == tempScore[j]:
                        bestmove = oplist[j]
       # print'originalag'
       # print copylist
        return bestmove
                                
                
start()


