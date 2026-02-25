# Program that detect cycle in undirected graph

from basic_type import GraphNode

def has_cycle(nodes: list[GraphNode]) -> bool:
# When exploring, found a node that is already visited,
# and not the parent node -> has cycle.
    visited = set()
    def dfs(node: GraphNode, parent: GraphNode) -> bool:
        visited.add(node)
        # Traverse its neighbor.
        for neighbor in node.neighbors:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True
            # Continue the traversal, and pass down parent.
            if dfs(neighbor, node):
                return True
        return False

    for node in nodes:
        if node not in visited:
            if dfs(node, None):
                return True

    return False

if __name__ == "__main__":
    root = GraphNode(1)
    node_0 = GraphNode(2)
    node_1 = GraphNode(3)
    # Connect the edges
    root.neighbors.append(node_0)
    node_0.neighbors.append(root)

    node_0.neighbors.append(node_1)
    node_1.neighbors.append(node_0)

    root.neighbors.append(node_1)
    node_1.neighbors.append(root)

    result = has_cycle([root])
    print(f"The graph has cycle, and the output is {result}.")
