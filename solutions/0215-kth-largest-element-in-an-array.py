class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num>heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]
        # nums = [-n for n in nums]
        # heapq.heapify(nums)
        # while k>0:
        #     last = heapq.heappop(nums)
        #     k-=1

        # return -last

        