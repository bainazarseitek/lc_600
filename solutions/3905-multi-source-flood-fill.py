class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        sources.sort(key = lambda x: -x[2])
        grid = [[0]*m for i in range(n)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for r,c,v in sources:
            grid[r][c] = v
        for r,c,v in sources:
            for dr, dc in directions:
                new_r  = r+dr
                new_c = c+dc
                if 0<=new_r<n and 0<=new_c<m and grid[new_r][new_c]==0:
                    grid[new_r][new_c]=v
                    sources.append([new_r, new_c, v])
        return grid



        




                    
            
                
        