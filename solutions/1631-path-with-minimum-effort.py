class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0,1], [0,-1], [1, 0], [-1,0]]
        minHeap = [[0, 0, 0]] # [diff, r, c]
        visit= set()
        while minHeap:
            diff, r, c  = heapq.heappop(minHeap)
            if (r,c) in visit: continue
            visit.add((r,c))
            if (r,c) == (ROWS-1, COLS-1):
                return diff
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if (new_r < 0 or new_c < 0 or 
                    new_r == ROWS or new_c == COLS or (new_r, new_c) in visit):
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[new_r][new_c])) 
                heapq.heappush(minHeap, (newDiff, new_r, new_c))
            



            


                
        