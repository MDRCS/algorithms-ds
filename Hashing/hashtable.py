#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:16:59 2019

@author: mdrahali
"""

class StackOverFlowError(Exception):
    pass

class NotFoundError(Exception):
    pass

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
    
class hashtable(object):
    
    def __init__(self,size=11):
        self.size = size
        self.array = [None] * self.size
        self.count = 0
    
    def hashing(self,key):
        return (key % self.size)
    
    def rehashing(self,key):
        n  = self.size 

        for i in range(n-1,0,-1):
            if self.isPrime(i):
                return (i - (key%i))

    def isPrime(self,v):
        for x in range(2,v):
            if v % x == 0:
                return False
        return True
    
    def insert(self,student):
        
        if self.count >= self.size // 2:
            self.resizing()
            
        n = self.size
        hs = self.hashing(student.getStudentId())
        index = hs
        for i in range(n):
            if self.array[index] is None or self.array[index].getStudentId() == -1:
                self.array[index] = student
                self.count+=1
                return
            
            #index = (hs + i) % self.size  #Linear probing
            #index = (hs + i**2)% self.size #Quadratic probing
            index = (hs + i*self.rehashing(student.getStudentId())) % self.size #double hashing
        
        raise StackOverFlowError("There is no space to store the new record ..")
        
    def resizing (self):
        htable = hashtable(self.size*2)
        n = self.size
        for i in range(n):
            if self.array[i] is not None and self.array[i].getStudentId() != -1:
                htable.array[i] = self.array[i]
            
        self.array = htable.array
        self.size = htable.size
        
    def delete(self,key):
        
        n = self.size
        hs = self.hashing(key)
        index = hs
        
        for i in range(n):
            if self.array[index] is not None and self.array[index].getStudentId() != -1:
                temp = self.array[index]
                self.array[index].setStudentId(-1)
                self.count-=1
                return temp
            
            #index = (hs + i) % self.size  #Linear probing
            #index = (hs + i**2)% self.size #Quadratic probing
            index = (hs + i*self.rehashing(student.getStudentId())) % self.size #double hashing
        
        return None
    
    def search(self,key):
        
        n = self.size
        hs = self.hashing(key)
        index = hs
        
        for i in range(n):
            if self.array[index] is not None and self.array[index].getStudentId() != -1:
                return self.array[index]
            
            #index = (hs + i) % self.size  #Linear probing
            index = (hs + i**2)% self.size #Quadratic probing
            #index = (hs + i*self.rehashing(student.getStudentId())) % self.size #double hashing
        raise NotFoundError("Not Found Record ..")
        
    def display(self):
        n = self.size
        
        for i in range(n):
            print("[",end='') ; print(i,end='') ; print("]",end='') ;
            if self.array[i] is not None and self.array[i].getStudentId() != -1:
                print(self.array[i])
            else:
                print("___")
    
if __name__ == "__main__":
    
    ht = hashtable(10)
    for i in range(3):
        std = student(i,"Student "+str(i))
        ht.insert(std)
    
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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
