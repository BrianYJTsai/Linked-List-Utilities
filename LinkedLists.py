#  File: ERsim.py
#  Description: This programs operates using linked lists. The user can store data and retrieve
#  information using the linked list API
#  Student's Name: Brian Tsai
#  Student's UT EID: byt76
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 10/25/17
#  Date Last Modified: 10/28/17


class Node (object):

   # Create a new node
   def __init__(self,initdata):
      self.data = initdata
      self.next = None

   # Return the node's data
   def getData(self):
      return self.data

   # Return a pointer to the next node
   def getNext(self):
      return self.next

   # Set the data of the node
   def setData(self, newData):
      self.data = newData

   # Set the pointer to the next node
   def setNext(self,newNext):
      self.next = newNext


class LinkedList:

    # Create a new linked list
    def __init__(self):
        self.head = None

    # Return the string representation of the linked list
    def __str__(self):
        list = []
        current = self.head

        # Append all node data to a list
        while (current != None):
            list.append(current.getData())
            current = current.getNext()

        # Format the nodes into ordered sequences
        list = [list[node : min(node + 10, len(list))] for node in range(0, len(list), 10)]
        list = ['  '.join(row) for row in list]
        string = '\n'.join(list)
        return str(string)

    # Add a node to the front of the linked list
    def addFirst(self, item):

        temp = Node(item)
        oldHead = self.head

        # Add new node to the front
        if (self.head == None):
            self.head = temp
        else:
            temp.setNext(oldHead)
            self.head = temp

    # Add a node to the end of the linked list
    def addLast(self, item):

        newNode = Node(item)
        currentNode = self.head

        # Add to the front of there are no elements in the list
        if (currentNode == None):
            self.head = newNode
            return

        # Search for the end of the linked list and the new node to the end
        while(currentNode.getNext() != None):
            currentNode = currentNode.getNext()
        currentNode.setNext(newNode)

    # Add a node such that the linked list remains in alphabetical order
    def addInOrder(self, item):

        newNode = Node(item)
        previousNode = self.head
        currentNode = self.head

        # Add a node to the front if there are no elements in the list
        if (currentNode == None):
            self.head = newNode
            return

        # Else, search for the correct spot to place the new element
        while(currentNode != None and newNode.getData() > currentNode.getData()):
            previousNode = currentNode
            currentNode = currentNode.getNext()

        # Add the new node to the proper location
        if (currentNode == self.head):
            self.head = newNode
            newNode.setNext(currentNode)
        else:
            previousNode.setNext(newNode)
            newNode.setNext(currentNode)


    # Return the length of the list
    def getLength(self):

        current = self.head
        count = 0

        # Count the number of items in the list
        while(current != None):
            current = current.getNext()
            count+=1
        return count

    # Search the unsorted list for the element
    def findUnordered(self, item):

        currentNode = self.head

        # Iterate through the list searching for the element
        while(currentNode != None):

            # Return true if the element is found
            if (item == currentNode.getData()):
                return True
            currentNode = currentNode.getNext()

        # Return false if the element is not found
        return False


    # Search the ordered list for the element
    def findOrdered(self, item):

        currentNode = self.head

        # Iterate through the list searching for the element or until the current node is larger than the element
        while (currentNode != None and item >= currentNode.getData()):

            # Return true if the element is found
            if (currentNode.getData() == item):
                return True
            currentNode = currentNode.getNext()

        # Return false if the element is not found
        return False


    # Remove the element from the linked list if found
    def delete(self, item):

        previousNode = self.head
        currentNode = self.head
        found = False

        # Iterate through the list and search for the element
        while(currentNode != None):
            if (currentNode.getData() == item):
                found = True
                break
            previousNode = currentNode
            currentNode = currentNode.getNext()

        # If the element is found, then remove it
        if (found):

            # Remove from the front
            if (currentNode == self.head):
                self.head = currentNode.getNext()

            # Remove from the end
            elif (currentNode.getNext() == None):
                previousNode.setNext(None)

            # Remove from in between
            else:
                previousNode.setNext(currentNode.getNext())
            return True

        else:
            return False


    # Return a copy of the original linked list
    def copyList(self):

        newList = LinkedList()
        oldCurrent = self.head

        # Create a copy of each node and add it to the new linked list
        while(oldCurrent != None):
            newList.addLast(oldCurrent.getData())
            oldCurrent = oldCurrent.getNext()
        return newList


    # Return a reverse copy of the original linked list
    def reverseList(self):

        newList = LinkedList()
        oldCurrent = self.head

        # Create a copy of each node and add it in reverse order to the new linked list
        while (oldCurrent != None):
            newList.addFirst(oldCurrent.getData())
            oldCurrent = oldCurrent.getNext()
        return newList


    # Return a copy of the original linked list in alphabetical order
    def orderList(self):

        newList = LinkedList()
        oldCurrent = self.head

        # Create a copy of each node and add it in order to the new linked list
        while(oldCurrent != None):
            newList.addInOrder(oldCurrent.getData())
            oldCurrent = oldCurrent.getNext()
        return newList


    # Return whether a list is in alphabetical order
    def isOrdered(self):

        current = self.head
        previous = self.head

        # Iterate through the linked list and break only when the list is out of order
        while (current != None):
            if (previous.getData() > current.getData()):
                return False
            previous = current
            current = current.getNext()
        return True

    # Return whether the list is empty
    def isEmpty(self):

        # Return True if a list is empty, or False otherwise
        return self.head == None

    # Merge two linked lists together and return a new linked list in alphabetical order
    def mergeList(self, b):

        newList = LinkedList()
        currentHead = self.head

        # Add elements of the first linked list to the new linked list
        while (currentHead != None):
            newList.addInOrder(currentHead.getData())
            currentHead = currentHead.getNext()

        currentHead = b.head

        # Add all elements of the second linked list to the new linked list
        while(currentHead != None):
            newList.addInOrder(currentHead.getData())
            currentHead = currentHead.getNext()

        return newList

    # Return whether two linked lists are equal
    def isEqual(self, b):

        listCurrent1 = self.head
        listCurrent2 = b.head

        # Iterate through each linked list
        while (listCurrent1 != None and listCurrent2 != None):

            # If each element is the same, then increase the index
            if (listCurrent1.getData() == listCurrent2.getData()):
                listCurrent1 = listCurrent1.getNext()
                listCurrent2 = listCurrent2.getNext()

            # Else, the linked lists are not the same
            else:
                break

        # If both linked lists have reach the end, then they are the same
        if (listCurrent1 == None and listCurrent2 == None):
            return True

        return False


    # Remove all duplicate elements from the linked list
    def removeDuplicates(self):

        duplicateList = LinkedList()
        current = self.head

        # Iterate through the linked list adding only unique elements
        while (current != None):
            if (not duplicateList.findUnordered(current.getData())):
                duplicateList.addLast(current.getData())
            current = current.getNext()
        return duplicateList


