class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l = best = 0

        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1
            best = max(best, r - l + 1)

        return n - best
