from collections import deque
from map import *

def BreadthFirstSearch(start, target):
	print(start, target)
	if start not in adjacency_list or target not in adjacency_list:
		return None  # One or both nodes not in the graph

	queue = deque([start])
	visited = set([start])

	while queue:
		current = queue.popleft()

		# Check if we've reached the target node
		if current == target:
			return True  # Target node found

		# Explore neighbours
		for neighbour in adjacency_list[current]:
			if territory_owned[neighbour][0] == player1:
				if neighbour not in visited:
					visited.add(neighbour)
					queue.append(neighbour)

	return False