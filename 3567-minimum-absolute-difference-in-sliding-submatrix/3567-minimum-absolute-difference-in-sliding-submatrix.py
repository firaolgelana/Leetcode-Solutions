class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ans = []
        for i in range(n - k + 1):
            curr = []
            for j in range(m - k + 1):
                seen = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        seen.add(grid[x][y])
                arr = sorted(seen)
                min_val = float('inf')
                if len(arr) == 1:
                    curr.append(0)
                for a in range(1, len(arr)):
                    min_val = min(min_val, arr[a] - arr[a - 1])
                if min_val != float('inf'):
                    curr.append(min_val)
            if curr:
                ans.append(curr[:])

        return ans