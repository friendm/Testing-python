'''
Created on May 23, 2011

@author: Michael Friend
'''

class node(object):
    '''
    this is a node object with an x,y,next and previous pointers
    '''


    def __init__(self,x,y,number):
        '''
        x value, y value, number
        '''
        self._x=x
        self._y=y
        next= 0
        previous=0
        
    def getx(self):
        '''returns x'''
        return node.x

    def gety(self):
        '''returns y'''
        return node.y
    def getnext(self):
        return node.next
    def getprev(self):
        return node.previous
    def getnumber(self):
        return node.number
    def setnext(self,x):
        node.next=x
    def setprev(self,x):
        node.previous=x
    
    def tostring(self):
        return "("+str(self.getx())+","+str(self.gety)+","+str(self.getnumber)+")"
            
