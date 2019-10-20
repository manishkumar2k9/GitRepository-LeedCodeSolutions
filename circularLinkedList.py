class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            new_node.next = self.head
        else:
            new_node = Node(data)
            curr = self.head
            while curr:
                curr = curr.next
                if curr.next == self.head:
                    break
            curr.next = new_node
            new_node.next = self.head

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

    def prepend(self,data):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        self.head = new_node

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            #print(curr.data)
            if curr.next == self.head:
                break
            curr = curr.next
        return count

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = (size // 2)
        counter = 0
        prev = None
        curr = self.head
        ## A -> B -> C -> D -> ...
        while curr and counter < mid:
            counter += 1
            prev = curr
            curr = curr.next
        prev.next = self.head
        second_circulatList = CircularLinkedList()
        while curr.next != self.head:
            second_circulatList.append(curr.data)
            curr = curr.next
        second_circulatList.append(curr.data)
        curr.next = second_circulatList

        self.print_list()
        print("")
        second_circulatList.print_list()


cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.prepend("E")
cllist.append("F")
#cllist.print_list()
print("")
#print(len(cllist))
cllist.split_list()


