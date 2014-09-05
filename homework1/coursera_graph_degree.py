"""Project 1 - Degree distributions for graphs"""


class GroupBy(object):
    """A copypaste from itertools because copyowl refuses to import it"""
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self._keyfunc = key
        self._iterable = iter(iterable)
        self._tgtkey = self._currkey = self._currvalue = object()

    def __iter__(self):
        return self

    def next(self):
        """A thing that is executed on every iteration"""
        while self._currkey == self._tgtkey:
            self._currvalue = next(self._iterable)    # Exit on StopIteration
            self._currkey = self._keyfunc(self._currvalue)
        self._tgtkey = self._currkey
        return (self._currkey, self._grouper(self._tgtkey))

    def _grouper(self, tgtkey):
        """A thing that groups values by keys"""
        while self._currkey == tgtkey:
            yield self._currvalue
            self._currvalue = next(self._iterable)    # Exit on StopIteration
            self._currkey = self._keyfunc(self._currvalue)

    def make_pylint_happy(self):
        """A good class is a class that has more than one public method. So be it ;-)"""
        pass



EX_GRAPH0 = {
    0: {1, 2},
    1: set(),
    2: set(),
}


EX_GRAPH1 = {
    0: {1, 4, 5},
    1: {2, 6},
    2: {3},
    3: {0},
    4: {1},
    5: {2},
    6: set(),
}


EX_GRAPH2 = {
    0: {1, 4, 5},
    1: {2, 6},
    2: {3, 7},
    3: {7},
    4: {1},
    5: {2},
    6: set(),
    7: {3},
    8: {1, 2},
    9: {0, 3, 4, 5, 6, 7},
}


def make_complete_graph(num_nodes):
    """Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed
    graph with the specified number of nodes"""
    graph = {}
    for node1 in range(0, num_nodes):
        graph[node1] = set()
        for node2 in range(0, num_nodes):
            if node1 == node2:
                continue
            graph[node1].add(node2)
    return graph


def compute_in_degrees(digraph):
    """Takes a directed graph digraph (represented as a dictionary)
    and computes the in-degrees for the nodes in the graph"""
    graph = {}
    for node1 in digraph:
        graph[node1] = 0
    for node2, out_nodes2 in digraph.iteritems():
        if node1 == node2:
            continue
        if node1 in out_nodes2:
            graph[node1] += 1
    return graph


def in_degree_distribution(digraph):
    """Takes a directed graph digraph (represented as a dictionary)
    and computes the unnormalized distribution of the in-degrees of the graph"""
    digraph = compute_in_degrees(digraph)
    key = lambda x: x[1]
    distribution = {}
    for key, group in GroupBy(sorted(digraph.items(), key=key), key=key):
        group = list(group)
        if group:
            distribution[key] = len(group)
    return distribution
