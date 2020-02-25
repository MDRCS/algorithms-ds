#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:45:44 2019

@author: mdrahali
"""

from StackArray import Stack

def isValid(expr):
    st = Stack()
    
    for ch in expr:
        if ch in '({[':
            st.push(ch)
        if ch in ']})':
            if st.isEmpty():
                print("Right parentheses are more that left ones")
                return False
            else:
                char = st.pop()
                if not match_parenthese(char,ch):
                    print("Mismatched parentheses")
                    return False
    
    if st.isEmpty():
        print("Balanced parentheses ")
        return True
    else:
        print("Left parentheses are more that right ones")
        return True
                    
                     
def match_parenthese(leftPar,rightPar):
    
    if leftPar == '(' and rightPar == ')':
        return True
    if leftPar == '{' and rightPar == '}':
        return True
    if leftPar == '[' and rightPar == ']':
        return True
    return False

######################################################################
    
if __name__ == "__main__":
    
    while True:
        
        print("Enter an expression (or q to quit) ")
        expr = input()
        
        if expr == 'q':
            break
        
        if isValid(expr):
            print("Valid expression")
        else:
            print("Invalid expression")
        
        