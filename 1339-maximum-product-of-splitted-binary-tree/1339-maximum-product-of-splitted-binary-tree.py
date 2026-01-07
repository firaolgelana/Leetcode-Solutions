# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        total_sum = 0
        def dfs(root):
            nonlocal total_sum
            if not root:
                return 0
            total_sum += root.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            _sum = node.val + dfs(node.left) + dfs(node.right)
            ans = max(ans, (total_sum - _sum) * _sum)
            return _sum
        dfs(root)
        return ans % MOD
      