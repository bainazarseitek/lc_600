class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]

        for n in nums:
            nextPerms = []
            for p in perms:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i,n)
                    nextPerms.append(pCopy)
            perms = nextPerms
        return perms
            #     return self.helper(0, nums)

    
    # def helper(self, i, nums):
    #     if i == len(nums):
    #         return [[]]
    #     resPerms=[]
    #     perm = self.helper(i+1, nums)
    #     for p in perm:
    #         for j in range(len(p)+1):
    #             pCopy = p.copy()
    #             pCopy.insert(j, nums[i])
    #             resPerms.append(pCopy)

    #     return resPerms

        