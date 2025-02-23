'''

You are given a 2-D matrix grid. Each cell can have one of three possible values:
    
0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every second, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, 
then the fresh fruit also becomes rotten.

Return the minimum number of seconds that must elapse until there are zero fresh fruits remaining.
If this state is impossible within the grid, return -1.

Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4

'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()

                for dr,dc in dirs:
                    row, col = r+dr, c+dc

                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1
        return time if fresh==0 else -1

        