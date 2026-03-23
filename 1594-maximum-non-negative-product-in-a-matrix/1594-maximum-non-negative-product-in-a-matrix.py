class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n, m = len(grid), len(grid[0])
        @cache
        def dfs(row, col, product):
            nonlocal max_product
            product *= grid[row][col]
            if row == n - 1 and col == m - 1:
                max_product = max(max_product, product)
                return

            if row + 1 < n:
                dfs(row + 1, col, product)
            if col + 1 < m:
                dfs(row, col + 1, product)
            
        max_product = float('-inf')
        dfs(0, 0, 1)
        return max_product % mod if max_product >= 0 else -1



        