#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:06:12 2019

@author: mdrahali
"""

class EmptyQueueError(Exception):
    pass

class Queue:
    
    def __init__(self,max_size=8):
        self.items = [None] * max_size
        self.front = 0
        self.count = 0
        
    def enqueue(self,value):
        
        i = (self.front+self.count) % len(self.items)
        self.items[i] = value
        self.count+=1
        
    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueError("The queue is empty")
        
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front+1) % len(self.items)
        self.count-=1
        return x
    
    def isEmpty(self):
        return self.count == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.isEmpty():
            raise EmptyQueueError("The queue is empty")
        if self.front == 0 :
            return self.items[self.front]
        else:
            return self.items[self.front-1]
    
    def display(self):
        print(self.items)
        
    def resize(self,new_size):
        if new_size > self.count:
            old_list = self.items
            self.items = [None] * new_size
            
            i = self.front
            
            for j in range(self.count):
                self.items[j] = old_list[i]
                i = (i+1)%len(self.items)
            self.front = 0
        
################################################################################
  
      
if __name__ == "__main__":
    
    qu = Queue()
    
    while True:
        print()
        print("1- Display Queue")
        print("2- Add a case")
        print("3- Delete a case")
        print("4- Resize the queue")
        print("5- Quit ")
        
        option = int(input("Enter a choice please "))
        
        if option == 1:
           qu.display()
        if option == 2:
            value = int(input("Enter a value "))
            qu.enqueue(value)
        if option == 3:
            qu.dequeue()
        if option == 4:
            size = int(input("Enter a value "))
            qu.resize(size)
        if option == 5:
            break
        
        
        
        