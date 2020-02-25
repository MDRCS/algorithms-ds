#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:51:03 2019

@author: mdrahali
"""

class EmptyQueueError(Exception):
    pass

class Node(object):
    
    def __init__(self,value):
        self.info = value
        self.next = None
        
class Queue(object):
    
    def __init__(self):
        self.front = None
        self.back = None
    
    def isEmpty(self):
         return self.front == self.back == None
     
    def enqueue(self,value):
        temp = Node(value)
        
        if self.isEmpty():
            self.back = temp
            self.front = temp
            return
        
        self.back.next = temp
        self.back = temp 
        
  
    def dequeue(self):
        p = self.front
        self.front = self.front.next
        return p.info
    
    def peek(self):
        return self.front
        
    def display(self):
        
        p = self.front
        
        while p is not None:
            print(p.info)
            p = p.next
            
#################################################
            
if __name__ == "__main__":

    Q = Queue()
    
    while True:
        print()
        print("1- Display Queue ")
        print("2- Add a new node to the Queue ")
        print("3- Delete a node")
        print("4- Quit")
        
        option = int(input("Enter a value please !"))
        
        if option == 1:
            Q.display()
        if option == 2:
            value = int(input("Enter the value that you want to Add !"))
            Q.enqueue(value)
        if option == 3:
            Q.dequeue()
        if option == 4:
            break
        