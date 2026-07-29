class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        minHeap = [(grid[0][0],0,0)]
        visit = set()
        visit.add((0,0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == n-1 and c == n-1:
                return t
            for dr, dc in directions:
                new_r = r+dr
                new_c= c+dc
                if 0<=new_r<n and 0<=new_c<n and (new_r, new_c) not in visit:
                    visit.add((new_r, new_c))
                    heapq.heappush(minHeap, (max(t, grid[new_r][new_c]),new_r, new_c))
        