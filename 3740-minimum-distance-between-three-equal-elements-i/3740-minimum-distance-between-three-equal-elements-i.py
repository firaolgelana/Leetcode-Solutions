class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        result = len(nums)
        seen = [(-len(nums), -len(nums))]*(len(nums)+1)
        for k, x in enumerate(nums):
            result = min(result, k - seen[x][0])
            seen[x] = (seen[x][1], k)
        return -1 if result >= len(nums) else 2 * result