def dfs_rec(graph):
    def _dfs(vertex):
        is_vertex_checked[vertex] = True
        vertex_depth[vertex] = current_depth[0]
        current_depth[0] += 1
        for descendant in graph[vertex]:
            if not is_vertex_checked[descendant]:
                _dfs(descendant)
        forward_depth[vertex] = current_depth[0]
        current_depth[0] += 1

    current_depth = [1]
    is_vertex_checked = [False for i in range(len(graph))]
    vertex_depth = [0 for i in range(len(graph))]
    forward_depth = [0 for i in range(len(graph))]
    for current_vertex in range(len(graph)):
        if not is_vertex_checked[current_vertex]:
            _dfs(current_vertex)
    print(vertex_depth)
    print(forward_depth)


dfs_rec([[1], [0, 2, 5], [1, 4, 5, 6], [5, 7], [], [1], [4, 7], [6]])
