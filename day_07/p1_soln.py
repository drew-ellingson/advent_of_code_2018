
with open('input.txt') as input_file:
    deps = [dep.strip() for dep in input_file.readlines()]

deps = [list(dep.replace('Step ', '') \
                .replace(' must be finished before step ', '') \
                .replace(' can begin.', '')) for dep in deps]

dist_nodes = list(set(''.join([''.join(dep) for dep in deps])))

def get_upstream_nodes(node):
    return [edge[0] for edge in list(filter(lambda x: x[1] == node, deps))]

graph = {
    node: get_upstream_nodes(node)
    for node in dist_nodes
}

node_order = []

def get_next_node(graph):
    no_deps = filter(lambda x: len(graph[x]) == 0, graph.keys())
    return min(no_deps)

def do_one_step(graph):
    now_node = get_next_node(graph)
    node_order.append(now_node)
    graph.pop(now_node)
    for node in graph.keys():
        graph[node] = list(filter(lambda x: x != now_node, graph[node]))
    return graph

while len(graph.keys()) > 0:
    graph = do_one_step(graph)

print(f'P1 Answer: {"".join(node_order)}')


