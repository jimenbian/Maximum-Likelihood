'''
Created on 2014-8-22
@author: Garvin
Maximum Likelihood theory practic

This code is base on the http://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E4%BC%BC%E7%84%B6%E4%BC%B0%E8%AE%A1
'''
w=2.0/3
h=49
t=31

def DefineParam():
    H=h
    T=t
    return H,T

def MaximumLikelihood(p=w):
    H,T=DefineParam()
    f1=Factorial(H+T)/(Factorial(H)*Factorial(T))
    
    f2=(p**H)*((1.0-p)**T)
    
    
    return f1*f2
    
    
def Factorial(x):
    return reduce(lambda x,y:x*y,range(1,x+1))    
    
    
print MaximumLikelihood()
    
    
    
    
    
    