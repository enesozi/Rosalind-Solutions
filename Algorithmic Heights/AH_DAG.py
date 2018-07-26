import sys
from enum import Enum

class Color(Enum):
	WHITE = 0
	GRAY = 1
	BLACK = 2


class Graph:
    def __init__(self,N):
        self.__adj_list = {node:[] for node in range(1,N+1)}

    def add_edge(self, u, v):
        self.__adj_list[u].append(v)

    def get_graph(self):
    	return self.__adj_list


def dfs_util(node,colors,graph):
	colors[node] = Color.GRAY

	for neighbour in graph[node]:
		if colors[neighbour] == Color.GRAY:
			return True

		if colors[neighbour] == Color.WHITE and dfs_util(neighbour,colors,graph):
			return True	

	colors[node] = Color.BLACK
	return False		

def is_acyclic(graph):
	N = len(graph)
	colors = [Color.WHITE] * (N+1)
	for i in range(1,N+1):
		if colors[i] == Color.WHITE:
			if(dfs_util(i,colors,graph)):
				return -1
	return 1	


def main(args):
	file = str(args[1])
	with open(file) as f:
		k = int(f.readline())
		for i in range(k):
			f.readline()
			N,E = map(int,f.readline().split())		
			g = Graph(N)
			for j in range(E):
				u,v = map(int,f.readline().split())
				g.add_edge(u,v)
			graph = g.get_graph()

			print(is_acyclic(graph), end=" ")

if '__main()__':
	main(sys.argv)		