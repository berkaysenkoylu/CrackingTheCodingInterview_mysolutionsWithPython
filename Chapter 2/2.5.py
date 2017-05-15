## Chapter 2 - 2.5) Sum Lists

import linked_list

def listToInteger(inp):
    """Returns a integer."""
    integer = "" 
    for element in inp:
        integer += str(element)

    return int(integer)

def linkedListSummer(linked_list1, linked_list2, reverse=True):
    mylist1 = linked_list1.linkedListToList()
    mylist2 = linked_list2.linkedListToList()
    
    if reverse:
        mylist1 = mylist1[::-1]
        mylist2 = mylist2[::-1]
    else:
        mylist1 = mylist1
        mylist2 = mylist2

    int1 = listToInteger(mylist1)
    int2 = listToInteger(mylist2)
    
    return mylist1, mylist2, int1 + int2



linkedList = linked_list.LinkedList()
linkedList1 = linked_list.LinkedList()

linkedList.add(6)
linkedList.add(1)
linkedList.add(7) ## 7 -> 1 -> 6

linkedList1.add(2)
linkedList1.add(9)
linkedList1.add(5) ## 5 -> 9 -> 2

print linkedListSummer(linkedList, linkedList1, True)

## Note that if argument "True" is changed to "False", then the order of adding elements
## to the linked list should also be changed!

