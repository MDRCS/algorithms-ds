#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 02:52:49 2019

@author: mdrahali
"""

from BinarySearchTree import BinarySearchTree,Node


def heap_construct(ls,pr):

    n = len(ls)
    #print(n)
    for i in range(2,n):
        #print(i)
        #print("Parent - ",ls[int(i/2)],end='\n')
        #print("Node - ",ls[i],end='\n')
        rt = ls[int(i/2)]
        #print(rt,"rt")
        p = pr.search(rt)
        if i % 2 == 0:
            while p is not None:
                pre = p
                p = p.left
            if pre.data != ls[i]:
                pre.left = Node(ls[i])
                p = pre.left
            else:
                p = pre
        else:
            while p is not None:
                pre = p
                p = p.right
            if pre.data != ls[i]:
                pre.right = Node(ls[i])
                p = pre.right
            else:
                p = pre
        
        if 2*i > n-1:
            print("left child doesn't exist ..")
#            while p is not None:
#                pre = p
#                p = p.left
            #pre.left = None
            #p = pre
            #print(p.data,"data exist pas 1")
        else:
            #print(pre.data,"data a")
            x = pre.left
            #print(x.data,ls[(2*i)+1])
            if x is not None:  
                if x.data != ls[2*i]:
                    print("Left child - ",ls[2*i],end='\n')
                    while p is not None:
                        pre = p
                        p = p.left
                    pre.left = Node(ls[2*i])
                    p = pre
            else:
                    print("Left child - ",ls[2*i],end='\n')
                    while p is not None:
                        pre = p
                        p = p.left
                    pre.left = Node(ls[2*i])
                    p = pre
           
        
        if ((2*i) +1)  > n-1:
            print("Right child doesn't existe ..")
#            while p is not None:
#                pre = p
#                p = p.right
#            pre.right = None
            #p = pre
            #print(p.data,"data exist pas 2")
        else:
            #print(pre.data,"data")
            x = pre.right
            #print(ls[(2*i)+1])
            if x is not None: 
                if x.data != ls[(2*i)+1]: 
                    #print("Right child - ",ls[(2*i)+1],end='\n')
                    while p is not None:
                        pre = p
                        p = p.right
                    pre.right = Node(ls[(2*i)+1])
                    p = pre
            else:
                    #print("Right child - ",ls[(2*i)+1],end='\n')
                    while p is not None:
                        pre = p
                        p = p.right
                    pre.right = Node(ls[(2*i)+1])
                    p = pre


        
  
def insert_heap(ls,x):
    ls.append(x)
    n = len(ls)
    for i in range(n-1,1,-1):
        if x > ls[int(i/2)]:
            ls[i],ls[int(i/2)] = ls[int(i/2)],ls[i]
            i = i//2   
    #print(ls)

def search_index(ls,x):
    n = len(ls)
    
    for i in range(1,n):
        if ls[i] ==  x:
            return i
    

def delete_heap(ls,x):
    
    i = search_index(ls,x)
    n = len(ls)
    if i == 1: #remove the root node
        while (i*2) +1 < n-1:
            if ls[(i*2)+1] > ls[i*2]:
                ls[i],ls[(i*2)+1] = ls[(i*2)+1],ls[i]
                i = (i*2)+1
            else:
                ls[i],ls[i*2] = ls[i*2],ls[i]
                i = i*2
        if (i*2) +1 >= n-1 and i*2 <= n-1:
            ls[i],ls[i*2] = ls[i*2],ls[i]
        ls[i] = None
            
    if i*2 +1 > n-1:
        if i*2 > n-1:
            ls[i] = None
        else:
            ls[i],ls[i*2] = ls[i*2],ls[i]
            ls[i*2] = None
    else:
        
        if ls[(i*2)+1] > ls[i*2]:
            ls[i],ls[(i*2)+1] = ls[(i*2)+1],ls[i]
            ls[(i*2)+1] = None
        else:
            ls[i],ls[i*2] = ls[i*2],ls[i]
            ls[i*2] = None
    
    
    
def heapify(ls):
    
    correct = False
    n = len(ls)
    while not correct:
        correct = True
        for i in range(n-1,1,-1):
            if ls[i]>ls[i//2]:
               ls[i],ls[i//2] = ls[i//2],ls[i]
               correct = False
        
        
#def heap_sorting(self,ls):    
    

ls_1 = [None,85,70,55,56,40,42,33,16,28,19,20,25] 
ls = [None,20,33,15,6,40,60,45,16,75,10,80,12] 

print("List one :",ls)
#print("List two :",ls_1)
#insert_heap(ls,80)
#insert_heap(ls_1,92)
#delete_heap(ls,85)
heapify(ls)
print("List one :",ls)

bst = BinarySearchTree()
bst.root = Node(ls[1])
heap_construct(ls,bst)
heapify(ls)
print(ls)
bst.delete(80)
heapify(ls)
print(ls)
bst.display()