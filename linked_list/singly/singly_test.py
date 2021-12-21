import singly


def test_singly_linkedlist_length_calc():
  linked_list = singly.LinkedList()
  linked_list.append(1)
  linked_list.append(2)
  assert linked_list.length() == 2

def test_singly_linkedlist_append_node():
  linked_list = singly.LinkedList()
  assert linked_list.length() == 0

  linked_list.append("value_one")
  assert linked_list.length() == 1

  linked_list.append("value_two")
  assert linked_list.length() == 2

def test_singly_linkedlist_to_list():
  linked_list = singly.LinkedList()
  linked_list.append(1)
  linked_list.append(2)
  assert linked_list.to_list() == [1, 2]


def test_singly_linkedlist_reverse():
  linked_list = singly.LinkedList()
  linked_list.append(1)
  linked_list.append(2)
  linked_list.reverse_linkedlist()
  assert linked_list.to_list() == [2, 1]

def test_singly_linkedlist_get_by_index():
  linked_list = singly.LinkedList()
  linked_list.append(1)
  linked_list.append(2)
  assert linked_list.get(1) == 2
  assert linked_list.get(2) is None

