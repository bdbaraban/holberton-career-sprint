#!/usr/bin/env python3
"""Binary tree implementation."""

class Node:
    """Represents a node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """Initialize a new Node.

        Attributes:
            value (None or int): The value of the node.
            left (None or Node): The left child of the node.
            right (None or Node): The right child of the node.
        """
        self.value = value
        self.left = left
        self.right = right


def inorderTraversal(self, root):
    """Traverse a binary tree using inorder traversal.

    Attributes:
        root (Node): The root of the binary tree to traverse.
    Returns:
        An array of values representing the inorder traversal of the tree.
    """
    stack, output = [], []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif len(stack) != 0:
            current = stack.pop()
            output.append(current.val)
            current = current.right
        else:
            break

    return output


def minDepth(self, root):
    """Calculate the minimum depth of a binary search tree.

    Attributes:
        root (Node): The root of the binary search tree.
    """

    def helper(node, depth):
        if root is None:
            return depth
        if node.left is None and node.right is None:
            return depth + 1
        return min(helper(node.left, depth + 1), helper(node.right, depth + 1))

    return helper(root, 0)


def minDepth(self, root):
    """Calculate the maximum depth of a binary search tree.

    Attributes:
        root (Node): The root of the binary search tree.
    """

    def helper(node, depth):
        if root is None:
            return depth
        if node.left is None and node.right is None:
            return depth + 1
        return max(helper(node.left, depth + 1), helper(node.right, depth + 1))

    return helper(root, 0)


def isBalanced(self, root):
    """Determines if a binary search tree is balanced.

    Attributes:
        root (Node): The root of the binary search tree.
    Returns:
        Ture if the BST is balanced, False otherwise.
    """
    def getHeight(root, height):
        if root is None:
            return height
        return max(getHeight(root.left, height + 1),
            getHeight(root.right, height + 1))
        
        if root is None:
            return True
        return (abs(getHeight(root.left, 1) - getHeight(root.right, 1)) <= 1 and
            self.isBalanced(root.left) and self.isBalanced(root.right))

def deleteFromBST(t, queries):
    """Delete nodes from a binary search tree.

    Attributes:
        queries (array): An array of values to delete from the BST.
    """
    for value in queries:
        to_delete_parent = None
        to_delete = t
        while to_delete is not None and to_delete.value != value:
            to_delete_parent = to_delete
            if to_delete.value > value:
                to_delete = to_delete.left
            else:
                to_delete = to_delete.right
                
        if to_delete is not None:
            if to_delete.left is not None:
                to_swap_parent = to_delete.left
                to_swap = to_delete.left
                while to_swap.right is not None:
                    to_swap_parent = to_swap
                    to_swap = to_swap.right
                    
                if to_swap_parent == to_swap:
                    to_delete.left = to_swap.left
                else:
                    if to_swap.left is not None:
                        to_swap_parent.right = to_swap.left
                    else:
                        to_swap_parent.right = None
                to_delete.value = to_swap.value
                
            elif to_delete.right is not None:
                to_delete.value = to_delete.right.value
                to_delete.left = to_delete.right.left
                to_delete.right = to_delete.right.right
            
            elif to_delete_parent is not None:
                if to_delete_parent.left == to_delete:
                    to_delete_parent.left = None
                else:
                    to_delete_parent.right = None
                    
            else:
                t = None
                
    return t