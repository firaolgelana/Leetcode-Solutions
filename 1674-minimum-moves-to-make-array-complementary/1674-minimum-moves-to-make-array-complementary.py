class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        l, r = 0, n - 1

        while l < r:
            a = nums[l]
            b = nums[r]

            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            diff[2] += 2

            diff[low] -= 1
            diff[high + 1] += 1

            diff[s] -= 1
            diff[s + 1] += 1

            l += 1
            r -= 1

        ans = float('inf')
        cur = 0

        for target in range(2, 2 * limit + 1):
            cur += diff[target]
            ans = min(ans, cur)

        return ans