#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:01:44 2019

@author: mdrahali
"""

class EmptyDequeError(Exception):
    pass

class Deque(object):
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def insert_front(self,value):
        
       self.items.insert(0,value)
       
    def insert_back(self,value):      
        self.items.append(value)
    
    def delete_front(self):
        if self.isEmpty():
            raise EmptyDequeError("Deque is empty")
        self.items.pop(0)
    
    def delete_back(self):
        if self.isEmpty():
            raise EmptyDequeError("Deque is empty")
        self.items.pop()
        
    def first(self):
        if self.isEmpty():
            raise EmptyDequeError("Deque is empty")
            
        return self.items[0]
    
    def last(self):
         if self.isEmpty():
            raise EmptyDequeError("Deque is empty")
         return self.items[-1]
    
    def display(self):
        print(self.items)
        
#########################################################################
        
if __name__ == "__main__":
    deque = Deque()
    while True:
        print()
        print("1- Display List")
        print("2- Insert in the beginning of the deque ")
        print("3- Insert in the end of deque")
        print("4- delete in the beginning")
        print("5- delete in the end")
        print("6- Quit")
        
        option = int(input("Enter a choice please "))
        
        if option == 1:
            deque.display()
        if option == 2:
            item = int(input("Enter a value"))
            deque.insert_front(item)
        if option == 3:
            item = int(input("Enter a value"))
            deque.insert_back(item)
        if option == 4:
            deque.delete_front()
        if option == 5:
            deque.delete_back()
        if option == 6:
            break
        
        
    
    
        