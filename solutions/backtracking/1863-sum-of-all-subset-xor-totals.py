class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0
        curSet = []
        self.helper(0, nums, curSet)
        return self.total

    def helper(self, i,nums, curSet):
        if i == len(nums):
            set_sum=0
            for n in curSet:
                set_sum = set_sum ^ n
            self.total+=set_sum
            return


        #add it
        curSet.append(nums[i])
        self.helper(i+1,nums, curSet)
        curSet.pop()


        #not add it
        self.helper(i+1,nums, curSet)

        