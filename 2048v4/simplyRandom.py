from Game import *
from copy import deepcopy





#begin
def start():
        print('Input:W(up) S(down) A(left) D(right), press <CR>.')
        g =game2048()
        g.display()
        #print g
        flag = True
        while flag==True:
            
            flag = g.judge()
            op = random.choice(['w','a','s','d'])
            print ('operation is : ' +op)
            g.operation(op)
            flag = g.judge()
            g.display()
start()
