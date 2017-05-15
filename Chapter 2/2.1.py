## Chapter 2 - 2.1) Remove Dups

import linked_list 


meinList = linked_list.LinkedList()

meinList.add(1)
meinList.add(2)
meinList.add(1)
meinList.add(2)
meinList.add(3)
meinList.add(5)
meinList.add(2)
meinList.add(3)
meinList.add(6)
meinList.add(6)
meinList.add(1)


meinList.iterate_through_list()

print "#" * 50

meinList.remove_duplicates()

print "#" * 50

meinList.iterate_through_list()

