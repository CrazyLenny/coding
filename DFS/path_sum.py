# Simple Path Sum Program
#   2
# 1  5
# should return 8

from basic_type import Node

def dfs(node: Node):
    if node is None:
        return 0
    # Calculate current node
    if not node.left and not node.right:
        return node.val
    # Calculate the sum of left and right subtree
    return node.val + dfs(node.left) + dfs(node.right)

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4, None, Node(1))
    root.right = Node(8, Node(2), Node(3))
    result = dfs(root)
    print(f"The total sum is expected to be 23 and the actual value is: {result}")
