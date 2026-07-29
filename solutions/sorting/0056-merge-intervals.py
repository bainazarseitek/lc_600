class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res= []
        intervals.sort(key = lambda i:i[0])
        res.append(intervals[0])
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if start<=lastEnd:
                res[-1][1] = max(end, lastEnd)
            else:
                res.append([start, end])
        return res