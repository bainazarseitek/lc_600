class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        
        for n in nums:
            total += n
            prefix.append(total)

        for i in range(len(nums)):
            left = prefix[i] - nums[i]
            right = total - prefix[i]

            if left == right:
                return i

        return -1