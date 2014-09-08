"""Homework 2"""


def bfs_distance(graph, node):
    """BFS distance"""
    queue = []
    d_graph = {}
    queue.append(node)
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in d_graph:
                d_graph[neighbor] = d_graph.get(node, 0) + 1
                queue.append(neighbor)
    return d_graph


def cc_distance(graph):
    """CC distance"""
    remaining_nodes = list(graph.keys())
    components = set()
    while remaining_nodes:
        arbitrary_node = remaining_nodes[0]
        distance = bfs_distance(graph, arbitrary_node)
        to_be_cced = set()
        for remaining_node in remaining_nodes:
            if remaining_node in distance:
                to_be_cced.add(remaining_node)
        components = components | to_be_cced
        remaining_nodes = list(set(remaining_nodes) - {arbitrary_node})
    return components


def bfs_visited(graph, node):
    """BFS visited"""
    queue = [node]
    visited = {node}
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def cc_visited(graph):
    """CC visited"""
    remaining_nodes = list(graph.keys())
    components = []
    while remaining_nodes:
        node = remaining_nodes[0]
        component = bfs_visited(graph, node)
        if component not in components:
            components.append(component)
        remaining_nodes = list(set(remaining_nodes) - {node})
    return components


def largest_cc_size(graph):
    """Largest CC size"""
    ccs = cc_visited(graph)
    if not ccs:
        return 0
    return max(len(x) for x in ccs)


def compute_resilience(graph, attack_order):
    """Resilience"""
    graph = graph.copy()
    resilience = [largest_cc_size(graph)]
    for node in attack_order:
        del graph[node]
        for node2, neighbors in graph.iteritems():
            if node in neighbors:
                graph[node2] = {x for x in neighbors if x != node}
        resilience.append(largest_cc_size(graph))
    return resilience
