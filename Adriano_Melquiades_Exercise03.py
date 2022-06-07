# -*- coding: utf-8 -*-
"""
Created on Wed May 25 10:49:09 2022

@author: apmel

name: Adriano Melquiades
student number: 301155357
"""



# Class to define node of the linked list    
class Node: 
    def __init__(self,data):    
        self.data = data;
        self.next_node = None;
    
    def __repr__(self):
        return str(self.data)
          
class CircularLinkedList:
      
    # Declaring Circular Linked List
    def __init__(self):    
        self.head = Node(None)    
        self.tail = Node(None) 
        self.head.next_node = self.tail 
        self.tail.next_node = self.head
          
      
    # Adds new nodes at the end of the Circular Linked List
    def add(self,data):    
          
        # Declares a new node to be added
        newNode = Node(data)
          
        # Checks if the Circular
        # Linked List is empty
        if self.head.data is None:
              
            # If list is empty then new node
            # will be the first node
            # to be added in the Circular Linked List
            self.head = newNode
            self.tail = newNode
            newNode.next_node = self.head
          
        else:
            # If a node is already present then
            # tail of the last node will point to
            # new node
            self.tail.next_node = newNode
              
            # New node will become new tail
            self.tail = newNode
              
            # New Tail will point to the head
            self.tail.next_node = self.head    
                  
    # Function to search the element in the 
    # Circular Linked List
    def findNode(self,element):
          
        # Pointing the head to start the search
        current = self.head
        i = 1;
          
        # Declaring f = 0
        f = 0;    
        # Check if the list is empty or not    
        if(self.head == None):
            print("Empty list") 
        else:
            while(True):     
                # Comparing the elements
                # of each node to the
                # element to be searched
                if(current.data ==  element): 
  
                    # If the element is present
                    # then incrementing f
                    f += 1;    
                    break;
                  
                # Jumping to next node
                current = current.next_node    
                i = i + 1;    
                  
                # If we reach the head
                # again then element is not 
                # present in the list so 
                # we will break the loop
                if(current == self.head):    
                    break;    
              
            # Checking the value of f
            if(f > 0):    
                print("element is present");    
            else:    
                print("element is not present")   
    
    def display(self):   
        provisory_node = self.head
        if self.head is not None:
            while (True):
                print(provisory_node)
                provisory_node = provisory_node.next_node
                if (provisory_node == self.head):
                    break

    def cloneCircularyList(self):        
        if self.head.data is None and self.tail.data is None:
            print('Empty list')
            return 
              
        clone_list = CircularLinkedList()
        provisory_node = self.head
        
        while (provisory_node.next_node != self.head):
            clone_list.add(provisory_node)
            provisory_node = provisory_node.next_node
        
        #Adding the tail
        clone_list.add(provisory_node)
            
        return clone_list

                  
# Driver Code
if __name__ == '__main__':
      
    # Creating a Circular Linked List
    list1 = CircularLinkedList();
      
    #Adding nodes to the list    
    list1.add(1);
    list1.add(2);
    list1.add(3);
    list1.add('Adriano')

    
    print('Printing l1:')
    list1.display()
      
    clone = list1.cloneCircularyList()

    print('Now printing the clone list:')
          
    clone.display()

