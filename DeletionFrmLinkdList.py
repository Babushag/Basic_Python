class Node:
  def __init__(self,cargo=None,next=None):
    self.cargo=cargo
    self.next=next
    
  
  def __str__(self):
    return str(self.cargo)
    
  def print_list(self,node):
    while node is not None:
      print(node,end=" ")
      node=node.next
      
  def remove_node(self,node):
    while node.next is None:return
    first=node
    second=node.next
    first.next=second.next
    second.next=None
      
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
print("Earlier the linkedlist is",end=" ")
node1.print_list(node1)
node1.remove_node(node1)
print()
print("List after deletion linkedlist is",end=" ")
node1.print_list(node1)