def main():

    # Test the program
    print("\n\n***************************************************************")
    print("Test of addFirst:  should see 'node34...node0'")
    print("***************************************************************")
    myList1 = LinkedList()
    for i in range(35):
        myList1.addFirst("node" + str(i))

    print(myList1)

    print("\n\n***************************************************************")
    print("Test of addLast:  should see 'node0...node34'")
    print("***************************************************************")
    myList2 = LinkedList()
    for i in range(35):
        myList2.addLast("node" + str(i))

    print(myList2)

    print("\n\n***************************************************************")
    print("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
    print("***************************************************************")
    greekList = LinkedList()
    greekList.addInOrder("gamma")
    greekList.addInOrder("delta")
    greekList.addInOrder("alpha")
    greekList.addInOrder("epsilon")
    greekList.addInOrder("omega")
    print(greekList)

    print("\n\n***************************************************************")
    print("Test of getLength:  should see 35, 5, 0")
    print("***************************************************************")
    emptyList = LinkedList()
    print("   Length of myList1:  ", myList1.getLength())
    print("   Length of greekList:  ", greekList.getLength())
    print("   Length of emptyList:  ", emptyList.getLength())

    print("\n\n***************************************************************")
    print("Test of findUnordered:  should see True, False")
    print("***************************************************************")
    print("   Searching for 'node25' in myList2: ", myList2.findUnordered("node25"))
    print("   Searching for 'node35' in myList2: ", myList2.findUnordered("node35"))

    print("\n\n***************************************************************")
    print("Test of findOrdered:  should see True, False")
    print("***************************************************************")
    print("   Searching for 'epsilon' in greekList: ", greekList.findOrdered("epsilon"))
    print("   Searching for 'omicron' in greekList: ", greekList.findOrdered("omicron"))

    print("\n\n***************************************************************")
    print("Test of delete:  should see 'node25 found', 'node34 found',")
    print("   'node0 found', 'node40 not found'")
    print("***************************************************************")
    print("   Deleting 'node25' (random node) from myList1: ")
    if myList1.delete("node25"):
        print("      node25 found")
    else:
        print("      node25 not found")
    print("   myList1:  ")
    print(myList1)

    print("   Deleting 'node34' (first node) from myList1: ")
    if myList1.delete("node34"):
        print("      node34 found")
    else:
        print("      node34 not found")
    print("   myList1:  ")
    print(myList1)

    print("   Deleting 'node0'  (last node) from myList1: ")
    if myList1.delete("node0"):
        print("      node0 found")
    else:
        print("      node0 not found")
    print("   myList1:  ")
    print(myList1)

    print("   Deleting 'node40' (node not in list) from myList1: ")
    if myList1.delete("node40"):
        print("      node40 found")
    else:
        print("   node40 not found")
    print("   myList1:  ")
    print(myList1)

    print("\n\n***************************************************************")
    print("Test of copyList:")
    print("***************************************************************")
    greekList2 = greekList.copyList()
    print("   These should look the same:")
    print("      greekList before delete:")
    print(greekList)
    print("      greekList2 before delete:")
    print(greekList2)
    greekList2.delete("alpha")
    print("   This should only change greekList2:")
    print("      greekList after deleting 'alpha' from second list:")
    print(greekList)
    print("      greekList2 after deleting 'alpha' from second list:")
    print(greekList2)
    greekList.delete("omega")
    print("   This should only change greekList1:")
    print("      greekList after deleting 'omega' from first list:")
    print(greekList)
    print("      greekList2 after deleting 'omega' from first list:")
    print(greekList2)

    print("\n\n***************************************************************")
    print("Test of reverseList:  the second one should be the reverse")
    print("***************************************************************")
    print("   Original list:")
    print(myList1)
    print("   Reversed list:")
    myList1Rev = myList1.reverseList()
    print(myList1Rev)

    print("\n\n***************************************************************")
    print("Test of orderList:  the second list should be the first one sorted")
    print("***************************************************************")
    planets = LinkedList()
    planets.addFirst("Mercury")
    planets.addFirst("Venus")
    planets.addFirst("Earth")
    planets.addFirst("Mars")
    planets.addFirst("Jupiter")
    planets.addFirst("Saturn")
    planets.addFirst("Uranus")
    planets.addFirst("Neptune")
    planets.addFirst("Pluto?")

    print("   Original list:")
    print(planets)
    print("   Ordered list:")
    orderedPlanets = planets.orderList()
    print(orderedPlanets)

    print("\n\n***************************************************************")
    print("Test of isOrdered:  should see False, True")
    print("***************************************************************")
    print("   Original list:")
    print(planets)
    print("   Ordered? ", planets.isOrdered())
    orderedPlanets = planets.orderList()
    print("   After ordering:")
    print(orderedPlanets)
    print("   ordered? ", orderedPlanets.isOrdered())

    print("\n\n***************************************************************")
    print("Test of isEmpty:  should see True, False")
    print("***************************************************************")
    newList = LinkedList()
    print("New list (currently empty):", newList.isEmpty())
    newList.addFirst("hello")
    print("After adding one element:", newList.isEmpty())

    print("\n\n***************************************************************")
    print("Test of mergeList")
    print("***************************************************************")
    list1 = LinkedList()
    list1.addLast("aardvark")
    list1.addLast("cat")
    list1.addLast("elephant")
    list1.addLast("fox")
    list1.addLast("lynx")
    print("   first list:")
    print(list1)
    list2 = LinkedList()
    list2.addLast("bacon")
    list2.addLast("dog")
    list2.addLast("giraffe")
    list2.addLast("hippo")
    list2.addLast("wolf")
    print("   second list:")
    print(list2)
    print("   merged list:")
    list3 = list1.mergeList(list2)
    print(list3)

    print("\n\n***************************************************************")
    print("Test of isEqual:  should see True, False, True")
    print("***************************************************************")
    print("   First list:")
    print(planets)
    planets2 = planets.copyList()
    print("   Second list:")
    print(planets2)
    print("      Equal:  ", planets.isEqual(planets2))
    print(planets)
    planets2.delete("Mercury")
    print("   Second list:")
    print(planets2)
    print("      Equal:  ", planets.isEqual(planets2))
    print("   Compare two empty lists:")
    emptyList1 = LinkedList()
    emptyList2 = LinkedList()
    print("      Equal:  ", emptyList1.isEqual(emptyList2))

    print("\n\n***************************************************************")
    print("Test of removeDuplicates:  original list has 14 elements, new list has 10")
    print("***************************************************************")
    dupList = LinkedList()
    print("   removeDuplicates from an empty list shouldn't fail")
    newList = dupList.removeDuplicates()
    print("   printing what should still be an empty list:")
    print(newList)
    dupList.addLast("giraffe")
    dupList.addLast("wolf")
    dupList.addLast("cat")
    dupList.addLast("elephant")
    dupList.addLast("bacon")
    dupList.addLast("fox")
    dupList.addLast("elephant")
    dupList.addLast("wolf")
    dupList.addLast("lynx")
    dupList.addLast("elephant")
    dupList.addLast("dog")
    dupList.addLast("hippo")
    dupList.addLast("aardvark")
    dupList.addLast("bacon")
    print("   original list:")
    print(dupList)
    print("   without duplicates:")
    newList = dupList.removeDuplicates()
    print(newList)

    test = LinkedList()
    test.addLast("a")
    test.addLast("b")
    test.addLast("c")
    test.delete("b")
    print()

main()