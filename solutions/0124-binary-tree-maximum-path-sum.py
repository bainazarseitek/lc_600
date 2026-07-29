# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val
        def dfs(root, maxVal):
            if not root: return 0
            
            left_sum = dfs(root.left, maxVal)
            right_sum = dfs(root.right, maxVal)

            maxVal=root.val + max(left_sum, right_sum, 0)
            self.maxSum = max((root.val +left_sum + right_sum), self.maxSum, maxVal, root.val)

            return maxVal
        dfs(root, root.val)
        return self.maxSum

        