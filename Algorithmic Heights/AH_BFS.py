import sys
from collections import defaultdict

class Graph:
 
	def __init__(self,max_node_val): 
		self.graph =  {node:[] for node in range(1,max_node_val+1)}

	def add_edge(self,u,v):
		self.graph[u].append(v)
 
	def BFS(self, start, end):

		dist = [-1000] * (len(self.graph)+1)

		queue = []

		queue.append(start)
		dist[start] = 0

		found = False
		
		while queue:

			c_node = queue.pop(0)
			
			if c_node == end:
				found = True
				break		

			for node in self.graph[c_node]:
				if dist[node] == -1000:
					dist[node] = dist[c_node] + 1
					queue.append(node)
					
		if found:
			return dist[end]
		return -1	            
	


def main(args):
	file = str(args[1])
	with open(file) as f:
		N,E = list(map(int,f.readline().split()))
		g = Graph(N)
		while True:
			line = f.readline() 
			if not line:
				break

			u,v = list(map(int,line.split()))
			g.add_edge(u,v)

	start = 1		
	for node in range(1,N+1):
		steps = g.BFS(start,node)
		print(steps, end=" ")

if '__main()__':
	main(sys.argv)	