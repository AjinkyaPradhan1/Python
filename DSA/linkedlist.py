from dataclasses import dataclass


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)       #creating a new node from the Node Class
        current = self.head         #a temporary pointer pointing to the currentnode being in work
        if(self.head!=None):                #if self.head is Not none means than keep traversing ahead
            while(current.next != None):    # while the next node is not None
                current = current.next      # keep traversing The next node
            current.next = new_node         # when the loop gets over and we reach the current.next == None Condition then, create the new_node at the current.next


l1 = LinkedList()
l1.head = Node(3)
print(l1.head.data)
