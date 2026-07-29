class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r =0, len(nums)-1
        res=nums[l]
        while l<=r:
            m=(l+r)//2
            if nums[m]>=nums[l]:
                res=min(nums[l], res)
                l=m+1
            else:
                r=m-1
                res=min(nums[m], res)
        return res
                
