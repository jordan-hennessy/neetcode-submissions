class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands = 0

        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if (i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == '0'):
                return
            
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    continue
                else:
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands
                
