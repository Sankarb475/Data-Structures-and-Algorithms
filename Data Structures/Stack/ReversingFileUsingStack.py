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
        if self.is_empty():
            raise TypeError('Stack is empty')
        return self.__data[-1]
    
    def pop(self):
        if self.is_empty():
            raise TypeError('Stack is empty')
        return self.__data.pop()
    
    def get_data(self):
        print(self.__data)


def reverse_file(filename):
    stack = ArrayStack()
    lines = open(filename)
    for i in lines:
        stack.push(i.rstrip('\n'))
    lines.close()
    stack.get_data()
    while not stack.is_empty():
        print(stack.pop())

obj1 = reverse_file("C:/Users/sb512911/Desktop/All/data/pythonStack.txt")
