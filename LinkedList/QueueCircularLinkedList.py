#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:58:04 2019

@author: mdrahali
"""

class Node(object):
    
    def __init__(self,value):
        self.info = value
        self.next = None
    
class CircularQueue(object):
    
    def __init__(self):
        self.rear = None
        
    def isEmpty(self):
        return self.rear == None
    
    def enqueue(self,value):
        temp = Node(value)
        if self.isEmpty():
            temp.next = temp 
            self.rear = temp
            return
        
        p = self.rear
        nx = p.next
        p.next = temp
        temp.next =nx
        self.rear = temp

        
    def dequeue(self):
        
        if self.isEmpty():
            return
        
        p = self.rear
        if self.rear.next == p:
            self.rear = None
        else: 
            p = self.rear.next
            self.rear.next = p.next
            p.next = None
            
        
        
    
    def display(self):
        #print(self.rear.info)
        if self.isEmpty():
            return
        
        p = self.rear
        p = p.next
        while p != self.rear:
            print(p.info)
            p = p.next
        print(p.info)
        
        
    def peek(self):
        if self.isEmpty():
            return
        
        if self.rear.next is None:
            return self.rear.info
        return self.rear.next.info
    
##################################################################
        
if __name__ == "__main__":
    
    qu = CircularQueue()
    
    while True:
        print()
        print("1- Display Queue")
        print("2- Add a value")
        print("3- Delete a Value")
        print("4- The first value in the queue")
        print("5- Quit")
        
        option = int(input("Enter an option "))
        
        if option == 1:
            qu.display()
        if option == 2:
            value = int(input("Enter a value "))
            qu.enqueue(value)
        if option == 3:
            qu.dequeue()
        if option == 4:
            print(qu.peek())
        if option == 5:
            break
        
    
    
    
    
    
    
    