class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap=defaultdict(int)
        res=[]
        for n in nums:
            hmap[n] += 1
        nm=sorted(hmap, key=hmap.get, reverse=True)
        return nm[:k]

        