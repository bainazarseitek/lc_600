class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
                
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows,columns = len(grid), len(grid[0])
        visit = set()
        area =0

        def dfs(r,c):
            if (r < 0 or c < 0 or r>=rows or c >= columns or (r, c) in visit or grid[r][c]==0 ):
                return 0
            visit.add((r,c))
            res =1
            for dr, dc in directions:
                res += dfs(r+dr, c+dc)
            return res


        for r in range(rows):
            for c in range(columns):
                area = max(area, dfs(r, c))
        return area
        