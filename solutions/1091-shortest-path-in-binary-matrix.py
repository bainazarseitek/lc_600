class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))
        lenth = 1
        directions = [
            [0,1], [0,-1], [1,0], [-1,0],
            [1,1], [1,-1], [-1,1], [-1,-1] ]

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS-1 and c  == COLS -1:
                    return lenth
                for dr,dc in directions:
                    new_row = r + dr
                    new_col = c + dc
                    if (min(new_row, new_col) < 0 or new_col >= COLS or new_row >= ROWS or (new_row, new_col) in visit or grid[new_row][new_col] == 1):
                        continue
                    queue.append((new_row,new_col))
                    visit.add((new_row,new_col))
            lenth +=1
        return -1



        