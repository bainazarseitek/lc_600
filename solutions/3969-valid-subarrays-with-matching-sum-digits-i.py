class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        res=0
        for l in range(len(nums)):
            curSum = 0
            for r in range(l,len(nums)):
                curSum += nums[r]
                if curSum % 10 ==x and int(str(curSum)[0])== x:
                    res+=1
        return res
                

        