class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        arr = nums + nums
        ans, n = [], len(nums)
        for i in range(n, n*2):
            if arr[i] < 0:
                idx = abs(arr[i]) % (2 * n)
                ans.append(arr[i - idx]) 
            else:
                idx = (arr[i] + i) % (2 * n)
                ans.append(arr[idx])
        return ans



        