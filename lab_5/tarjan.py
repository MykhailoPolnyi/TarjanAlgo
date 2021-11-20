def tarjan(graph: list):
    if type(graph) != list:
        raise ValueError("Wrong graph_to_reverse interpretation provided, expected: list")

    def count_order(vertex):
        is_vertex_checked[vertex] = True
        current_order[0] += 1
        for descendant in graph[vertex]:
            if not is_vertex_checked[descendant]:
                count_order(descendant)
        forward_order[vertex] = current_order[0]
        current_order[0] += 1

    def dfs(checked_graph, entry_point):
        def _dfs(vertex):
            is_vertex_checked[vertex] = True
            result.append(vertex)
            for descendant in checked_graph[vertex]:
                if not is_vertex_checked[descendant]:
                    _dfs(descendant)

        result = []
        _dfs(entry_point)
        return result

    def reverse_graph(graph_to_reverse):
        result_graph = [[] for i in graph_to_reverse]
        for i, l in enumerate(graph_to_reverse):
            for x in l:
                result_graph[x].append(i)
        return result_graph

    current_order = [1]
    connected_components = []
    is_vertex_checked = {i: False for i in range(len(graph))}
    forward_order = {i: 0 for i in range(len(graph))}
    for current_vertex in range(len(graph)):
        if not is_vertex_checked[current_vertex]:
            count_order(current_vertex)

    revered_graph = reverse_graph(graph)
    is_vertex_checked = {i: False for i in range(len(graph))}
    while len(forward_order) != 0:
        search_start = max(forward_order, key=lambda key: forward_order[key])
        if not is_vertex_checked[search_start]:
            connected_components.append(dfs(revered_graph, search_start))
        forward_order.pop(search_start)
    return connected_components


