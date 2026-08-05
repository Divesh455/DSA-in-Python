class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    def Traverse(self):

        if self.head is None:
            print("List are Empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.val,"->",end=" ")
                cur = cur.next


sll = SinglyLinkedList()
sll.append(12)
sll.append(13)
sll.append(14)
sll.append(15)
sll.Traverse()
