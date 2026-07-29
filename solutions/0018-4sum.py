class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]

        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            new_target=target-a
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l, r = j+1, len(nums)-1
                while l<r:
                    threeSum=nums[j]+nums[l]+nums[r]
                    if threeSum < new_target:
                        l+=1
                    elif threeSum > new_target:
                        r-=1
                    else:
                        res.append([a, nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
        return res

                



        