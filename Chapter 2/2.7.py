## Chapter 2 - 2.7) Intersection

import linked_list


## Create two linked lists that have an intersect
def createTwoLinkedListWithIntersect():
    intersectingNode = linked_list.Node(7)

    ## First Linked List: 1 -> 3 -> 5 -> "7" -> 9 -> 11 ("7" node is the intersect)
    firstLinkedList = linked_list.LinkedList()
    
    ## Second Linked List: 2 -> 4 -> "7" -> 9 -> 11 ("7" node is the intersect)
    secondLinkedList = linked_list.LinkedList()

    firstLinkedList.add_node(intersectingNode)
    firstLinkedList.add(5)
    firstLinkedList.add(3)
    firstLinkedList.add(1)

    secondLinkedList.add_node(intersectingNode)
    secondLinkedList.add(4)
    secondLinkedList.add(2)

    return firstLinkedList, secondLinkedList


## FORMATION OF TWO LINKED LIST WITH AN INTERSECT

first_linkedList, second_linkedList = createTwoLinkedListWithIntersect()


## Final form of the first list
first_linkedList.add_to_end(9)
first_linkedList.add_to_end(11)
##first_linkedList.iterate_through_list()
##
##second_linkedList.iterate_through_list()

#################################################

## METHOD TO CHECK IF TWO LINKED LIST HAS AN INTERSECT
def intersecticide(firstLinkedList, secondLinkedList):
    """
    The main idea is to add the addresses of the nodes of the both linked
    lists to a python list. Then, we check for the duplicates, removing them,
    forming another list of unique adresses. If the lengths of the two lists
    are different, then we have a duplicate node, therefore, an intersect.
    """
    addresses = []

    ## Get the address of first list
    first_addresses = firstLinkedList.getAddresses()

    ## Get the address of second list
    second_addresses = secondLinkedList.getAddresses()

    ## Concatenate
    addresses = first_addresses + second_addresses


    ## Utilizing set() method of python, which forms a list containing only unique elements of the input list
    return len(addresses) != len(set(addresses))



print intersecticide(first_linkedList, second_linkedList)








