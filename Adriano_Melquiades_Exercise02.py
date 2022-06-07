# -*- coding: utf-8 -*-
"""
Created on Wed May 18 07:25:11 2022

@author: apmel

name: Adriano Melquiades
student number: 301155357
"""
    
from Adriano_Melquiades_Exercise01 import SinglyLinkedList

    ################# Exercise 02 code #################
def concatenate(l1, l2):
    concat_list = SinglyLinkedList()    
    
    if l1.head is None and l2.head is None:
        print('Empty lists')
        return
    
    elif l1.head is None and l2.head is not None:
        concat_list = l2.copy_list()
        
    elif l2.head is None and l1.head is not None:
        concat_list = l1.copy_list()
        
    else:
        concat_list = l1.copy_list()
        provisory_node = concat_list.head
        while provisory_node.next_node is not None:
            provisory_node = provisory_node.next_node
        provisory_node.next_node = l2.head
    
    concat_list.display()    
    
    ################# Exercise 02 code #################

        
#Testing the code

if __name__ == '__main__':
    list1 = SinglyLinkedList()
    list1.addFirst(1)
    list1.addLast(3)
    list1.addLast(2)
    list1.addFirst(4)
    
    list1.display()
    print('###########')
        
    list1.addLast('apm')
    
    list1.display()
    print('###########')    
    
    list1.remove_node('apm')
    list1.display()
    print('###########')    
       
    list1.swap_two_nodes(4, 2)
    list1.display()
    print('###########')  

    list1.swap_two_nodes(2, 1)
    list1.display()        
        
    print("exercise02:")
    
    list2 = SinglyLinkedList()
    list2.addFirst("Adriano")    
    list2.addLast("Melquiades")
    
    list2.display()
    list1.display()
        
    concatenate(list1, list2)

        
        
        
        
        
        