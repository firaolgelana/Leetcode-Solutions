class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for key, val in count.items():
            if val > 2:
                return False

        return True