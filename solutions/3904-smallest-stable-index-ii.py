class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        maxpref=[0] * n
        minpref = [0] * n
        maxpref[0]=nums[0]
        for i in range(1, n):
            maxpref[i]=max(nums[i], maxpref[i-1])
        minpref[n-1]=nums[n-1]
        for i in range(n-2, -1, -1):
            minpref[i]=min(nums[i], minpref[i+1])
        for i in range(n):
            val=maxpref[i]-minpref[i]
            if val <=k:
                return i
        return -1
        
        