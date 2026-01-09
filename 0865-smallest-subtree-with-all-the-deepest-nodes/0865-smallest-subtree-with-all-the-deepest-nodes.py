# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node.left and not node.right:
                return node, depth
            left, right = None, None
            if node.left:
                left = dfs(node.left, depth + 1)
            if node.right:
                right = dfs(node.right, depth + 1)
            if not right and left:
                return left
            if not left and right:
                return right
            if left[1] > right[1]:
                return left
            if right[1] > left[1]:
                return right
            return node, left[1]
        
        return dfs(root, 0)[0]

            

        