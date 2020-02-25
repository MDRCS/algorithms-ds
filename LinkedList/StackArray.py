#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:20:15 2019

@author: mdrahali
"""

class EmptyStackError(Exception):
    pass

class FullStackError(Exception):
    pass

class Stack:
    
    def __init__(self,max_size=20):
        self.items = [None] * max_size
        self.count = 1
        
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == len(self.items)
    
    def push(self,item):
        if self.isFull():
            raise FullStackError("The stack is full")
        self.items[self.count] = item
        self.count+=1
        
    def pop(self):
        if self.isEmpty():
            raise EmptyStackError("Stack is empty")
        x = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count-=1
        return x
    
    def peek(self):
        if self.isEmpty():
            raise EmptyStackError("Stack is empty")
        return self.items[self.count-1] #-1 give you the index of the latest item ( == len -1)
        
    def display(self):
        print(self.items)
        
if __name__ == "__main__":
    
    st = Stack()

    while True:
        print()
        print("1- Check if the stack is empty ")
        print("2- Add a node ")
        print("3- Delete a node")
        print("4- Get the last node")
        print("5- Display list")

        option = int(input("Choice a value : "))

        if option == 1:
            print(st.isEmpty())
        if option == 2:
            item = int(input("Enter a value to be added : "))
            st.push(item)
        if option == 3:
            print(st.pop())
        if option == 4:
            print(st.peek())
        if option == 5:
            st.display()
    

    