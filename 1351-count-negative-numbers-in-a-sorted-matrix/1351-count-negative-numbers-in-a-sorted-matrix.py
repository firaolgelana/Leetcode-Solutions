class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        left, right = len(grid) - 1, 0
        count = 0
        while left >= 0 and right < len(grid[0]):
            if grid[left][right] < 0:
                count += len(grid[0]) - right
                left -= 1
            else:
                right += 1
        return count