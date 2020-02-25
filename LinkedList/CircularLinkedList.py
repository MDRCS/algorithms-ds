#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:27:27 2019

@author: mdrahali
"""

class Node(object):
    
    def __init__(self,value):
        self.info = value
        self.next = None
    
class CircularLinkedList(object):
    
    def __init__(self):
        self.last = None
        
    def display_list(self):
        if self.last is None:
            return
        
        p=self.last
        p=p.next
        while p != self.last:
            print(p.info," ",end='')
            p=p.next
        print(p.info," ",end='')
        print()
        
        
        
    def insert_beginning(self,data):
        
        p = self.last
        nx = p.next
        temp = Node(data)
        temp.next = nx
        p.next = temp

        
        
    def insert_emptylist(self,data):
        
        if self.last is None:
            temp = Node(data)
            self.last = temp
            temp.next = temp
            return

        
    def insert_endlist(self,data):
        
        if self.last is None:
            self.insert_emptylist(data)
            return
        else:
            p= self.last 
            fr = p.next
            temp = Node(data)
            p.next = temp
            self.last = temp
            temp.next = fr
            return
        
        
    def create_list(self):
        
        n = int(input("please enter the number of nodes for this list ! : "))
        for i in range(n):
            data = int(input("Enter the value that you want to add please "))
            self.insert_endlist(data)

        
    def insert_after(self,value):
        
        if self.last is None:
            return
        
        p = self.last
        p = p.next
        while p != self.last:
            if p.info == value:
                data = int(input("Enter the value that you want to add please "))
                temp = Node(data)
                nx = p.next
                temp.next = nx
                p.next = temp 
                print(p.info)
                return
            p=p.next
            
        
    def delete_firstnode(self):
        
        rm = p = self.last
        rm = rm.next
        nx = p.next.next
        rm.next = None
        p.next = nx

        
    def delete_lastnode(self):
        
        p = pr = self.last
        fr = self.last.next
        while pr.next != p:
            pr = pr.next
        pr.next = fr
        self.last = pr
        
      
        
    def delete_anynode(self,value):
        
        if self.last.info == value:
            self.delete_lastnode()
            return
        
        if self.last.next.info == value:
            self.delete_firstnode()
            return
         
        else:
            p = self.last.next
            while p != self.last:
                if p.info == value:
                    nx = p.next
                    prev.next = nx
                    return
                prev = p    
                p=p.next
                
    def concatenate_twolists(self,sec_list):
        
        fr_one = self.last.next
        print(fr_one.info)  #1
        
        fr_sec = sec_list.last.next
        print(fr_sec.info) #5
        
        self.last.next = fr_sec 
        self.last = sec_list.last
        self.last.next = fr_one
             
       
        
                
################################################################
                
list = CircularLinkedList()
list.create_list()
            
while True:
    print()
    print("1- Display List")
    print("2- Insert in empty list")
    print("3- Insert in the beginning of the list")
    print("4- Insert a node in the end of the list")
    print("5- Insert a node after a specified value")
    print("6- Delete first node")
    print("7- Delete last node")
    print("8- Delete Any node")
    print("9- Concatenate two circular lists")
    print("10- Quit")

    option = int(input("Enter your choice please : "))
        
    if option == 1:
        list.display_list()
    if option == 2:
        data = int(input("Enter the value that you want to add please "))
        list.insert_emptylist(data)
    if option == 3:
        data = int(input("Enter the value that you want to add please "))
        list.insert_beginning(data)
    if option == 4:
        data = int(input("Enter the value that you want to add please "))
        list.insert_endlist(data)
    if option == 5:
        value = int(input("Enter a position please "))
        list.insert_after(value)
    if option == 6:
        list.delete_firstnode()
    if option == 7:
        list.delete_lastnode()
    if option == 8:
        value = int(input("Enter a position please "))
        list.delete_anynode(value)
    if option == 9:
        sec_list = CircularLinkedList()
        sec_list.create_list()
        list.concatenate_twolists(sec_list)
    if option == 10:
        break
        
        
        
        