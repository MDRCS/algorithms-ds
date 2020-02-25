#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 10:59:46 2019

@author: mdrahali
"""

class Node(object):
    
    def __init__(self,value):
        self.info = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList(object):
    
    def __init__(self):
        self.start = None
    
    def display_list(self):
        
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is")
            p = self.start
        
            while p is not None:
                print(p.info," ",end='')
                p=p.next
            print()
        
        
    def create_list(self):
        n = int(input("How much of nodes do you wanna create ?  "))
        
        if n==0:
            return
        
        p=self.start
        for i in range(n):
            data = int(input("Value of the node please : "))
            self.insert_endlist(data)
            
    def insert_endlist(self,data):
        temp = Node(data)
        
        if self.start is None:
            self.start = Node(data)
            return
        
        p = self.start
        
        while p.next is not None:
            p=p.next
        p.next = temp
            
    def insert_emptylist(self):
        
        data = int(input("Enter a value please"))
        self.start = Node(data)
        
    def insert_beginning(self):
        if self.start is None:
            self.insert_emptylist()
            return
        p = self.start
        data = int(input("Enter a value to add in the beginning"))
        temp = Node(data)
        p.prev = temp
        temp.next = p
        temp.prev = self.start
        p=p.prev
        self.start = p

    def insert_after_node(self,pos):
        if self.start is None:
            self.insert_emptylist()
            return
        
        data = int(input("Enter a value please :"))
        p = self.start
        count = 1
        while p.next is not None:
            if count == pos:
                print(p.info)
                nx=p.next
                temp = Node(data)
                temp.next = nx
                temp.prev = p
                p.next = temp
                nx.prev = temp
                return
            p=p.next
            count+=1
        
        if p.next is None and count==pos:
            self.insert_endlist(data)
            
            
            
                
    def insert_before_node(self,pos):
        if self.start is None:
            self.insert_emptylist()
            return
        
        p = self.start
        count = 1
        while p.next is not None:
            if count == pos:
                print(p.info)
                pr=p.prev
                data = int(input("Enter a value please :"))
                temp = Node(data)
                temp.next = p
                temp.prev = pr
                p.prev = temp
                pr.next = temp
                return
            p=p.next
            count+=1    
    
    def delete_firstnode(self):
        
        self.start = self.start.next
        self.start.prev = None
        
    def delete_lastnode(self):
        
        p = self.start
        
        while p.next.next is not None:
            p=p.next
        p.next = None
        
    def delete_anynode(self,pos):
        
        p = self.start 
        c=1
        while p.next is not None:
            if c == pos:
                break
            p=p.next
            c+=1
        
        if c == 1:
            self.delete_firstnode()
            
        if p.next is not None and c == pos:
            p.prev.next = p.next 
            p.next.prev = p.prev 
        else:
            if c == pos:
                p.prev.next = None
            else:
                print(pos," is not found ")
        
            
    def reverse_list(self):
        
        p=self.start
        prev=None
        while p is not None:
            next = p.next
            p.next = prev
            p.prev = next
            prev = p
            p = next
        self.start = prev
            
######################################################################################################
        
list = DoublyLinkedList()
list.create_list()


while True:
    print("1- Display the list")
    print("2- Insert in empty list")
    print("3- Insert a node in the end of the list")
    print("4- Insert a node in the beginning of the list")
    print("5- Insert a node after a specified node")
    print("6- Insert a node before a specified node")
    print("7- Delete first node")
    print("8- Delete last node")
    print("9- Delete any node")
    print("10- Reverse the list")
    print("11- Quit")
    
    option = int(input("Enter an option "))
    
    if option == 1:
        list.display_list()
    if option == 2:
        list.insert_emptylist()
    if option == 3:
        data = int(input("Enter a value please :"))
        list.insert_endlist(data)
    if option == 4:
        list.insert_beginning()
    if option == 5:
        pos = int(input("Enter a position please :"))
        list.insert_after_node(pos)
    if option == 6:
        pos = int(input("Enter a position please :"))
        list.insert_before_node(pos)
    if option == 7:
        list.delete_firstnode()
    if option == 8:
        list.delete_lastnode()
    if option == 9:
        pos = int(input("Enter a position please :"))
        list.delete_anynode(pos)
    if option == 10:
        list.reverse_list()
    if option == 11:
        break
        
