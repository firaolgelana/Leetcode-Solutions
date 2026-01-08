class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        current = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= current:
                ans += current - nums[i] + 1
                current += 1
            current = max(current, nums[i])

        return ans
        