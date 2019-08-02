#!/usr/bin/env python3
"""Linked list implementation."""


class Node:
    """Represents a node of a singly-linked list."""

    def __init__(self, value=None, next=None):
        """Initialize a new linked list node.
        
        Attributes:
            value (None or int): The value of the node.
            next (None or Node): The next node in the linked list.
        """
        self.val = value
        self.next = next


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Initialize a new singly-linnked list."""
        self.head = None

    def get(self, index):
        """Retrive the index-th node in the singly-linked list.

        If the index is invalid, returns -1.

        Attributes:
            index (int): The index in the linked list of the node to retrieve.
        """
        current = self.head
        while current is not None and index > 0:
            current = current.next
            index -= 1

        return -1 if index != 0 or current is None else current.val

    def addAtHead(self, val):
        """Add a node to the head of the singly-linked list.

        Attributes:
            val (int): The value of the new node to add.
        """
        new = Node(val, self.head)
        self.head = new

    def addAtTail(self, val):
        """Append a node to the end of the singly-linked list.

        Attributes:
            val (int): The value of the new node to append.
        """
        tail = self.head
        while tail is not None and tail.next is not None:
            tail = tail.next

        if tail is None:
            self.head = Node(val, None)
        else:
            tail.next = Node(val, None)

    def addAtIndex(self, index, val):
        """Add a node before the index-th node in the singly-linked list.

        If the index is equal to the length of the list, the node is
        appended to the end.
        If the index is greater than the length, the node is not inserted.

        Attributes:
            index (int): The index in the linked list to insert the node before.
            val (int): The value of the new node to add.
        """
        current = self.head
        while current is not None and current.next is not None and index > 1:
            current = current.next
            index -= 1

        if index <= 0:
            self.head = Node(val, None)
        elif index == 1 and current is not None:
            new = Node(val, current.next)
            current.next = new

    def deleteAtIndex(self, index):
        """Delete the index-th node in the linked list, if the index is valid.

        Attributes:
            index (int): The index of the node to delete.
        """
        current = self.head
        previous = None
        while current is not None and index > 0:
            previous = current
            current = current.next
            index -= 1
        if current is not None and index == 0:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next


def reverseList(self, head):
    """Reverse a singly-linked list.

    Attributes:
        head (Node): The head of the linked list to reverse.
    Returns:
        The head of the reversed linked list.
    """
    if head is None:
        return None

    reverse = ListNode(head.val)
    reverse.next = None

    head = head.next
    while head is not None:
        new = ListNode(head.val)
        new.next = reverse
        reverse = new
        head = head.next

    return reverse


def hasCycle(self, head):
    """Determine if a singly-linked list contains a cycle.

    Attributes:
        head (Node): The head of the singly-linked list.
    Returns:
        True if the list contains a cycle, False otherwise.
    """
    if head is None or head.next is None:
        return False
    tortoise, hare = head, head.next
    while (
        tortoise.next is not None
        and hare.next is not None
        and hare.next.next is not None
    ):
        if tortoise.val == hare.val:
            return True
        tortoise = tortoise.next
        hare = hare.next.next
    return False


def detectCycle(self, head):
    """Return the node where a cycle in a singly-linked list begins.
        
        Attributes:
            head (Node): The head of the singly-linked list.
        Returns:
            If a cycle exists, the node where it begins; None otherwise.
        """
    if head is None or head.next is None:
        return None

    tortoise, hare = head, head.next
    while (
        tortoise.next is not None
        and hare.next is not None
        and hare.next.next is not None
    ):
        if tortoise == hare:
            tortoise = head
            hare = hare.next
            while tortoise != hare:
                tortoise = tortoise.next
                hare = hare.next
            return tortoise

        tortoise = tortoise.next
        hare = hare.next.next

    return None
