'''

Max Area of Island


You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. Y
ou may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.

Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6


Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c):
            if(
                r < 0
                or r == rows
                or c == cols
                or c < 0
                or grid[r][c] == 0
                or (r,c) in visit
            ):
                return 0
            
            visit.add((r,c))
            return 1+ dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        return area
        