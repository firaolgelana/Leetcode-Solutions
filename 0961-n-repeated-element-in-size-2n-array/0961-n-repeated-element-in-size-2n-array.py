class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        for key, val in Counter(nums).items():
            if val == n:
                return key
        