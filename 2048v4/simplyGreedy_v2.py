from Game import *

from copy import deepcopy





#begin
def start():
        print('Input:W(up) S(down) A(left) D(right), press <CR>.')
        g =game2048()
        gamecopy = game2048()
        g.display()
        flag = True
        while flag==True:
            opbestmove = simplyGreedy(g,gamecopy)
            for x in range(1):
                op= opbestmove[0]
                flag = g.judge()
                print ('operation is : ' +op)
                if g.validmove(op)==True:
                    print ('operation is : ' +op)
                    g.operation(op)
                else:
                    op = random.choice(['w','a','s','d'])
                    print ('operation is : ' +op)
                    g.operation(op)
                    
                flag = g.judge()
                g.display()



def simplyGreedy(g,gamecopy):
        op =''
        maxnumb=0
        oplist=[['w','w'],['w','a'],['w','s'],['w','d'],['a','w'],['a','a'],['a','s'],['a','d'],['s','w'],['s','a'],['s','s'],['s','d'],['d','w'],['d','a'],['d','s'],['d','d']]
        copylist =[]
        copylist.extend(g.v)
        copylist1=[]
        copylist1 =deepcopy(copylist)
        #print copylistall
        #print'original'
        #print copylist
        bestmove=[]
        tempScore=[]
        lasttime=gamecopy.totalScore
        for i in range(16):
                #print'original'
                #print copylist1
                #tempScore=[]
                oplist2 = oplist[i]
                gamecopy.v = []
                gamecopy.v=deepcopy(copylist1)
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


