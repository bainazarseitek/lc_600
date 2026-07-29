class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest












# class FindUnion:
#     def __init__(self,n):
#         self.par = [i for i in range(n)]
#         self.rank = [1]*n
#     def find(self, x):
#         while x != self.par[x]:
#             x = self.par[x]
#         return self.par[x]
    

#     def union(self, x1, x2):
#         p1, p2 = self.find(x1), self.find(x2)

#         if p1 == p2:
#             return False
#         if self.rank[p1] > self.rank[p2]:
#             self.par[p2] = p1
#             self.rank[p1] += self.rank[p2]
#         else:
#             self.par[p1] = p2
#             self.rank[p2] += self.rank[p1]
#         return True


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         num_map  = {}
#         uf = FindUnion(len(nums))
#         if not nums:
#             return 0
#         for i, num in enumerate(nums):
#             if num in num_map:
#                 continue
#             num_map[num] = i
        
#             if num-1 in num_map:
#                 uf.union(i,num_map[num-1])
#             if num+1 in num_map:
#                 uf.union(i, num_map[num+1])
#         return max(uf.rank)


        
        