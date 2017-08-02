class Stack:
  def __init__(self):
    self.item=[]
  
  def push(self,data):
    self.item.append(data)
    
  def pop(self):
    return self.item.pop()
    
  def isEmpty(self):
    return self.item==[]
    
s=Stack()
s.push(34)
s.push(45)
s.push(38)

#print(s.isEmpty())
while s.isEmpty():
 print(s.pop())
