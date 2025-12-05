class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prefix = list(accumulate(nums))
        ans = 0
        for num in prefix:
            if num > 0:
                ans += 1
            else:
                return ans

        return ans
        