'''
Created on May 20, 2011

@author: Michael Friend
'''

import node

def squareofsums(n):
    a=range(n)
    sum=0
    for x in a:
        sum+=x
    sum*=sum
    return sum


def sumofsquares(n):
    a=range(n)
    sum=0
    for x in a:
        sum+=(x*x)
    return sum


    
    
def factorial(n):
    a=range(1,n+1)
    sum=1
    for x in a:
        sum =x*sum
    return sum


def raisetothepowerof(j,n):
    a=range(n)
    sum=1
    for x in a:
        sum*=j
        
    return sum


def sumofindividualsquaring(n):
    """ takes the sum of raising each number in a sequence to 1000
    and sums them
    """
    sum=0
    for x in range(1,n+1):
        sum+= raisetothepowerof(x,x)
    return sum
    
def nodemaker(n):
    a=[]
    for x in range(n):
        y= node(x,x,x)
        a.append(y)   
    return a
          

 
number=5
test= 'word'+ str(5)
word ='square of sums problem:' +' '+  str(squareofsums(101)-sumofsquares(101))
word2='factorial problem:'+' '+ str(factorial(20))
word3= 'Sum of individual squaring:' + ' '+ str(sumofindividualsquaring(1000))
number= len(word3)
print word
print word2
print word3
print 'node test: ' +str(nodemaker (3))




