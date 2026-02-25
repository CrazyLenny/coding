# Class for a simple binary tree node
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

