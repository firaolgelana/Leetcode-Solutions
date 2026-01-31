class Solution:
    def countElements(self, nums: List[int]) -> int:
        max_num, min_num = max(nums), min(nums)
        count = 0
        for num in nums:
            if min_num < num < max_num:
                count += 1
                
        return count