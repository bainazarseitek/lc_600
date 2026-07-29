class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        last1, last2 = -1,-1
        res=float('inf')
        for i, n in enumerate(nums):
            if n == 1:
                last1 = i
                if last2 != -1:
                    res=min(res, abs(last2-last1))
            if n == 2:
                last2 = i
                if last1 != -1:
                    res=min(res, abs(last2-last1))
        return -1 if res == float('inf') else res
                    
            
        