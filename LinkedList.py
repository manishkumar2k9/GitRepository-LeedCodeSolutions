from NodePkg.Node import Node

class LinkedListClass():

    def __init__(self):
        self.head = Node()

    def append(self, data):
        cur = self.head
        print("data {} cur.head {} ".format(str(data),str(id(cur.nex))))
        while cur.next_node is not None:
            cur = cur.next()
        cur.next_node = Node(data)

    def display(self):
        cur = self.head
        elem = {}
        while cur.next() is not None:
            elem[cur.data] = id(cur.next())
        return elem

l1 = LinkedListClass()
print(" Here {} " + str(id(l1.head)))
l1.append(10)
print(" Here {} " + str(id(l1.head)))
l1.append(20)
print(" Here {} " + str(id(l1.head)))
print(l1.display())