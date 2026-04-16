class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        maps = defaultdict(list)
        for i, num in enumerate(nums):
            maps[num].append(i)
        
        ans = [-1] * len(queries)
        
        for qi, q in enumerate(queries):
            num = nums[q]
            positions = maps[num]
            
            if len(positions) == 1:
                continue
            
            idx = bisect_left(positions, q)
            
            prev_idx = positions[idx - 1] if idx > 0 else positions[-1]
            next_idx = positions[idx + 1] if idx < len(positions) - 1 else positions[0]
            
            d1 = abs(q - prev_idx)
            d1 = min(d1, n - d1)
            
            d2 = abs(q - next_idx)
            d2 = min(d2, n - d2)
            
            ans[qi] = min(d1, d2)
        
        return ans