class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS=len(matrix), len(matrix[0])
        l, r = 0, COLS-1
        for i in range(ROWS):
            if matrix[i][l]<=target and matrix[i][r]>=target: 
                while l<=r:
                    m=(l+r)//2
                    if matrix[i][m]<target:
                        l=m+1
                    elif matrix[i][m]>target:
                        r-=1
                    else:
                        return True
                    
            else:
                continue
        return False
                # m=(l+r)//2
                # if matrix[i][m]>target:

                # elif matrix[i][m]<target:
                #     continue


        