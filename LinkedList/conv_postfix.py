#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:19:38 2019

@author: mdrahali
"""

from StackArray import Stack

def infix_postfix(expr):
    ch = expr
    stack = Stack()
    postfix = ''
    for ch in expr:
        if type_ch(ch) == 4 :
            postfix+=ch
        if type_ch(ch) == 2 :
            stack.push(ch)
        if type_ch(ch) == 3 :
            v = stack.pop()
            while v != '(':
                postfix+=v
                v = stack.pop()
        if type_ch(ch) == 1:
            if stack.isEmpty():
                stack.push(ch)
            else:
                v = stack.pop()
                x =0
                if  priority_operator(ch) > priority_operator(v):
                    stack.push(v)
                    stack.push(ch)
                else:
                    stack.display()
                    while priority_operator(ch) <= priority_operator(v) and not stack.isEmpty():
                        postfix+=v
                        v = stack.pop()
                    if priority_operator(ch) <= priority_operator(v) and  stack.isEmpty():
                        postfix+=v   
                        x = 1
                    if x == 0:                
                        stack.push(v)
                        stack.push(ch)
                    else:
                        stack.push(ch)
    
    if not stack.isEmpty():
        while not stack.isEmpty():
            v = stack.pop()
            postfix+=v
    return postfix
        
            
def priority_operator(val):
    
    if val == '(':
        return 0
    if val in '+-':
        return 1
    if val in '*/':
        return 2
    if val == 'ˆ':
        return 3
    
            
            
def type_ch(ch):
    
    if ch in '+/-*ˆ':
        return 1
    else:
        if ch in '()':
            if ch == '(':
                return 2
            if ch == ')':
                return 3
    return 4


def evaluation(postfix):
    
    stack = Stack()
    
    for symbol in postfix:
        if symbol.isdigit():
            
            stack.display()
            stack.push(int(symbol))
        else:
            x = stack.pop()
            y = stack.pop()
            
            if symbol == '+':
                stack.push(y+x)
            if symbol == '-':
                stack.push(y-x)
            if symbol == '*':
                stack.push(y*x)
            if symbol == '/':
                stack.push(y/x)
            if symbol == 'ˆ':
                stack.push(y**x)
            
    return stack.pop()
        
    
        
    


###############################################################################
    
if __name__ == "__main__":
    
    print("Enter an arithmetic expression please ")
    expr = input()
    postfix = infix_postfix(expr)
    print(postfix)
    print(evaluation(postfix))
















