# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:57:03 2019

@author: Sankar Biswas
"""

class ArrayStack:
    
    def __init__(self):
        
        self.__data = []
        
    def length(self):
        return len(self.__data)   
    
    def is_empty(self):
        return len(self.__data) == 0
    
    def push(self,e):
        self.__data.append(e)
        
    def top(self):
        if self.is_empty():
            raise TypeError('Stack is empty')
        return self.__data[-1]
    
    def pop(self):
        if self.is_empty():
            raise TypeError('Stack is empty')
        return self.__data.pop()
    
    def get_data(self):
        print(self.__data)
        
def parenthesis_match(expr):
    righty = ')}]'
    lefty = '({['
    stack = ArrayStack()
    for c in expr:
        if c in lefty:
            stack.push(c)
        elif c in righty:
            if stack.is_empty():
                return False
            if righty.index(c) != lefty.index(stack.pop()):
                return False
    return stack.is_empty()

obj1 = parenthesis_match("[({(}))]")
print(obj1)
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
