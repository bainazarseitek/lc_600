class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap=[]
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        res=""
        while maxHeap:
            cnt, ch = heapq.heappop(maxHeap)
            if len(res)>1 and ch == res[-1] == res[-2]:
                if not maxHeap:
                    break
                cnt2, ch2 = heapq.heappop(maxHeap)
                res+=ch2
                cnt2+=1
                if cnt2:
                    heapq.heappush(maxHeap, (cnt2, ch2))
                heapq.heappush(maxHeap, (cnt, ch))

            else:
                res+=ch
                cnt+=1
                if cnt:
                    heapq.heappush(maxHeap, (cnt, ch))


        return res