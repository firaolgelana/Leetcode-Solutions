class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for j, num in enumerate(nums):
            for i in range(num.bit_length()):
                curr = num & ~(1 << i)
                if curr | (curr + 1) == num:
                    ans[j] = curr

        return ans        