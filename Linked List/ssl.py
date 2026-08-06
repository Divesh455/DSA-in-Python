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
                
    def insert(self,p,val):
        new_node = Node(val)
        
        if p > 0 and self.head == None:
            print('Linked List are empty')
        elif p == 0:
            self.head = new_node
            print("Value add at begining")
        else:
            cur = self.head
            pr = p
            while cur is not None and pr > 1:
                cur = cur.next
                pr -= 1
                
            if cur is None:
                print("Your Position is out of range")
                return
                
            r = cur.next
            cur.next = new_node
            new_node.next = r
            print(f'Value add at {p} Position')

sll = SinglyLinkedList()
sll.append(13)
sll.append(14)
sll.append(15)
sll.append(16)
sll.append(17)
sll.insert(10,20)
sll.Traverse()
