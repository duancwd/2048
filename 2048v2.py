# -*- coding: utf-8 -*-
"""
 

"""
 
import random
 
class game2048:
    totalScore = 0
 

    v = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    
    def __init__(self):
        '''
        self.v=[[0, 0, 0, 0],
                [0, 0, 0, 0],
                [2, 4, 8, 2],
                [1, 1, 1, 1]]'''
        for i in range(4):
            self.v[i] = [random.choice([0,0,0,0,0,0,0,0,0,2,2,4]) for x in range(4)]
 
 
    def display(self):
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[0][0], self.v[0][1], self.v[0][2], self.v[0][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[1][0], self.v[1][1], self.v[1][2], self.v[1][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[2][0], self.v[2][1], self.v[2][2], self.v[2][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(self.v[3][0], self.v[3][1], self.v[3][2], self.v[3][3]))
        print('score:{0:4}'.format(self.totalScore))
        #print('is it over?:{0:4}'.format(self.isOver()))
   
    def align(self,vList, direction):
        for i in range(vList.count(0)):
            vList.remove(0)
        zeros = [0 for x in range(4-len(vList))]
        if direction == 'left':
            vList.extend(zeros)
        else:
            vList[:0] = zeros
    
   
    def addSame(self,vList, direction):
        increment=0
        if direction == 'left':
            for i in [0,1,2]:
                if vList[i]==vList[i+1] and vList[i+1]!=0:
                    vList[i] *= 2
                    vList[i+1] = 0
                    increment += vList[i]
        else:
            for i in [3,2,1]:
                if vList[i]==vList[i-1] and vList[i-1]!=0:
                    vList[i] *= 2
                    vList[i-1] = 0
                    increment += vList[i]
        return increment
    #处理行和方向,返回新增积分
    def handle(self, vList, direction):
        self.align(vList, direction)
        increment = self.addSame(vList, direction)
        self.align(vList, direction)
        self.totalScore += increment #直接加到总值
        return increment
    
    def judge(self):
         
        if self.isOver():
            print('GAME OVER!')
            return False
            
        else:
             
            if max(max(self.v)) >= 2048:
                print('you win, but you can keep going')
            return True
   
    def isOver(self):
        
        N = self.calcCharNumber(0)
        if N!=0:
            return False
        else:
            for row in range(4):
                flag = self.isListOver(self.v[row])
                
                if flag==False:
                    return False   
            for col in range(4):
                
                vList = [self.v[row][col] for row in range(4)]
                flag = self.isListOver(vList)
                if flag==False:
                    return False
        return True
     
    
    def isListOver(self, vList):
        for i in [0,1,2]:
            if vList[i]==vList[i+1] and vList[i+1]!=0:
                return False
        return True
    def calcCharNumber(self, char):
        n = 0
        for q in self.v:
            n += q.count(char)
        return n
    def addElement(self):
        # 统计空白区域数目 N
        N = self.calcCharNumber(0)
        if N!=0:
            # 按2和4出现的几率为3/1来产生随机数2和4
            num = random.choice([2, 2, 2, 4]) 
            # 产生随机数k，上一步产生的2或4将被填到第k个空白区域
            k = random.randrange(1, N+1)    #k的范围为[1,N]
            n = 0
            for i in range(4):
                for j in range(4):
                    if self.v[i][j] == 0:
                        n += 1
                        if n == k:
                            self.v[i][j] = num
                            return


 
                 
    def moveLeft(self):
        self.moveHorizontal('left')
    def moveRight(self):
        self.moveHorizontal('right')
    def moveHorizontal(self, direction):
        for row in range(4):
            self.handle(self.v[row], direction)
 
    def moveUp(self):
        self.moveVertical('left')
    def moveDown(self):
        self.moveVertical('right')
    def moveVertical(self, direction):
        for col in range(4):
            # 将矩阵中一列复制到一个列表中然后处理
            vList = [self.v[row][col] for row in range(4)]
            self.handle(vList, direction)
            # 从处理后的列表中的数字覆盖原来矩阵中的值
            for row in range(4):
                self.v[row][col] = vList[row]
                 
    #主要的处理函数
    def operation(self):
        #op = random.choice(['w','a'])
        
        op = input('operator:')
        print('operation is '+ op +"\n\r")
        if op in ['a', 'A']:
            #if self.validmove(op):   # 向左移动
                self.moveLeft()
                self.addElement()
        elif op in ['d', 'D']:
           # if self.validmove(op):  # 向右移动
                self.moveRight()
                self.addElement()
        elif op in ['w', 'W']:
           # if self.validmove(op):  # 向上移动
                self.moveUp()
                self.addElement()
        elif op in ['s', 'S']:
           # if self.validmove(op):  # 向下移动
                self.moveDown()
                self.addElement()
        else:
            print('error. please a valid move or  type [W, S, A, D] or[w, s, a, d]')




    def isvalid(self,vList, direction):
        copy_vList=[]
        copy_vList1=[]
        copy_vList.extend(vList)
        copy_vList1.extend(vList)
        print copy_vList
        for i in range(copy_vList1.count(0)):
            copy_vList1.remove(0)
        zeros = [0 for x in range(4-len(copy_vList1))]
        if direction == 'left':
           copy_vList1.extend(zeros)
           new_vList = copy_vList1
           if copy_vList == new_vList:
                return False
        else:
            copy_vList1[:0] = zeros
            new_vList = copy_vList1
            if copy_vList == new_vList:
                return False
            


    def validmove(self,op):
        N = self.calcCharNumber(0)
        print N
        if N!=0:
             if op in ['a', 'A','d', 'D']:
                
                for col in range(4):
                    vList = [self.v[row][col] for row in range(4)]
                    flag = self.isListOver(vList)
                    if flag==False:
                        if op in ['a', 'A']:
                            if self.isvalid(vList, 'left') == False:
                                print 'you cannot left, try to other way'
                            return self.isvalid(vList, 'right')
                        elif op in ['d', 'D']:
                            if self.isvalid(vList, 'right') ==False:
                                print 'you cannot right, try to other way'
                            return self.isvalid(vList, 'lift')
             elif op in ['s', 'S','w', 'W']:
                 for row in range(4):
                    flag = self.isListOver(self.v[row])
                    if flag==False:
                        if op in ['s', 'S']:
                            if self.isvalid(self.v[row], 'left')== False :
                                #print self.v[row]
                                print 'you cannot Donw, try to other way'
                            return self.isvalid(self.v[row], 'left')
                        elif op in ['w', 'W']:
                            if self.isvalid(self.v[row], 'right'):
                                print 'you cannot up, try to other way'
                            return self.isvalid(self.v[row], 'right')
                
        else:
            if op in ['a', 'A','d', 'D']:
                for col in range(4):
                    vList = [self.v[row][col] for row in range(4)]
                    flag = self.isListOver(vList)
                    if flag==False:
                        print 'you cannot to move, try to other way'
                        return False
                
            elif op in ['s', 'S','w', 'W']:
                for row in range(4):
                    flag = self.isListOver(self.v[row])
                    if flag==False:
                        print 'you cannot to move, try to other way'
                        return False
                
        return True
                
                
            
        
        
        


    
#begin
def start():
        print('Input：W(up) S(down) A(left) D(right), press <CR>.')
        g =game2048()
        flag = True
        while flag==True:
            g.display()
            flag = g.judge()
            g.operation()
            
            flag = g.judge()
start()

