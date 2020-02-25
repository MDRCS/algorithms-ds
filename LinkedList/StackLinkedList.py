#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:26:48 2019

@author: mdrahali
"""

class EmptyStackError(Exception):
    pass

class FullStackError(Exception):
    pass

class Node(object):
    
    def __init__(self,value):
        self.info = value 
        self.next = None

class Stack(object):
    
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
        return self.top == None
        
    def push(self,value):
        temp = Node(value)
        temp.next = self.top
        self.top = temp
        
    def pop(self):
        p = self.top
        self.top = self.top.next
        return p.info
        
    def display(self):
        if self.top is None:
            self.EmptyStackError("Stack is empty")
            
        p = self.top
        while p.next is not None:
            print(p.info)
            p = p.next
        print(p.info)
        
##############################################################################
            
if __name__ == "__main__":

    st = Stack() 

    while True:
        print()
        print("1- Display List")
        print("2- Add an element")
        print("3- Delete an element")
        print("4- Quit")
        
        option = int(input("Enter an option "))
        
        if option == 1:
            st.display()
        if option == 2:
            value = int(input("Enter a value please "))
            st.push(value)
        if option == 3:
            print(st.pop())
        if option == 4:
            break
