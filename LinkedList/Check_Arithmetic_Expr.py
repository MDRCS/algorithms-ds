#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:52:48 2019

@author: mdrahali
"""

# This program could calculate a long arithmetic expression check for who have the priority etc 
# Ex: 8*(1-9)*(3+4) , 7-1+3*9-1
# NB : but this one could not function with an expression like this 8-1+34-(3+5-2*8) because i don't check for the priority e
# inside the parenthese (it could be done with recurision )

from SingleLinkedList import SingleLinkedList

def arithmetic_expr(ls,expr):
    
    list_create(ls,expr)

    while ls.start.next is not None:
        p = priority_operation(ls)
        if p is not None and p.info == '(' :   
            link = p
            p = p.next
                
            while p.info != ')':
                fr = int(p.info) 
                p.info = '--'
                p = p.next
                op = p.info
                p.info = '--'
                p = p.next
                lst = int(p.info) 
                p.info = '--'
                p = p.next
                if op == '+':    
                    link.info = str(fr + lst) 
                if op == '*':    
                    link.info = str(fr * lst) 
                if op == '/':    
                    link.info = str(fr / lst)
                if op == '-':    
                    link.info = str(fr - lst) 
                if op == 'ˆ':    
                    link.info = str(fr ** lst) 
            p.info = '--'
            if p.next is None:
                link.next = None
            
            
        optimize_space(ls) 
        p = priority_operation(ls)
        if p is not None and p.next is not None and p.next.info == '*': 
            link = p
            fr  = int(p.info) 
            p.info = '--'
            p.next.info = '--'
            p = p.next.next
            lst = int(p.info) 
            p.info = '--'
            link.info = str(fr * lst)
            if p.next is None:
                link.next = None
        
        optimize_space(ls) 
        p = priority_operation(ls)  
        if p is not None and p.next is not None and p.next.info == '/': 
            link = p
            fr  = int(p.info) 
            p.info = '--'
            p.next.info = '--'
            p = p.next.next
            lst = int(p.info) 
            p.info = '--'
            link.info = str(fr / lst)
            if p.next is None:
                link.next = None
         

        optimize_space(ls) 
        p = priority_operation(ls) 
        if p is not None and p.next is not None and p.next.info == '+': 
            link = p
            fr  = int(p.info) 
            p.info = '--'
            p.next.info = '--'
            p = p.next.next
            lst = int(p.info) 
            p.info = '--'
            link.info = str(fr + lst)
        
        optimize_space(ls) 
        p = priority_operation(ls)
        if p is not None and p.next is not None and p.next.info == '-': 
            link = p
            fr  = int(p.info) 
            p.info = '--'
            p.next.info = '--'
            p = p.next.next
            lst = int(p.info) 
            p.info = '--'
            link.info = str(fr - lst)
            if p.next is None:
                link.next = None

        optimize_space(ls) 
 
def optimize_space(ls):
    p = ls.start
   
    while not catch_empty(ls):
        p = ls.start
        if p.info == '--':
           ls.delete_firstnode() 
        p = p.next
        while p is not None and p.next is not None:
            if p.info == '--':
                ls.delete_node_between('--')
            p = p.next
    
        if p is not None and p.info == '--':
            ls.delete_endlist()

        
    
def catch_empty(ls): 
    p  = ls.start
    
    while p is not None:
        if p.info == '--':
            return False
        p = p.next
    return True

def priority_operation(ls):
    p = ls.start
    prev = None
    while p is not None:
        if p.info == '(':
            return p
        p  = p.next
        
    p = ls.start
    prev = None
    while p is not None:    
        if p.info == '*' or p.info == '/' :
            return prev
        prev = p
        p  = p.next
            
    p = ls.start
    prev = None
    while p is not None:
        if p.info == '+' or p.info == '-' :
            return prev
 
        prev = p
        p  = p.next
        
    ls.start.next = None 
    return ls.start

def list_create(ls,expr):
        
        for char in expr:
            ls.insertion_endlist(char)
    
def display(ls):
    p = ls.start
    s = ''
    while p is not None:
        s+=p.info + " "
        p = p.next
    print("Result : ",s)
    
    
###########################################
        
if __name__ == "__main__":
    
    while True:
        
        print("Enter an expression (or click q to quit)  ")
        expr = input()
        
        if expr == 'q':
            break
        
        ls = SingleLinkedList()
        arithmetic_expr(ls,expr)
        
        display(ls)