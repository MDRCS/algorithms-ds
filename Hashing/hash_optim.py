#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:36:47 2019

@author: mdrahali
"""

class student(object):
    
    def __init__(self,key,name):
        self.studentId = key
        self.studentName = name
    
    def getStudentId(self):
        return self.studentId
    
    def setStudentId(self,key):
        self.studentId = key

    def __str__(self):
        return str(self.studentId) + " - " + self.studentName

class Node(object):
    
    def __init__(self,student):
        self.student = student
        self.next = None

class SingleLinkedList:
    
    def __init__(self):
        self.start = None
        
    def create_list(self,n):

        for i in range(n):
            
            key = int(input("Please enter the student's ID "))
            name = input("Please enter the student's name ")
            std = student(key,name)
            self.insertion_endlist(std)
            
    def display_list(self):
        if self.start is None:
            print("_____")
            return
        else:
            p=self.start
            
            while p is not None:
                print("[",end=' ') ; print(p.student,end=' '); print("]",end=' ') ;
                print(" -> ",end=' ') ;
                p=p.next
            print("None");
    
    def count_nodes(self):
        p=self.start
        n=0
        
        while p is not None:
            n+=1
            p=p.next
        
        print("The number of nodes in this List is ",n)
        
        
    def search(self,x):
        p=self.start
        position = 1
        
        while p is not None:
            if p.student.getStudentId() == x:
                print("the position of ",x," is ", position)
                return True
            position+=1
            p=p.next
        else:
            print(x," does not exist in this List")
            return False
        

    def insertion_beginning(self,x):
        
        temp = Node(x)
        temp.next = self.start
        self.start = temp
        
    def insertion_empty_list(self,x):
        self.start = Node(x)
        
    def insertion_endlist(self,x):
        temp = Node(x)
        
        if self.start is None:
            self.start = temp
            return 
        
        p = self.start
        while p.next is not None:
            p=p.next
        p.next = temp

    def delete_firstnode(self):
        
        if self.start is None:
            return
        
        if self.start.next is None:
            self.start = None

        self.start = self.start.next
        
    
    def delete_node_between(self,x):
    
        if self.start is None:
            return
        
        if self.start.next is None:
            self.start = None
            self.start = self.start.next
            return
        
        p = self.start
        pos = 1
        prec = p
        while p.next is not None:
            if p.student.getStudentId() == x:
                prec.next = p.next
            pos+=1
            prec = p
            p=p.next
            
    def delete_endlist(self):
        
        if self.start is None:
            return
        
        p = self.start
        while p.next.next is not None:
            p=p.next
            
        p.next = None
                
        
        
class hashtable(object):
    
    def __init__(self,size=5):
        self.size = size  
        self.array = [None] * self.size 
        
    def display(self):
        
        n = self.size
        
        for i in range(n):
            print("[",end='') ; print(i,end=''); print("]",end='') ;
            print(" -> ",end=' ')
            if self.array[i] != None:
                self.array[i].display_list()
            else:
                print("___")
    
    def hashing(self,key):
        return (key % self.size)
    
    def insert(self,student):
        
        index = self.hashing(student.getStudentId())
        if self.array[index] == None:
            self.array[index] = SingleLinkedList()
            self.array[index].insertion_beginning(student)
            return
        self.array[index].insertion_endlist(student)

    def delete(self,key):
        
        index = self.hashing(key)

        if self.array[index] is not None:
            #self.array[index].delete_firstnode()
            self.array[index].delete_endlist()
            #self.array[index].delete_node_between(key)
      
    
    def search(self,key):
        
        hs = self.hashing(key)
        index = hs

        if self.array[index] is not None:
            self.array[index].search(key)

            
        
###############################################################################################

if __name__ == "__main__":

    ht = hashtable()

    
    while True:
        print("- Menu-")
        print("1- Display")
        print("2- Insert a record")
        print("3- Delete a record")
        print("4- Search for record")
        print("5- Quit")
        
        option = int(input("Please enter a choice !! "))
        
        if option == 1:
            ht.display()
        if option == 2:
            key = int(input("Please enter the student's ID "))
            name = input("Please enter the student's name ")
            std = student(key,name)
            ht.insert(std)
        if option == 3:
            ht.display()
            key = int(input("Please enter the student's ID that you want to delete "))
            ht.delete(key)
        if option == 4:
            key = int(input("Please enter the student's ID that you want to search for "))
            std = ht.search(key)
            print(std)
        if option == 5:
            break

        
        
