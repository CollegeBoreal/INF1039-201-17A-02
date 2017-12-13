graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("infinity")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = "none"

processed = []

def node(costs):
	node = find_lowest_cost_node(costs)
	while node is not None:
		cost = costs[node]
		neighbors = graph[node]
		for n in neighbors.key():
			new_cost = cost + neighbors[n]
			if costs[n] > new_cost:
				costs[n] = node
		processed.append(node)
		node = find_lowest_cost_node(costs)

def find_lowest_cost_node():
	lowest_cost = float("inf")
	lowest_cost_node = 0
	for node in costs:
		cost = cost[node]

	if cost < lowest_cost and node not in processed:
		lowest_cost = cost
		lowest_cost_node = node
	return lowest_cost_node



print("Costs from the start to each node:")
print(costs)

