class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        import math
        B = int(math.sqrt(n)) + 1
        
        small = [{} for _ in range(B + 1)]
        
        for l, r, k, v in queries:
            if k > B:
                idx = l
                while idx <= r:
                    nums[idx] = (nums[idx] * v) % MOD
                    idx += k
            else:
                if l % k not in small[k]:
                    small[k][l % k] = []
                small[k][l % k].append((l, r, v))
        
        for k in range(1, B + 1):
            if not small[k]:
                continue
            
            for rem in small[k]:
                updates = small[k][rem]
                
                for start in range(rem, n, k):
                    mul = 1
                    for l, r, v in updates:
                        if l <= start <= r:
                            mul = (mul * v) % MOD
                    nums[start] = (nums[start] * mul) % MOD
        
        ans = 0
        for x in nums:
            ans ^= x
        
        return ans