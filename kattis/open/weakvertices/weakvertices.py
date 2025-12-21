while True:
	graph = {}

	n = int(input())
	if n == -1:
		break
	for i in range(n):
		graph[i] = [int(j) for j in input().split()]


	weak = []
	for i in range(n):
		vertices_amount = graph[i].count(1)
		if vertices_amount < 2:
			weak.append(i)

		else:

			edges = []
			for index,possible_edge in enumerate(graph[i]):
				if possible_edge:
					edges.append(index)
			is_weak = True
			for first in edges:
				for second in edges:
					if graph[first][second] == 1:
						is_weak = False
						break
				if not is_weak:
					break
			if is_weak:
				weak.append(i)
	print(*weak)
