class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_diff = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                if abs(i - start) < min_diff:
                    min_diff = abs(i - start)
                    
        return min_diff
        