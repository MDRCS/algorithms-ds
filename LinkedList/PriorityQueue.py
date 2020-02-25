#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:50:38 2019

@author: mdrahali
"""

class EmptyQueueError(Exception):
    pass

class Node(object):
    
    def __init__(self,index,value):
        self.info = value
        self.index = index
        self.next = None
        
class PriorityQueue(object):
    
    def __init__(self):
        self.front = None
        
    def isEmpty(self):
        return self.front == None
    
    def enqueue(self,index,value):
        temp = Node(index,value)
        
        if self.isEmpty() or self.front.index > temp.index:
            temp.next = self.front
            self.front = temp
        else:
            p = self.front
            while p.next != None and p.next.index < temp.index:
                p = p.next
            temp.next = p.next
            p.next = temp 
            
        
    def dequeue(self):
        
        if self.isEmpty():
            raise EmptyQueueError("the queue is empty")
        
        p = self.front
        
        self.front = self.front.next
        p.next = None
        
    def display(self):
        if self.isEmpty():
            raise EmptyQueueError("the queue is empty")
            
        p = self.front
        while p is not None:
            print(p.info," - index : ", p.index)
            p = p.next
        print()


#####################################################

if __name__ == "__main__":
    
    qu = PriorityQueue()
    
    while True:
        print()
        print("1- Display Queue elements")
        print("2- Add a element")
        print("3- Delete an element")
        print("4- Quit")

    
        option = int(input("Enter a choice "))
        
        if option == 1:
            qu.display()
        if option == 2:
            value = int(input("Enter a value please "))
            index = int(input("Enter a priority "))
            qu.enqueue(index,value)
        if option == 3:
            qu.dequeue()
        if option == 4:
            break












        