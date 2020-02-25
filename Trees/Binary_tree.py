#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:21:05 2019

@author: mdrahali
"""

from collections import deque

class Node(object):
    
    def __init__(self,value):
        self.info = value
        self.right = None
        self.left = None
        
class Binarytree(object):
    
    def __init__(self):
        self.root = None
        
    def create_tree(self):
        
        self.root = Node('P')
        self.root.left = Node('Q')
        self.root.right = Node('R')
        
        self.root.left.left = Node('A')
        self.root.left.right = Node('B')
        
        self.root.right.right = Node('X')
        
    def display(self):
        self._display(self.root,0)
    
    def _display(self,p,level):
        
        if p is None:
            return
        
        self._display(p.left, level + 1)
        
        for i in range(level):
            print("     ",end='')
        print(p.info)
        self._display(p.right, level + 1)
        
        
    def preorder(self):
        self._preorder(self.root)
    
    def _preorder(self,p):
        
        if p is not None:
            print(p.info + " kayna")
            self._preorder(p.left)
            self._preorder(p.right)
        
    def inorder(self):
        self._inorder(self.root)
    
    def _inorder(self,p):    
        
        if p is not None:
            self._inorder(p.left)
            print(p.info + " ")
            self._inorder(p.right)
        
    def postorder(self):
        self._postorder(self.root)
    
    def _postorder(self,p):    
        if p is not None:
            self._postorder(p.left)
            self._postorder(p.right)
            print(p.info + " ")
            
    
    def level_order(self):
        p = self.root
        if p is None:
            return
        
        qu = deque()
        qu.append(p)
        
        while len(qu) != 0:
            p = qu.popleft()
            print(p.info + " ",end='')
            if p.left is not None:
                qu.append(p.left)
            if p.right is not None:
                qu.append(p.right)
                
# with preorder and inorder i could make a Tree
    
    def construct_tree(self,preOrder,inOrder,in_st,in_end):
        
        if in_st > in_end:
            return None
        
        node_tree = Node(preOrder[self.index])
        self.index+=1
        print(bt.index)
        if in_st == in_end:
            return node_tree
        
        print(node_tree.info)
        index_len = self.search(inOrder,in_st,in_end,node_tree.info)
        print(index_len,"index", in_st,in_end)
        self.root.left = self.construct_tree(preOrder,inOrder,in_st,index_len-1)
        self.root.right = self.construct_tree(preOrder,inOrder,index_len+1,in_end)
        
        return node_tree
  
       
    def search(self,list_ino,in_st,in_end,x):        
        for i in range(in_st,in_end+1):
            if x == list_ino[i]: 
                return i
            
    
    def height(self):
        return self._height(self.root)
    
    def _height(self,p):
        
        if p is None:
            return 0
        
        hl = self._height(p.left)
        hr = self._height(p.right)
        
        if hl > hr:
            return 1 + hl 
        else:
            return 1 + hr
        
######################################################

if __name__ == "__main__":
    
    bt = Binarytree()
#    bt.create_tree()
#    
#    
#    
#    print("Display - Preorder")
#    bt.preorder()
#    print()
#    
#    print("Display - Inorder")
#    bt.inorder()
#    print()
#    
#    print("Display - Postorder")
#    bt.postorder()
#    print()
#    
#    print("Display")
#    bt.display()
#    print()
#    
#    print("Display - Level order")   
#    bt.level_order()
#    print()
#     
#    print("Height of this Tree is :")
#    print(bt.height())
#    
    ##################################
    bt.index = 0 # Index to travers preorder array
    
    inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] 
    n = len(inOrder)
    bt.root = bt.construct_tree(preOrder,inOrder,0,n-1)
    
    print("Print Tree constructed from inOrder, and preorder display \n \n")
    print(inOrder)
    print(preOrder,end='\n \n')
    bt.display()
    
    
    
    
    
    
    
    
    
    