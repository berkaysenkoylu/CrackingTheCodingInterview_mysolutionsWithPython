## Chapter 2 - 2.3) Delete Middle Node

import linked_list

myList = linked_list.LinkedList()

for i in range(1, 10):
    myList.add(i)

myList.iterate_through_list()
myList.delete_middle_node()
print "#" * 50
myList.iterate_through_list()
