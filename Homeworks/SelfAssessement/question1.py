from collections import deque

def bfs_traversal(graph, initial_node):
    # your implementation here
    # your function will return a list!
    l = []
    visited = set()
    d = deque()
    d.append(initial_node)
    visited.add(initial_node)

    while d: # using bfs to print out the transversal
        curr_node = d.popleft()
        l.append(curr_node)
        for neighbor in graph[curr_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                d.append(neighbor)

    return l

if __name__ == "__main__":
    # test case 1
    print(bfs_traversal({"+": ["*",3], "*":[2,7], 2:[],7:[],3:[]}, "+"))

    # test case 2
    print(bfs_traversal({0: [1,3], 1:[2,3], 2:[3,1], 3:[0,1]}, 0))