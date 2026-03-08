class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        perm = []
        n = len(nums[0])
        def backtrack(arr):
            if len(arr) == n:
                perm.append(''.join(arr[:]))
                return
            for char in '01':
                arr.append(char)

                backtrack(arr)
                arr.pop()
            
        backtrack([])
        for bin in perm:
            if not bin in nums:
                return bin
        