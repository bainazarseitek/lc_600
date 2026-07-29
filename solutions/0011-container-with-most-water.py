class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res=0

        while l<r:
            container = (r-l)*min(height[r], height[l])
            res=max(res,container)
            if height[r] < height[l]:
                r-=1
            else:
                l+=1
        return res