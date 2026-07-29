class Solution:
        def permuteUnique(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            perms=[[]]
            for n in nums:
                nextPerms= []
                for p in perms: 
                    for i in range(len(p)+1):
                        pCopy = p.copy()
                        pCopy.insert(i, n)
                        nextPerms.append(pCopy)
                
                        if i<len(p) and p[i] == n:
                            break
                perms = nextPerms
            return perms 
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()           
    #     return self.helper(0, nums)
        
    # def helper(self, i, nums):
    #     if i == len(nums):
    #         return [[]]
    #     resPerm=[]
    #     perm = self.helper(i+1, nums)
    #     for p in perm:
    #         for j in range(len(p)+1):
    #             pCopy=p.copy()
    #             pCopy.insert(j, nums[i])
    #             resPerm.append(pCopy)

                
    #             if j < len(p) and nums[i] == p[j]:
    #                 break
    #     return resPerm