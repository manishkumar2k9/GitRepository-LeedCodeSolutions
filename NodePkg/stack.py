class Stack():

   def __init__(self):
       self.items = []
       self.minList = []
       self.maxList = []

   def push(self, value):
       self.items.append(value)
       if self.isEmpty(self.minList):
           self.minList.append(value)
       else:
           if value < self.minList[-1]:
               self.minList.append(value)

       if self.isEmpty(self.maxList):
           self.maxList.append(value)
       else:
           if value > self.maxList[-1]:
               self.maxList.append(value)

   def isEmpty(self, list):
       return list == []

   def pop(self):
       return self.items.pop()

   def peek(self):
       return self.items[-1]

   def get_Stack(self):
       return self.items

   def min(self):
       return self.minList[-1]

   def max(self):
       return self.maxList[-1]


s = Stack()
s.push(25)
s.push(30)
s.push(5)
s.push(100)
print(s.get_Stack())
print(s.min())
print(s.max())


