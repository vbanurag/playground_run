'''
Count Number of Islands

Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. 
You may assume water is surrounding the grid (i.e., all the edges are water).

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

Output: 1
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        island = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == '0'
                or (r,c) in visit
            ):
                return
            
            visit.add((r,c))
            directions = [[0,1], [0,-1], [1,0],[-1,0]]

            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    island +=1
                    dfs(r,c)
        return island
        