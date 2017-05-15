## Chapter 2 - 2.8) Loop Detection

import linked_list

linkedList = linked_list.LinkedList()

for i in range(1, 6):
    linkedList.add(i)


linkedList.outputLastNode().set_next(linkedList.root)

print linkedList.whereLoopBegins()
