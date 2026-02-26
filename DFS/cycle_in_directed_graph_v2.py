# The program that detects cycle in directed graph.

from basic_type import GraphNode

class DirectedGraphNode(GraphNode):
    def __init__(self, val: int, color: int = 0):
        super().__init__(val)
        self.color = color


def has_cycle(nodes: list[DirectedGraphNode]) -> bool:
    # Coloring:
    # 0 - unvisited
    # 1 - exploring
    # 2 - finished
    # If found a node that is in the exploring state
    # -> found cycle.
    def dfs(node: DirectedGraphNode) -> bool:
        # Cycle Found
        if node.color == 1:
            return True
        # the node has been examined and its connnetion is safe.
        if node.color == 2:
            return False
        node.color = 1
        for neighbor in node.neighbors:
            # If any neighbor has cycle, then has cycle.
            if dfs(neighbor):
                return True
        node.color = 2
        return False

    for node in nodes:
        if node.color == 0:
            if dfs(node):
                return True
    return False

if __name__ == "__main__":
    # Construct a directed graph
    root = DirectedGraphNode(1)
    node_0 = DirectedGraphNode(2)
    node_1 = DirectedGraphNode(3)

    # Connect the edges
    root.neighbors.append(node_0)
    node_0.neighbors.append(node_1)
    node_1.neighbors.append(root)

    result = has_cycle([root])
    print(f"This graph has cycle and the output is: {result}")
    # Construct a directed graph
    root = DirectedGraphNode(1)
    node_0 = DirectedGraphNode(2)
    node_1 = DirectedGraphNode(3)

    # Connect the edges
    root.neighbors.append(node_0)
    node_0.neighbors.append(node_1)

    result = has_cycle([root])
    print(f"This graph has no cycle and the output is: {result}")
