## Linked List

class Node():

    def __init__(self, data, n=None):
        self.data = data
        self.next = n

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList():

    def __init__(self, root=None):
        ## When one creates a list root is None, since it is empty
        self.root = root

        ## Size = 0, since we have an empty list
        self.size = 0

    def add(self, data):
        ## First, create a node
        newNode = Node(data, self.root)

        ## Change the root to the new node
        self.root = newNode

        ## Increment the size of the linked list
        self.size += 1

    def add_node(self, node):
        """A method that adds a node"""
        ## Change the root to the new node
        self.root = node

        ## Increment the size of the linked list
        self.size += 1

    def find(self, data):
        """Find the given data in the linked list."""
        ## We start with the root node
        currentNode = self.root

        ## If we hit the end of the list currentNode will be None, breaking the loop
        while currentNode:

            ## If we find the data, return it
            if currentNode.get_data() == data:
                return data
            else:
                ## We move on to the next node
                currentNode = currentNode.get_next()

        ## if we haven't returned anything so far, it means we couldn't find the data in the list, thus return None
        return None

    def remove(self, data):
        currentNode = self.root
        previousNode = None

        while currentNode:
            if currentNode.get_data() != data:
            ## It is not the one we are looking to remove, move on
                previousNode = currentNode
                currentNode = currentNode.get_next()
            else:
                ## Check if previousNode exists
                if previousNode:
                    previousNode.set_next(currentNode.get_next())
                else:
                    ## If previousNode doesn't exist, it means the data you are looking for is in the first node
                    self.root = currentNode.get_next()
                self.size -= 1
                return True
            
        ## When the data doesn't exist in the list
        return False
                
    def iterate_through_list(self, k=1):
        """Iterate through the list, printing the data."""
        currentNode = self.root
        counter = 1
        while currentNode:
            if counter >= k:
                print currentNode.get_data()
            currentNode = currentNode.get_next()
            counter += 1

    def remove_duplicates(self):
        """Iterate through the linked list and remove the duplicate elements"""
        myList = self.linkedListToList()   ## A list that contains the nodes' datas
        glossary = {} ## A dict that holds the unique elements, and their number of occurances {"element" : "how many of it that list has"}

        ## Populate the dictionary
        for data in myList:
            if data not in glossary:
                glossary[data] = myList.count(data)

        ## Removal should take place if the item occurs more than once
        for key, value in glossary.items():
            if value > 1:
                for _ in range(value - 1):
                    self.remove(key)

    def delete_middle_node(self):
        """A function that deletes the node located in the middle"""
        ## For either odd or even number, middle is going to be the same number
        middle = self.size / 2

        ## Since there is no indexing, it is done manually by counting
        counter = 1

        ## The first node is not the middle one (The question states that way). Thus, nothing changes in the list
        if middle == 1:
            return False

        ## Iterating through the linked list, when counter == middle, remove operation will take place
        currentNode = self.root
        while currentNode:
            if counter == middle:
                self.remove(currentNode.get_data())
                return True
            else:
                currentNode = currentNode.get_next()
                counter += 1

    def linkedListToList(self):
        """A method that converts the linked list to a list"""
        myList = []
        currentNode = self.root
        while currentNode:
            myList.append(currentNode.get_data())
            currentNode = currentNode.get_next()

        return myList

    def isPalindrome(self):
        """A method to check if the linked list is a palindrome"""
        myList = self.linkedListToList()
        return myList == myList[::-1]

    def outputLastNode(self):
        """A method that outputs the last node"""
        currentNode = self.root

        while currentNode:
            if currentNode.get_next() == None:
                return currentNode
            else:
                currentNode = currentNode.get_next()

    def whereLoopBegins(self):
        """
        A function for circular looped linked list,
        it returns the element at the start of the each
        loop.
        """
        myList = []
        currentNode = self.root
        while currentNode:
            if currentNode.get_data() not in myList:
                myList.append(currentNode.get_data())
                currentNode = currentNode.get_next()
            else:
                return currentNode.get_data()
        

    def add_to_end(self, data):
        """A method that adds a node to the last node of the linked list"""
        
        currentNode = self.root
        
        while currentNode:
            if currentNode.get_next() == None:
                ## The last node
                new_node = Node(data)
                currentNode.set_next(new_node)
                self.size += 1
                return True
            else:
                currentNode = currentNode.get_next()
            

    def getAddresses(self):
        """
        A method that returns a list containing
        the address of the nodes in the memory
        """
        addresses = []

        currentNode = self.root
        while currentNode:
            if currentNode.get_next() != None:
##                print currentNode
                addresses.append(currentNode)
            currentNode = currentNode.get_next()

        return addresses












