#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 01:10:31 2019

@author: mdrahali
"""
      
from collections import deque
  
def selection_sort(ls):
    
    n = len(ls)
    
    for i in range(n):
        j = min_fnc(ls,i,n)
        ls[i],ls[j] = ls[j],ls[i]
    
    
    
def min_fnc(ls,start,end):
    minn = start
    for i in range(start+1,end):
        if ls[i] < ls[minn]:
            minn = i
    return minn
    

def bubble_sort(ls):
    for i in range(len(ls)-1,0,-1):
        for j in range(i):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]

#we can modifie the solution to not do all n-1 iterations because not all arrays need n-1 iterations to be sorted
                
def bubble_sort_optim(ls):
    for i in range(len(ls)-1,0,-1):
        swap = 0
        for j in range(i):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
                swap+=1
        if swap == 0:
            print(i)
            break


def insertion_sort(ls,step,start):
    
    n = len(ls)
    
    for i in range(start,n,step):
        for j in range(i,0,-step):
            if ls[j] < ls[j-step]:
                ls[j],ls[j-step] = ls[j-step],ls[j]  
        


def shell_sort(ls):
    steps = [5,3,1]
    n = len(steps)
    for step in range(n):
        for start in range(steps[step]):  
            insertion_sorting(ls,steps[step],start)
            #print(ls,"start :",start)
    

def merge_sorted_twolist(ls,lss):
    n = len(ls)
    m = len(lss)
    lsss = []
    i = j = 0
    while i < n and j<m :
        if ls[i]< lss[j]:
            lsss.append(ls[i])
            i+=1
        else:
            lsss.append(lss[j])
            j+=1
    
    if i>=n:
        #print("here 1",lsss)
        start = j
        for j in range(start,m):
            lsss.append(lss[j])
    elif j>= m:
        #print("here 2",lsss)
        start = i
        for i in range(start,n):
            lsss.append(ls[i])
    return lsss
        
       
            
                
def quick_sort(ls,low,high):
    
    if low < high:
        
        p = partionning(ls,low,high)
        quick_sort(ls,low,p-1)
        quick_sort(ls,p+1,high)


def partionning(ls,low,high):
    
    pivot = ls[high]
    i = low - 1
    
    for j in range(low,high):
        if ls[j] < pivot:
            i+=1
            ls[i],ls[j] = ls[j],ls[i]
    
    ls[i+1],ls[high] = ls[high],ls[i+1]
    
    return (i+1)
            
        
        
# exp is variable to get part that we want from a number (units,decimal,hundreds)
def counting_sort(arr,exp):
    
    n = len(arr)
    
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = int(arr[i] / exp)
        count[(index) % 10]+=1
        
    for i in range(1,10):
        count[i]+=count[i-1]
        
    i = n-1
    while i >= 0 :
        index = int(arr[i] / exp)
        output[count[(index) % 10]-1] = arr[i]
        count[(index) % 10]-=1
        i-=1
    
    i = 0
    for i in range(n):
        arr[i] = output[i]
        
        
def radix_sort(arr):
    
    max1 = max(arr)
    
# exp is variable to get part that we want from a number (units,decimal,hundreds)
    exp = 1
    
    while max1/exp > 0:
        counting_sort(arr,exp)
        exp *= 10
    
    
        
    


#in this version i tried to minimize number of movement by sorting sublists with diffrent steps 
#using the same sort algorithm = insertion sort
            
#def shell_sorting(ls):
#    #steps = [5,3,1]
#    #n = len(steps)
#    step = int(len(ls)/2)
#    while step>0:
#        for start in range(step):  
#            insertion_sorting(ls,step,start)
#            print(ls,"start :",start)
#        step = int(step/2)




ls = [21,60,2,7,8,11,1,19,9,4,48,3,5,17,16,13,59]
#lss = [1,4,6,9,10,30]
#bubble_sort(ls)
#bubble_sort_optim(ls)
#shell_sort(ls)
print(ls)
#print(lss)
#quick_sort(ls,0,len(ls)-1)
radix_sort(ls)
print(ls)
#lsss = merge_sorted_twolist(ls,lss)
#print("length :",len(lsss))
#insertion_sort(ls,1,0)
#selection_sort(ls)
#print(lsss)