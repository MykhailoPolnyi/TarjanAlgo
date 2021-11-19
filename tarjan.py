def dfs(graph: list):
    container = []
    is_vertex_checked = [False for i in graph]
    vertex_depth = [0 for i in graph]
    forward_depth = [0 for i in graph]
    curr_depth = 1
    for vertex in range(len(graph)):
        if not is_vertex_checked[vertex]:
            container.append(vertex)
            while len(container) != 0:
                current_vertex = container.pop()
                print(f"{'    '*curr_depth}Searching in {current_vertex}")
                if not is_vertex_checked[current_vertex]:
                    is_vertex_checked[current_vertex] = True
                    vertex_depth[current_vertex] = curr_depth
                    for descendant in reversed(graph[current_vertex]):
                        container.append(descendant)
                    print(f"{'    '*curr_depth}Ended search in {current_vertex}\n")
                    curr_depth += 1
                else:
                    print(f"{'    '*curr_depth}Already searched in {current_vertex}\n")
    print(vertex_depth)
    print(forward_depth)


dfs([[1], [0, 2, 5], [1, 4, 5, 6], [5, 7], [], [1], [4, 7], [6]])
