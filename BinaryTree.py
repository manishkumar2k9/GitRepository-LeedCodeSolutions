class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_Empty():
            return self.items.pop()

    def is_Empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_Empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,value):
        self.items.insert(0,value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node():
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class BinaryTree():
    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preoder_traverse(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_traverse(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(self.root, "")
        elif traversal_type == "levelorder":
            return self.inLeverOrder_traverse(self.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_traverse(self.root)
        elif traversal_type == "ZigzagLevelOrderTraversal":
            return self.ZigzagLevelOrderTraversal(self.root)
        else:
            print("The traversal " + str(traversal_type) + " is not valid !")
            return False

    def preoder_traverse(self, start, traversal):
        if start:
            traversal += str(start.value) + " -> "
            traversal = self.preoder_traverse(start.left, traversal)
            traversal = self.preoder_traverse(start.right, traversal)
        return traversal

    def inorder_traverse(self,start, traversal):
        if start:
            traversal = self.inorder_traverse(start.left, traversal)
            traversal += str(start.value) + " -> "
            traversal = self.inorder_traverse(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left,traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += str(start.value) + " -> "
        return traversal

    def height(self, start,counter):
        #counter = 0
        if start.left and start.right is None:
            return 1
        if start.left:
            counter += self.height(start.left)
        elif start.right:
            counter += self.height(start.right)
        return counter

    def inLeverOrder_traverse(self, start):
        if start is None:
            return
        queue = Queue()
        outputStr = []
        queue.enqueue(start)
        while len(queue) > 0:
            currNode = queue.dequeue()
            #print(currNode.value)
            outputStr.append(currNode.value)
            if currNode.right:
                queue.enqueue(currNode.right)
            if currNode.left:
                queue.enqueue(currNode.left)
        return " -> ".join(outputStr)

    def reverse_levelorder_traverse(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()

        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += (str(node.value) + " -> ")

        return traversal

    def height(self, start):
        if start is None:
            return -1
        left_height = self.height(start.left)
        right_height = self.height(start.right)

        ## Adding 1 to make sure we get 0 on leaf and add 1 upwards.
        return 1 + max(left_height, right_height)

    # Total no. of nodes, recursion way
    def size_(self, start):
        if start is None:
            return 0
        return 1 + self.size_(start.left) + self.size_(start.right)


    # Total no. of nodes, iterative way
    def size(self, start):
        if start is None:
            return 0
        queue = Queue()
        counter = 1
        queue.enqueue(start)
        while len(queue) > 0:
            node = queue.dequeue()
            if node.left:
                counter += 1
                queue.enqueue(node.left)
            if node.right:
                counter += 1
                queue.enqueue(node.right)
        return counter

    def ZigzagLevelOrderTraversal(self, start):
        currentQ = Queue()
        nextQ = Queue()
        flag = False
        traversal = []
        temp = []
        currentQ.enqueue(start)
        while len(currentQ) > 0:
            node = currentQ.dequeue()
            if flag:
                if node.left:
                    nextQ.enqueue(node.left)
                if node.right:
                    nextQ.enqueue(node.right)
            else:
                if node.right:
                    nextQ.enqueue(node.right)
                if node.left:
                    nextQ.enqueue(node.left)
            temp.append(node.value)
            if len(currentQ) == 0:
                flag = not flag
                currentQ, nextQ = nextQ, currentQ
                traversal.append(temp)
                temp = []
        return traversal



'''
tree = BinaryTree('f')
tree.root.left = Node('b')
tree.root.right = Node('g')
tree.root.left.left = Node('a')
tree.root.left.right = Node('d')
tree.root.left.right.left = Node('c')
tree.root.left.right.right = Node('e')
tree.root.left.right.right.right = Node('j')
tree.root.left.right.right.right.right = Node('k')
tree.root.right.right = Node('i')
tree.root.right.right.left = Node('h')
print("Pre-Order : " + str(tree.print_tree("preorder")))
print("In-Order  : " + str(tree.print_tree("inorder")))
print("Post-Order: " + str(tree.print_tree("postorder")))
#print("Height    : " + str(tree.height(tree.root)))
print("Level-Order: " + str(tree.print_tree("levelorder")))
#print("reverse_levelorder: " + str(tree.reverse_levelorder_traverse("reverse_levelorder")))
print("Height of this tree: " + str(tree.height(tree.root)))
print("Size of this tree: " + str(tree.size(tree.root)))
print("Size (Recursion) of this tree: " + str(tree.size_(tree.root)))
'''

tree = BinaryTree(3)
tree.root.left = Node(9)
tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)
print("Pre-Order : " + str(tree.print_tree("preorder")))
print("ZigzagLevelOrderTraversal : " + str(tree.print_tree("ZigzagLevelOrderTraversal")))