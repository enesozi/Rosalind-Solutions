import sys

class Graph:
    def __init__(self,N):
        self.__adj_list = {node:[] for node in range(1,N+1)}

    def add_edge_with_weight(self, u, v):
        self.__adj_list[u].append(v)
        self.__adj_list[v].append(u)

    def get_graph(self):
    	return self.__adj_list


def dfs_util(node,visited,graph):
	stack = []
	stack.append(node)

	while stack:
		elm = stack.pop()
		if not visited[elm]:
			visited[elm] = True

		for neighbour in graph[elm]:
			if not visited[neighbour]:
				stack.append(neighbour)	

def dfs(graph):
	N = len(graph)
	visited = [False] * (N+1)
	cc = 0
	for i in range(1,N+1):
		if not visited[i]:
			dfs_util(i,visited,graph)
			cc += 1

	print(cc)		



def main(args):
	file = str(args[1])
	with open(file) as f:
		N,E = map(int,f.readline().split())
		g = Graph(N)
		while True:
			line = f.readline() 
			if not line:
				break

			u,v = map(int,line.split())
			g.add_edge_with_weight(u,v)
	graph = g.get_graph()

	dfs(graph)

if '__main()__':
	main(sys.argv)					