def tarjan(graph):
    if type(graph) != list:
        raise (ValueError(f"Expected graph presentation, expected: list, got: {type(graph)}"))

    def find_scc(entry_vertex):
        index_of[entry_vertex] = index[0]
        lowest_reached[entry_vertex] = index[0]
        index[0] += 1
        stack.append(entry_vertex)

        for successor in graph[entry_vertex]:
            if index_of[successor] is None:
                find_scc(successor)
                lowest_reached[entry_vertex] = min(lowest_reached[entry_vertex], lowest_reached[successor])
            elif successor in stack:
                lowest_reached[entry_vertex] = min(lowest_reached[entry_vertex], index_of[successor])

        if lowest_reached[entry_vertex] == index_of[entry_vertex]:
            result = []
            scc_component = stack.pop()
            result.append(scc_component)
            while scc_component != entry_vertex:
                scc_component = stack.pop()
                result.append(scc_component)
            sc_components_list.append(result)

    index = [0]
    stack = []
    graph_range = range(len(graph))
    index_of = {i: None for i in graph_range}
    lowest_reached = {}
    sc_components_list = []
    for vertex in graph_range:
        if index_of[vertex] is None:
            find_scc(vertex)
    return sc_components_list
