'''

There is an undirected graph with n nodes. 
There is also an edges array, where edges[i] = [a, b] means t
hat there is an edge between node a and node b in the graph.

Return the total number of connected components in that graph.

Input:
    n=3
edges=[[0,1], [0,2]]

Output:
1


'''

class UnionFind:
    def __init__(self):
        self.f = {}
    
    def findParent(self, x):
        y = self.f.get(x,x)
        if x!=y:
            y = self.f[x] = self.findParent(y)
        return y
    
    def union(self, x, y):
        self.f[self.findParent(x)] = self.findParent(y)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a, b in edges:
            dsu.union(a,b)
        
        return len(set(dsu.findParent(x) for x in range(n)))
        