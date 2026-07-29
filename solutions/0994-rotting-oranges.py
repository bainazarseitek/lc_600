class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        directions=[[1,0], [-1, 0], [0, 1], [0,-1]]
        q=deque()
        ROWS, COLS = len(grid),  len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append([r,c])
        while q and fresh>0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r = r+dr
                    new_c= c+dc
                    if 0<=new_r<ROWS and 0<=new_c<COLS and grid[new_r][new_c]==1:
                        grid[new_r][new_c]=2
                        q.append([new_r,new_c])
                        fresh-=1
            time+=1
        return time if fresh == 0 else -1
                    

            
        