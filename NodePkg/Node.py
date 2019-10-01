class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def next(self):
        return self.next_node

    def get_date(self):
        return self.data

    def set_next(self, new_node):
        self.next_node = new_node
