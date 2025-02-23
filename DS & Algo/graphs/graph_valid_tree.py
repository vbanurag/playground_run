'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.


Input:
    n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true



'''


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True
        
        adj = {i: [] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0,-1) and n == len(visit)
        