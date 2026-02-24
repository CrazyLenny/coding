# Find the path that sum up to target

from basic_type import Node

def dfs(node: Node, target: int, cur_list: list, res: list):
    # Reach the bottom but not found. 
    if node is None:
        return
    # Always record the path.
    cur_list.append(node.val)
    target = target - node.val
    # Reach leave node and found the path.
    if not node.left and not node.right and target == 0:
        res.append(list(cur_list))
    # Regular case, continue the traverse.
    dfs(node.left, target, cur_list, res)
    dfs(node.right, target, cur_list, res)
    # BACKTRACK: Need to remove current node before return
    cur_list.pop()
        
if __name__ == "__main__":
    target = 10
    root = Node(3)
    root.left = Node(4, Node(3), Node(2))
    root.right = Node(7, None, None)
    cur_list = []
    res = []
    dfs(root, target, cur_list, res)
    print(f"The expected sum of each sub-list is {target}, the list is {res}.")
