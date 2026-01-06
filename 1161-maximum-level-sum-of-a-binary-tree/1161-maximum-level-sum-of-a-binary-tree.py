# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = smallest_level = 1
        queue = deque([root])
        max_sum = float('-inf')
        while queue:
            _sum = 0
            for _ in range(len(queue)):
                current = queue.popleft()
                _sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            if _sum > max_sum:
                smallest_level = level
                max_sum = _sum
            level += 1

        return smallest_level

                
        