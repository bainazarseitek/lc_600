class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        res=[[set() for c in range(cols)] for r in range(rows)]
        res[0][0].add(grid[0][0])
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                     continue
                curr = set()
                if r>0:
                    for n in res[r-1][c]:
                        curr.add(n ^ grid[r][c])
                if c>0:
                    for n in res[r][c-1]:
                        curr.add(n ^ grid[r][c])
                res[r][c]=curr
        return min(res[rows-1][cols-1])
                