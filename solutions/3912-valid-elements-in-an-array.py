class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        res=[]
        n=len(nums)
        suffix=[float("-inf")]*n
        for i in range(n-2, -1, -1):
            suffix[i]=max(nums[i+1], suffix[i+1])
        for i in range(len(nums)):
            if i == 0 or i == n-1:
                res.append(nums[i])
                continue
            elif nums[i]>res[-1]:
                res.append(nums[i])
            elif nums[i]>suffix[i]:
                res.append(nums[i])
                
            
        return res
        