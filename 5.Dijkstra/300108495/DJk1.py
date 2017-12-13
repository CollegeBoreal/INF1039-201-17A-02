graph = {}
graph["a"]={}
graph["a"]["fin"]={}
graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5
graph["fin"]={}

infinity = float("inf")
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node= None
    for node in costs:
        cost=costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node
def node(costs):
    node=find_lowest_cost_node(costs)
    while node is not None:
        cost=costs[node]
        neighbors=graph[node]
        for n in neighbors.keys() :
            new_cost = cost + neighbors[n]
            if costs[n]>new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node=find_lowest_cost_node(costs)


print ("Cost from the start to each node:")
print costs


