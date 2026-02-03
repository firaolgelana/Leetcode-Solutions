class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 1
        inc = False
        while i < len(nums) and nums[i - 1] < nums[i]:
            inc = True
            i += 1
        if not inc:
            return False
        dec = False
        while i < len(nums) and nums[i - 1] > nums[i]:
            dec = True
            i += 1
        if not dec:
            return False
        inc = False
        while i < len(nums):
            if nums[i - 1] >= nums[i]:
                return False
            inc = True
            i += 1

        return inc
        