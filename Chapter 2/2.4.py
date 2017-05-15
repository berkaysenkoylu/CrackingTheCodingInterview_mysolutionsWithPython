## Chapter 2 - 2.4) Partition

import linked_list
from random import choice

## Populating the linked list as given in the problem
myList = [1, 2, 10, 5, 8, 5, 3]

myLinkedList = linked_list.LinkedList()

for element in myList:
    myLinkedList.add(element)
#####################################################

def partition(myLinkedList, k):
    
    transformedList = []
    
    ## Transform the list into an ordinary python list
    transformedList = myLinkedList.linkedListToList()

    ## Sort the list using python method "sort". (Algorithms such as bubble sort etc may also be utilized.)
    transformedList.sort()

    left_partition, right_partition = [], []
    
    
    ## Divide the list into left and right partitions
    if k in transformedList:
        index = transformedList.index(k)
        left_partition = transformedList[:index]
        right_partition = transformedList[index:]
    else:
        index = 0
        for i in range(len(transformedList)):
            if transformedList[i] > k:
                index = i
                break
        left_partition = transformedList[:index]
        right_partition = transformedList[index:]

    ## Now randomly pick from right and left partition in order,
    ## and populate the new linked list, which will replace
    ## the given linked list (First right, then left)

    newLinkedList = linked_list.LinkedList()
    
    ## Start with right
    while right_partition:
        ## Randomly choose an element (To create a shuffle effect)
        new_element = choice(right_partition)
        
        ## Get the index of it
        index = right_partition.index(new_element)

        ## Remove it from the list, and save it to another variable
        element_to_add = right_partition.pop(index)

        ## Add it to the new linked list
        newLinkedList.add(element_to_add)

    ## Left
    while left_partition:
        ## Randomly choose an element (To create a shuffle effect)
        new_element = choice(left_partition)
        
        ## Get the index of it
        index = left_partition.index(new_element)

        ## Remove it from the list, and save it to another variable
        element_to_add = left_partition.pop(index)

        ## Add it to the new linked list
        newLinkedList.add(element_to_add)
    

    return newLinkedList



## DEMO ##

newLinkedList = partition(myLinkedList, 5)
newLinkedList.iterate_through_list()


































