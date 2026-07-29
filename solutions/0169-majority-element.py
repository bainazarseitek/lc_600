class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)
        for n in nums:
            hashmap[n]+=1

        maj=len(nums)/2
        for key, val in hashmap.items():
            if val > maj:
                return key
