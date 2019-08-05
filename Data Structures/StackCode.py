# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:25:44 2019

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
        if self.is_empty:
            raise Empty('Stack is empty')
        return self.__data[-1]
    
    def pop(self):
        if self.is_empty:
            raise Empty('Stack is empty')
        return self.__data.pop()
    
    def get_data(self):
        print(self.__data)

obj1 = ArrayStack()
obj1.push(1)
obj1.push(2)
obj1.push(3)
obj1.push(4)
obj1.push(5)

obj1.get_data()

        
