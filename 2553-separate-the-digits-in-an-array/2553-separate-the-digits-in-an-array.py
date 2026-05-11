class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        strs = "".join(str(num) for num in nums)
        digits = [int(n) for n in strs]
        return digits
