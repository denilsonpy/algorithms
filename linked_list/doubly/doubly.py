# doubly LinkedList

'''
      head          second       third
        |             |            |
        |             |            |
    +---+----+   +---+----+   +---+-----+
    | 1 | o----->| 2 | o----->| 3 | null|
    |   | o<-----|   | o<-----|   |     |
    +---+----+   +---+----+   +---+-----+
'''
class DoubleNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.previous = None
  
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, data):
    new_node = DoubleNode(data)

    new_node.next = None
    if self.head == None:
      new_node.previous = None
      self.head = new_node
      return
    last_node = self.head
    while last_node:
      last_node = last_node.next
    last_node.next = new_node

    new_node.previous = last_node
    return