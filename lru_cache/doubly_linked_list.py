"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes. """
#ALL TESTS FINALLY PASS

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    # TEST PASSES
    def add_to_head(self, value):
        # wrap the given value in a ListNode
        new_head = ListNode(value)
        # this will increase the length in increments
        self.length += 1
        # handle if list has a head
        if not self.head and not self.tail:
            # changes other node to new node
            self.head = new_head
            # inserts a new node at the head
            self.tail = new_head
        # handle if list has no head
        else:
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    # TEST PASSES
    def remove_from_head(self):
        if not self.head:
            return
        value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
            self.length = 0
        else:
            node_begone = self.head
            self.head = self.head.next
            self.delete(node_begone)
        # value = self.head.value
        # # runs the actual delete method
        # self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    # TEST PASSES
    def add_to_tail(self, value):
        new_node = ListNode(value)

        self.length += 1

        if self.tail:
            self.tail.next = new_node
            # sets new node previous to the new tail
            new_node.prev = self.tail
            # replaces the tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    # TEST PASSES
    def remove_from_tail(self):
        if self.tail is None and self.head is None:
            return None
        value = self.tail.value
        # value you want to return is reassigned
        if self.tail == self.head:
            self.length = 0
            self.tail = self.head = None
        else:
            node_begone = self.tail
            self.tail = self.tail.prev
            self.delete(node_begone)
        return value

        # value = self.tail.value
        # # runs the actual delete method
        # self.delete(self.tail)
        # return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    #TEST PASSSES
    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)

    # delete
    # then add_to_head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    #TEST PASSES
    def move_to_end(self, node):
        self.add_to_tail(node.value)
        self.delete(node)

    # delete

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    #TEST PASSES
    def delete(self, node):
        """"# if statement for if node was the head or tail
                if not self.head:
                    return None
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                # use remove_from_head open ended
                if node == self.head:
                    self.head = node.next
                    self.head.prev = None
                # use remove_from_tail open ended
                if node == self.tail:
                    self.tail = node.prev
                    self.tail.next = None
                else:
                    node.delete()
                self.length -= 1"""

        # this lone works
        if self.tail == node:
            self.remove_from_tail()
        elif self.head == node:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1

    """Returns the highest value currently in the list"""
    #TEST PASSES
    def get_max(self):
        if self.head == self.tail:
            return self.head.value

        node = self.head
        i = 0
        value = 0

        while i < self.length:
            i += 1
            if value < node.value:
                value = node.value
            node = node.next

        return value
