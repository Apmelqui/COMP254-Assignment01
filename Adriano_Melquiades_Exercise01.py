# -*- coding: utf-8 -*-
"""
Created on Wed May 18 07:25:11 2022

@author: apmel

name: Adriano Melquiades
student number: 301155357
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
    def __repr__(self):
        return str(self.data)

class SinglyLinkedList:
    
    #Creating the first node, which will be the reference for all the others nodes
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0       
        
    #return the size of the list
    def size_of_the_list(self):
        return self.num_of_nodes        
    
    def addFirst(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)
        
        #If the data structure is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def addLast(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)
        
        #Cheking if the list is empty
        if self.head is None:
            self.head = new_node
        else:
            #When the list is not empty
            provisory_node = self.head
            
            while provisory_node.next_node is not None:
                provisory_node = provisory_node.next_node
                
            #reaching the end of the list and inserting the new_node
            provisory_node.next_node = new_node
    
    def display(self):
        provisory_node = self.head
        while provisory_node is not None:
            print(provisory_node)
            provisory_node = provisory_node.next_node

    def remove_node(self, data):
        #If the list is empty, nothing is done
        if self.head is None:
            return
        
        #Keeping track of the previous node
        provisory_node = self.head
        previous_node = None
        
        #Seraching for the data to be removed
        while provisory_node is not None and provisory_node.data != data:
            previous_node = provisory_node
            provisory_node = provisory_node.next_node
            
        #not found?
        if provisory_node is None:
            return
        
        #Updating the reference so we have the data to be removed - ps the head is the one to be removed
        if previous_node is None:
            self.head = provisory_node.next_node
        else:
            #Updating the pointer - no need to remove the node 
            previous_node.next_node = provisory_node.next_node  
    
    def copy_list(self):
        
        ###
        if self.head is None:
            return
        ###
        
        result = SinglyLinkedList()
        prov = self.head
        
        while prov.next_node is not None:
            result.addLast(prov.data)
            prov = prov.next_node
        result.addLast(prov.data)
        return result
        
        ############ Exercise 01 code ##############
        
    def swap_two_nodes(self, n1, n2):
        
        #Empty list
        if self.head is None:
            return
    
        #Equal nodes        
        if (n1 == n2):
            return
        
        #Searching for n1 and keeping track of the previus and the current node
        previous_n1 = None
        current_n1 = self.head
        while current_n1 != None and current_n1.data != n1:
            previous_n1 = current_n1
            current_n1 = current_n1.next_node
            
        #Searching for n2 and keeping track of the previous and the current node
        previous_n2 = None
        current_n2 = self.head
        while current_n2 != None and current_n2.data != n2:
            previous_n2 = current_n2
            current_n2 = current_n2.next_node
            
        #If n1 or n2 is not found - return
        if current_n1 == None or current_n2 == None:
            return
        
        #If n1 is not the head of the list
        if previous_n1 != None:
            previous_n1.next_node = current_n2
        else:
            #make n2 the new head
            self.head = current_n2
            
        #If n2 is not the head of the list
        if previous_n2 != None:
            previous_n2.next_node = current_n1
        else:
            #make n1 the new head
            self.head = current_n1
            
        #Now swapping the next pointers
        temp = current_n1.next_node
        current_n1.next_node = current_n2.next_node
        current_n2.next_node = temp
        
        ############ Exercise 01 code ##############           
        
#Testing the code

if __name__ == '__main__':
    list = SinglyLinkedList()
    list.addFirst(1)
    list.addLast(3)
    list.addLast(2)
    list.addFirst(4)
    
    list.display()
    print('###########')
        
    list.addLast('Adriano')
    
    list.display()
    print('###########')    
    
    list.remove_node('Adriano')
    list.display()
    print('###########')    
       
    list.swap_two_nodes(4, 2)
    list.display()
    print('###########')  

    list.swap_two_nodes(2, 1)
    list.display()        
        
        
        
        
        
        

        
        
        
        
        
        
        