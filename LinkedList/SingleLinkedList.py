#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 16:54:02 2019

@author: mdrahali
"""

class Node:
    
    def __init__(self,value):
        self.info = value
        self.next = None

class SingleLinkedList:
    
    def __init__(self):
        self.start = None
        
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is ")
            p=self.start
            
            while p is not None:
                print(p.info," ",end='')
                p=p.next
            print()
    
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
            if p.info == x:
                print("the position of ",x," is ", position)
                return True
            position+=1
            p=p.next
        else:
            print(x," does not exist in this List")
            return False
        
    def create_list(self,n):
        
        if n == 0:
            return
        
        for i in range(n):
            data = int(input(" Enter the value of the node : "))
            self.insertion_endlist(data)
            #p=self.start
            #while p.next is not None:
            #    p=p.next
            #p.next = Node(data)
        
            
    def last_node(self):
        
        if self.start is None:
            return
        else:
            p = self.start
            while p.next is not None:
                p = p.next
            print(p.info)
        
    def second_lastnode(self):
        
        if self.start is None:
            return 
        else:
            p = self.start
            while p.next.next is not none: # if we have just one node this algorithm won't work
                p = p.next
            print(p.info)
    
    def find_node(self,x):
        p=self.start
        
        while p.next is not None:
            if p.info == x:
                return True
            p = p.next
        else:
            return False 
        
    def second_given_node(self,x):
        p=self.start
        while p.next is not None:
            if p.next.info == x:
                return True
            p = p.next
        else:
            return False 
        
    
    def find_node_position(self,pos):
        position = 1
        p=self.start
        
        while position < pos and p.next is not None:
            p = p.next
            position+=1
            
            return p
        else:
            return None
        
    
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
        
        
    def insert_after(self,x):
        
        if  self.start is None:
            return
        
        p = self.start
        while p.next is not None:
            if p.info == x:
                temp = p.next
                data = int(input(" Enter the value of the node :"))
                new = Node(data)
                new.next = temp
                p.next = new
            p = p.next
                
    
    def insert_pos(self,x):
        
        if self.start is None:
            return
        
        p = self.start
        position = 1
        
        while p.next is not None and position+1 != x:
            position+=1
            p=p.next
        
        if p.next is not None and position+1 == x:
            p= p.next
            s = p.next
            data = int(input("Enter a value to be insert :"))
            temp = Node(data)
            temp.next = p.next
            p.next = temp
        else:
            print(" you can't insert in this position")
            return
 
        
    def delete_firstnode(self):
        
        if self.start is None:
            return
        
        if self.start.next is None:
            self.start = None

        self.start = self.start.next
        
    
    def delete_node_between(self,x):
    
        if self.start is None:
            return
        
        p = self.start
        pos = 1
        prec = p
        while p.next is not None:
            if p.info == x:
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
        
    
    def reverse_list(self):
        
        if self.start is None:
            return
        
        prev = None
        p = self.start
        
        while p is not None:
            next = p.next
            p.next = prev
            prev = p
            p = next 
        self.start = prev
        
    def bubble_sorting_exdata(self):
        
        p = self.start
        q = p.next
        end = None

        while end != self.start.next:
            p = self.start
            q = p.next
            
            while q != end:
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p=q
                q=q.next
            end = p
            
    def bubble_sorting_exlinks(self):
        
        end = None
        
        while end != self.start.next:
            r = p = self.start
            while p.next != end:
                q=p.next
                if p.info > q.info:
                    p.next = q.next
                    q.next = p
                    if p != self.start:
                        r.next = q
                    else:
                        self.start = q
                    p,q = q,p #we used two ponters p was first and q second but after the permutation we exchanged them so we should get them back as they had 
                r=p
                p=p.next
            end = q
        
    def merge_sorted_list(self,list_1,list_2):
        
        p = list_1.start
        pr = list_2.start
        new_list = SingleLinkedList()        
        while p is not None and pr is not None:
            if p.info <= pr.info:
                new_list.insertion_endlist(p.info)
                new_list.insertion_endlist(pr.info)
            else:
                 new_list.insertion_endlist(pr.info)
                 new_list.insertion_endlist(p.info)
            p=p.next
            pr=pr.next
        else:
            if p is None:
                while pr is not None:
                    new_list.insertion_endlist(pr.info)
                    pr=pr.next
            else:
                while p is not None:
                    new_list.insertion_endlist(p.info)
                    p=p.next
        
        return new_list

    def merge_sorted_list_ref(self,list_2):
        
        p = self.start
        pr = list_2.start
        if p.info <= pr.info:
            start = p
            p=p.next
        else:
            start = pr
            pr=pr.next
            
        pm = start
        
        while p is not None and pr is not None:
            if p.info <= pr.info:
                pm.next = p
                pm = pm.next
                p=p.next
            else:
                pm.next = pr
                pm = pm.next
                pr=pr.next

        else:
            if p is None:
                pm.next = pr
            else:
                p=p.next
        
        self.start = start
        return start
    
#    def merge_sort(self):
#        self.start = self.merge_sort_rec(self.start)
#    
#    def merge_sort_rec(self,list_start):
#        
#        if list_start is None and list_start.next is None:
#            return list_start
#        
#        start_1 = list_start
#        start_2 = self.dividing_list(list_start)
#        start_1 = self.merge_sort_rec(start_1)
#        start_2 = self.merge_sort_rec(start_2)
#        start_m = self.merge_sorted_list(start_1,start_2)
#        return start_m
#    
#    def dividing_list(self,p):
#        q = p.next.next
#        while q is not None and q.next is not None:
#            p=p.next
#            q=q.next.next
#        
#        start2 = p.next
#        p.next = None
#        return start2
                    
    def detecting_cyclic_list(self):
        if self.start is None or self.start.next is None:
            return None
        
        h = self.start
        t = self.start
        
        while h is not None:
            t=t.next
            h=h.next.next
            if t==h:
                print("the list is cyclic")
                return t
        print("the list is not cyclic")
        return None
             
    def create_cyclic_list(self,n):
        #this part just for creating cyclic linkedlist
        c=n/2
        p = self.start
        s=None
        
        while p.next is not None:
            if c == 0:
                s = p
            c-=1
            p=p.next
        p.next = s

    def remove_cycle(self):
        
        c = self.detecting_cyclic_list()
        
        if c is None:
            return
        
        len_cycle = 1
        p = q = c
        q=q.next
        while p != q:
            len_cycle+=1
            q=q.next 
        p = self.start
        
        len_remlist = 0
        while p!= q:
            q=q.next
            p=p.next
            len_remlist+=1
        list_length = len_remlist + len_cycle
        print(list_length)
        p = self.start
        
        while list_length > 1:
            list_length-=1
            p=p.next
        p.next = None
        
    def Concatenate_twolists(self,sec_list):
        
        p = self.start 
        
        while p.next is not None:
            p=p.next
            
        p.next = sec_list.start
        
    def insert_sortedlist(self,value):
        temp = Node(value)
        if self.start is not None :
            per=self.start
            self.start = temp 
            self.start.next = per
            return
            
        p = self.start
        
        while p.next is not None and p.next.info <= value:
            p=p.next
        else:
            nx = p.next
            temp.next = nx
            p.next = temp
            


      
#######################################################################
    
if __name__ == "__main__" :
    
    list = SingleLinkedList()
    #list_2 = SingleLinkedList()
    #list_3 = SingleLinkedList()
    n= int(input(" Enter the number of nodes to create : "))
    list.create_list(n)
    #list.create_cyclic_list(n)
    
    #list_2.create_list()
    
    
    while True:
        print("1- Display a List")
        print("2- Count nodes")
        print("3- Search")
        print("4- Insert in the beginning")  
        print("5- Insert after a value")
        print("6- Insert in a position")    
        print("7- Delete in the beginning of the list")    
        print("8- Delete in a given position")    
        print("9- Delete in the end of the list")  
        print("10- Reverse a linked list")  
        print("11- Bubble Sorting")  
        print("12- Merge two sorted lists")  
        print("13- Merge sort of a linkedlist")  
        print("14- Detecting cyclic list")  
        print("15- Removing cycle")
        print("16- Concatenate two lists")
        print("17- Insert Sorted list")
        print("18- Quit")
        
        option = int(input("Enter your choice : "))
    
        if option == 1:
            list.display_list()
        if option == 2:
            list.count_nodes()
        if option == 3:
            data = int(input("Enter the number that you search for :"))
            list.search(data)
        if option == 4:
            data = int(input("Enter the value to be insered in the beginning :"))
            list.insertion_beginning(data)
        if option == 5:
            data = int(input("Enter the value that you want to insert after :"))
            list.insert_after(data)
        if option == 6:
            data = int(input("Enter a position :"))
            list.insert_pos(data)
        if option == 7:
            list.delete_firstnode()
        if option == 8:
            data = int(input("Enter a position :"))
            list.delete_node_between(data)
        if option == 9:
            list.delete_endlist()
        if option == 10:
            list.reverse_list()
        if option == 11:
            #list.bubble_sorting_exdata()
            list.bubble_sorting_exlinks()
        if option == 12:
            #list_3 = list.merge_sorted_list(list_2)
            list.merge_sorted_list_ref(list,list_2)
            list.display_list()
        if option == 13:
            list.merge_sort() 
        if option == 14:
            list.detecting_cyclic_list()
        if option == 15:
            list.remove_cycle()
        if option == 16:
            list_2 = SingleLinkedList()
            n= int(input(" Enter the number of nodes to create for the second list : "))
            list_2.create_list(n)
            list.Concatenate_twolists(list_2)
        if option == 17:
            list.bubble_sorting_exdata()
            data = int(input("Enter the value to be insered :"))
            list.insert_sortedlist(data)
        if option == 18:
            break
        