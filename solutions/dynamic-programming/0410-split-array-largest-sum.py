class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums), sum(nums)
        res=r
        def isSplit(largest):
            subarray=0
            curSum=0
            for n in nums:
                curSum+=n
                if curSum>largest:
                    curSum=n
                    subarray+=1
            return subarray+1<=k

        while l<=r:
            m=(r+l)//2
            if isSplit(m):
                r=m-1
                res=m
            else:
                l=m+1
        return res

        
        