# -*- coding: utf-8 -*-
"""22 assignment ppt

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OpvDJjIL-hGtgIY0ozhhFZ2mMWwsi6HQ
"""

#1solution

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binary_tree_to_dll(root):
    if not root:
        return None

    def inorder_traversal(node):
        nonlocal prev, head
        if not node:
            return

        inorder_traversal(node.left)

        # If head is None, it means this is the leftmost node (smallest value) of the tree
        if not head:
            head = node

        # Modify pointers to convert the current node to a DLL node
        node.left = prev
        if prev:
            prev.right = node

        prev = node

        inorder_traversal(node.right)

    prev = None  # to keep track of the previously visited node during in-order traversal
    head = None  # to store the head of the DLL

    inorder_traversal(root)
    return head

# Helper function to print the Doubly Linked List
def print_dll(head):
    current = head
    while current:
        print(current.val, end=" <-> ")
        current = current.right
    print("None")

# Test the code
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    # Convert the binary tree to a doubly linked list (DLL)
    dll_head = binary_tree_to_dll(root)

    # Print the DLL in the specified order
    print("Doubly Linked List (DLL) in in-order:")
    print_dll(dll_head)

#2 solution

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def flip_binary_tree(root):
    if not root:
        return None

    # Base case: If it's a leaf node, return itself
    if not root.left and not root.right:
        return root

    # Recursively flip the left and right subtrees
    flipped_left = flip_binary_tree(root.left)
    flipped_right = flip_binary_tree(root.right)

    # Flip the current node's left and right children
    root.left = flipped_right
    root.right = flipped_left

    return root

# Helper function to print the tree in in-order traversal
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val, end=" ")
        print_inorder(root.right)

# Test the code
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Print the original tree
    print("Original Tree (In-order):")
    print_inorder(root)
    print()

    # Flip the binary tree
    flipped_root = flip_binary_tree(root)

    # Print the flipped tree
    print("Flipped Tree (In-order):")
    print_inorder(flipped_root)
    print()

#3 solution

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_root_to_leaf_paths(root):
    if not root:
        return

    stack = [(root, str(root.val))]

    while stack:
        node, path = stack.pop()

        if not node.left and not node.right:
            # Leaf node reached, print the path from root to this leaf node
            print(path)

        if node.right:
            stack.append((node.right, path + " -> " + str(node.right.val)))

        if node.left:
            stack.append((node.left, path + " -> " + str(node.left.val)))

# Test the code
if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(6)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Print all root-to-leaf paths
    print("Root-to-leaf paths:")
    print_root_to_leaf_paths(root)

#4solution

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_from_pre_in(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)
    root_idx_inorder = inorder.index(root_val)

    root.left = build_tree_from_pre_in(preorder[1:1 + root_idx_inorder], inorder[:root_idx_inorder])
    root.right = build_tree_from_pre_in(preorder[1 + root_idx_inorder:], inorder[root_idx_inorder + 1:])

    return root

def build_tree_from_post_in(postorder, inorder):
    if not postorder or not inorder:
        return None

    root_val = postorder[-1]
    root = TreeNode(root_val)

    root_idx_inorder = inorder.index(root_val)

    root.left = build_tree_from_post_in(postorder[:root_idx_inorder], inorder[:root_idx_inorder])
    root.right = build_tree_from_post_in(postorder[root_idx_inorder:-1], inorder[root_idx_inorder + 1:])

    return root

def is_same_tree(preorder, inorder, postorder):

    root_pre_in = build_tree_from_pre_in(preorder, inorder)


    root_post_in = build_tree_from_post_in(postorder, inorder)


    return are_trees_equal(root_pre_in, root_post_in)

def are_trees_equal(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False

    return (root1.val == root2.val and
            are_trees_equal(root1.left, root2.left) and
            are_trees_equal(root1.right, root2.right))


if __name__ == "__main__":
    inorder = [4, 2, 5, 1, 3]
    preorder = [1, 2, 4, 5, 3]
    postorder = [4, 5, 2, 3, 1]
    print(is_same_tree(preorder, inorder, postorder))

    inorder = [4, 2, 5, 1, 3]
    preorder = [1, 5, 4, 2, 3]
    postorder = [4, 1, 2, 3, 5]
    print(is_same_tree(preorder, inorder, postorder))

