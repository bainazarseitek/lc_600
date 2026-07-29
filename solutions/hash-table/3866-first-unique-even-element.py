class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            elif n % 2 == 0:
                hashmap[n]=1
        
        for n in hashmap:
            if hashmap[n] == 1:
                return n
        return -1
                