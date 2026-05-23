class Solution:
    def check(self, nums: List[int]) -> bool:
        idx = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                idx = i + 1
                break
        return sorted(nums) == nums[idx:] + nums[:idx]
        
        