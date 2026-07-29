class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]
        visit = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r==ROWS or c == COLS or board[r][c] != "O" or (r,c) in visit:
                return
            visit.add((r,c))
            board[r][c] = "t"
            for dr, dc in directions:
                new_r = r+dr
                new_c = c+dc
                dfs(new_r, new_c)


        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "t":
                    board[r][c] = "O"