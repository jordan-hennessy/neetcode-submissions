class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific, atlantic = set(), set()

        m, n = len(heights), len(heights[0])

        def dfs(i: int, j: int, prev: int, ocean: set):
            if i < 0 or j < 0 or i >= m or j >= n or prev > heights[i][j] or (i, j) in ocean:
                return
            else:
                ocean.add((i, j))
                
                dfs(i + 1, j, heights[i][j], ocean)
                dfs(i - 1, j, heights[i][j], ocean)
                dfs(i, j + 1, heights[i][j], ocean)
                dfs(i, j - 1, heights[i][j], ocean)

        lr, lc = m - 1, n - 1

        for i in range(m):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, lc, heights[i][lc], atlantic)

        for j in range(n):
            dfs(0, j, heights[0][j], pacific)
            dfs(lr, j, heights[lr][j], atlantic)

        return list(pacific.intersection(atlantic))