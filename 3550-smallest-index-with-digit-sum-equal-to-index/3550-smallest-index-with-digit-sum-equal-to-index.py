class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            str_num = str(num)
            cnt = 0
            for char in str_num:
                cnt += int(char)

            if cnt == i:
                return i
        
        return -1

        