# Using DFS to perform topological sort.

def topological_sort(num_courses: int, prerequisites: list[list[int]]):
    # Construct the DAG w. adjacent list.
    adj = [[] for _ in range(num_courses)]
    for dest, src in prerequisites:
        adj[src].append(dest)
    # Status list, 0: unvisited, 1: visiting, 2: visited.
    visited = [0] * num_courses
    path = []

    def has_cycle(node: int):
        # Find a cycle.
        if visited[node] == 1:
            return True
        if visited[node] == 2:
            return False
        visited[node] = 1
        for neighbor in adj[node]:
            if has_cycle(neighbor):
                return True
        visited[node] = 2
        path.append(node)
    
    for course in range(num_courses):
        if has_cycle(course):
            return []
    return path[::-1]

if __name__ == "__main__":
    num_courses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]

    path = topological_sort(num_courses, prerequisites)
    print(f"The path is expected to be 0->1->2->3 to finish is: {path}")

    num_courses = 4
    prerequisites = [[1, 0], [3, 0], [1, 3], [2, 1]]

    path = topological_sort(num_courses, prerequisites)
    print(f"The path is expected to be 0->3->1->2 to finish is: {path}")
