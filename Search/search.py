#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:57:37 2019

@author: mdrahali
"""

def search(arr,x):
    
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

#start = 0, end= len(arr)-1
def dichotomic_search(arr,x):
    
    last = len(arr)-1
    first = 0
    
    while first<=last:
        mid = int((last+first)/2)
        if arr[mid] > x:
            last = mid - 1
        elif arr[mid] < x:
            first = mid + 1
        elif arr[mid] == x:
            return mid
    
    return -1
            
    
    
    

    
    
    
    

if __name__ == "__main__":
    
    ls = [13,26,29,1,3,22,95,47]
    ls_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 16, 17, 19, 21, 48, 59, 60] #
    
    index = dichotomic_search(ls_sorted,11)
    #search(ls,26)
    
    if index == -1:
        print("The value that you entred doesn't exist in this array ..")
    else:
        print(ls_sorted[index],"found in the index ",index)