class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list."""
        items = []
        node = self.head
        while node is not None:
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes."""
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        new_node = Node(item)
        if self.is_empty():
            # If the list is empty, new node is both head and tail
            self.head = self.tail = new_node
        else:
            # Otherwise, append the new node after the current tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list."""
        new_node = Node(item)
        if self.is_empty():
            # If the list is empty, new node is both head and tail
            self.head = self.tail = new_node
        else:
            # Otherwise, make the new node the head and link it to the old head
            new_node.next = self.head
            self.head = new_node

    def find(self, matcher):
        """Return an item from this linked list if it matches the given condition."""
        node = self.head
        while node is not None:
            if matcher(node.data):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the first occurrence of item in the list."""
        current = self.head
        prev = None
        
        # Case 1: The list is empty
        if current is None:
            raise ValueError(f"Item not found: {item}")

        # Case 2: Item to be deleted is the head
        if current.data == item:
            self.head = current.next
            if self.head is None:  # If list becomes empty, tail should also be None
                self.tail = None
            return

        # Case 3: Item to be deleted is somewhere other than the head
        while current:
            if current.data == item:
                if current.next is None:  # If it's the last node, update the tail
                    self.tail = prev
                prev.next = current.next
                return
            prev = current
            current = current.next

        # Case 4: Item not found, raise ValueError
        raise ValueError(f"Item not found: {item}")

    def replace(self, old_item, new_item):
        node = self.head
        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return True
            node = node.next
        return False

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()