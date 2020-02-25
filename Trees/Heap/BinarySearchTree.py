#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:25:03 2019

@author: mdrahali
"""
class EmptyTreeError(Exception):
    pass

class Node(object):
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
        
    def create_bst(self,ls):
        
        
        self.root = Node(ls[0])
        for i in range(1,len(ls)):            
            self.insert(ls[i])
        
#        self.root = Node(40)
#        
#        self.root.left = Node(38)
#        self.root.right = Node(50)
#        
#        self.root.left.left = Node(36)
#        self.root.left.right = Node(39)
#        
#        self.root.right.right = Node(70)
#        self.root.right.left = Node(46)
        
    def isEmpty(self):
        return self.root == None
    
    def insert(self,x):
        
        p  = self.root
        
        if p is None:
            p = Node(x)
        
        while p is not None:
            if p.data > x:
                pre = p
                p = p.left
            elif p.data < x:
                pre = p 
                p = p.right
        
        if pre.data > x:
            pre.left = Node(x)
        elif pre.data < x:
            pre.right = Node(x)
            
        
    def delete(self,x):
        p = self.root
        
        if p.data == x:
            lt = self.root.left
            rt = self.root.right
            node = self.min_fnc(rt)
            #print(node.data,lt)
            
            self.root = rt
            node.left = lt
            
        else:
            while p is not None:
                if p.data > x:
                    pre = p
                    p = p.left
                elif p.data < x:
                    pre = p
                    p = p.right
                else:
                    if p.left is None and p.right is None:
                        if pre.data > x:
                            pre.left = None
                            p = None
                        else:
                            pre.right = None
                            p = None
                    elif p.left is not None and p.right is not None:
                            rm = p
                            p = p.left
                            p.right = rm.right
                            if pre.data > rm.data:
                                rm = None
                                pre.left = p
                            else:
                                rm = None
                                pre.right = p
                    elif p.left is None and p.right is not None:
                        if pre.data > rm.data:
                            pre.left = p.right
                            p = None
                        else:
                            pre.right = p.right
                            p = None
                    elif p.left is not None and p.right is None:
                        if pre.data > p.data:
                            pre.left = p.left
                            p = None
                        else:
                            pre.right = p.left
                            p = None
                        

    def search(self,x):
        p = self.root
        #self.inorder()
        while p is not None:  
            if p.data > x:
                p = p.left
            elif p.data < x:
                p = p.right
            else:
                return p 
        return None
        
    def min_fnc(self,link):
        p = link
        while p.left is not None:
            p = p.left
        return p

        
    def max_fnc(self):
        p = self.root 
        while p.right is not None:
            p = p.right
        return p
    
    def height(self):
        pl = pr = self.root
        hl = hr = 0
        if pr is None:
            return -1
        elif pr.right is None and pl.left is None:
            return 0
        else:
            while pr.right is not None or pl.left is not None:
                if pr.right is not None:
                    pr = pr.right
                    hr+=1
                elif pl.left is not None:
                    pl = pl.left
                    hl+=1
        if hl > hr:
            return hl
        else:
            return hr
                    
        
        
    def display(self):     
        self._display(self.root,0)
        
    def _display(self,p,level):
        
        if p is None:
            return
        
        self._display(p.right,level + 1)            
        for i in range(level):
            print("   ",end='')
        print(p.data)
        self._display(p.left,level + 1)
                    
        
    def inorder(self):
        self._inorder(self.root)
    
    def _inorder(self,p):    
        
        if p is not None:
            self._inorder(p.left)
            print(p.data, " ",end="")
            self._inorder(p.right)
           
            
    def dichotomic_search(self,x):
        
        
        
#########################################################
                
if __name__ == "__main__":
    
    bst = BinarySearchTree()
    ls = [21, 60, 2, 7, 8, 11, 1, 19, 9, 4, 48, 3, 5, 17, 16, 13, 59]
    bst.create_bst(ls)
    
    
    
    
#    bst.display()
#    print("Height : ",bst.height())
#    
#    p = bst.max_fnc()
#    print("max : ",p.data)
#     
#    p = bst.min_fnc(bst.root)
#    print("min : ",p.data)
#    
#    if bst.search(p.data):
#        print(p.data,"Exist in the tree ..")
    
    bst.display()
    print(end='\n \n')
    
    bst.inorder()
    print(end='\n \n')
    
    #bst.insert(2)
    #bst.insert(60)
    
    #bst.delete(2)
    #bst.display()
    
    #bst.delete(70)
    #st.display()
    
    #bst.delete(38)
    #bst.display()
    
    #bst.delete(21)
    #bst.display() 
        
             
        