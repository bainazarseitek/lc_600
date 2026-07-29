class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        freq_map = dict(count)
        res=""
        minHeap = [(-n, s) for s, n in freq_map.items()]
        heapq.heapify(minHeap)

        q=deque()
        while minHeap or q:
            if not minHeap:
                return ""
            n, s = heapq.heappop(minHeap)
            n+=1
            res+=s
            if q:
                n_prev,s_prev = q.popleft()
                heapq.heappush(minHeap,(n_prev,s_prev))            
            if n<0:
                q.append([n,s])



        return res
        