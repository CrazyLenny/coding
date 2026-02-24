# This question treat the path together a number
#   4
# 1  2
# return 41 + 42 = 83

from basic_type import Node

def dfs(node: Node, cur_sum: int):
    # This is a safety check on empty tree.
    if node is None:
        return 0
    cur_sum = 10 * cur_sum + node.val
    # This code has specific logic on leaf nodes and other node.
    # It is problem specific.
    if not node.left and not node.right:
        return cur_sum
    return dfs(node.left, cur_sum) + dfs(node.right, cur_sum)

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(1, None, None)
    root.right = Node(2, None, None)
    result = dfs(root, 0)
    print(f"Expected result is 83, actual is {result}.")
