class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)
            z = y-x
            if z == 0:
                continue
            else:
                heapq.heappush(maxHeap, z)
            
        return 0 if len(maxHeap) == 0 else -maxHeap[0]

        