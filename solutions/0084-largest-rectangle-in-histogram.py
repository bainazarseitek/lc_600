class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[] # pair: start and heights

        for i, h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index, height = stack.pop()
                maxArea= max(maxArea,(i-index)*height)
                start=index
            stack.append((start,h))

        for i, h in stack:
            maxArea=max(maxArea, (h * (len(heights)-i)))
        
        return maxArea
        

                




        # n=len(heights)

        # stack=[]
        # leftMost=[-1]*n
        # for i in range(n):
        #     if stack and heights[stack[-1]] >= heights[i]:
        #         stack.pop()
        #     if stack:
        #         leftMost[i]=stack[-1]
        #     stack.append(i)
        
        # stack=[]
        # rightMost=[n]*n
        # for i in range(n-1, -1, -1):
        #     if stack and heights[stack[-1]] >= heights[i]:
        #         stack.pop()
        #     if stack:
        #         rightMost[i]=stack[-1]
        #     stack.append(i)
        # maxArea=0
        # for i in range(n):
        #     leftMost[i] += 1
        #     rightMost[i]-=1
        #     maxArea=max(maxArea, heights[i]*(rightMost[i]-leftMost[i]+1))
        # return maxArea

