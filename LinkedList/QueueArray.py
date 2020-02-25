#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:42:08 2019

@author: mdrahali
"""

class EmptyQueueError(Exception):
    pass

class Queue:
    
    def __init__(self):
        self.items = []
        self.front = 0
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,value):
        self.items.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueError("The queue is empty")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front +=1 
        return x
    
    def peek(self):
        if self.isEmpty():
            raise EmptyQueueError("The queue is empty")
        return self.items[0]
    
    def display(self):
        print(self.items)

############################################################

if __name__ == "__main__":  
    
    qu = Queue()
            
    while True:
        print()
        print("1- Display Queue")
        print("2- Add an item ")
        print("3- Delete an item")
        print("4- First item")
        print("5- Quit ")
        
        option = int(input("Enter a choice "))
        
        if option == 1:
            qu.display()
        if option == 2:
            value = int(input("Enter a value ! "))
            qu.enqueue(value)
        if option == 3:
            qu.dequeue()
        if option == 4:
            print(qu.peek())
        if option == 5:
            break