# singly LinkedList

'''
      head          second       third
        |             |            |
        |             |            |
    +---+----+   +---+----+   +---+-----+
    | 1 | o----->| 2 | o----->| 3 | null|
    +---+----+   +---+----+   +---+-----+
'''

# list node
class Node:
  def __init__(self, data):
    self.data = data
    # reference to the next value of the list
    self.next = None

class LinkedList:
  def __init__(self):
      self.head = None

  # insert values in the list
  def append(self, data):
    new_node = Node(data)

    # if the list is empty
    if self.head == None:
      # first head
      self.head = new_node
      return     

    current_node = self.head

    # false if current.node is None
    while current_node.next:
      # creates reference to the next node
      current_node = current_node.next
    # defines the next node
    current_node.next = new_node
    return

  # return linkedlist length
  def length(self):
    if self.head == None:
      return 0
    current_node = self.head
    total = 0
  
    while current_node:
      total += 1
      current_node = current_node.next
    
    return total
  
  # return linkedlist in a normal array
  def to_list(self):
    node_data = []
    current_node = self.head

    while current_node:
      node_data.append(current_node.data)
      current_node = current_node.next
    return node_data
  
  # get element by index in linkedlist
  def get(self, index):
    if index >= self.length() or index < 0:
      print("Index out of range")
      return None
    current_index = 0
    current_node = self.head
    while current_node != None:
      if current_index == index:
        return current_node.data
      current_node = current_node.next
      current_index += 1
  
  # print in console all value of linkedlist
  def display(self):
    contents = self.head

    if contents is None:
      print("List has no data")

    while contents:
      print(contents.data)
      contents = contents.next
    print("-------")

  # return linkedlist reversed
  def reverse_linkedlist(self):
    previous_node = None
    current_node = self.head
    while current_node != None:
      next = current_node.next
      current_node.next = previous_node
      previous_node = current_node
      current_node = next
    self.head = previous_node

