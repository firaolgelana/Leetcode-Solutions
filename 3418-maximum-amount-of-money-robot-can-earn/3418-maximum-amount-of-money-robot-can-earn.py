class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        rows, cols = len(coins), len(coins[0])
        K = 2

        dp = [[[float('-inf')] * (K + 1) for _ in range(cols)] for _ in range(rows)]

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                for k in range(K + 1):
                    
                    if r == rows - 1 and c == cols - 1:
                        if coins[r][c] < 0 and k > 0:
                            dp[r][c][k] = 0
                        else:
                            dp[r][c][k] = coins[r][c]
                        continue

                    best_next = float('-inf')

                    if r + 1 < rows:
                        best_next = max(best_next, dp[r + 1][c][k])

                    if c + 1 < cols:
                        best_next = max(best_next, dp[r][c + 1][k])

                    take = coins[r][c] + best_next

                    skip = float('-inf')
                    if coins[r][c] < 0 and k > 0:
                        best_skip = float('-inf')
                        if r + 1 < rows:
                            best_skip = max(best_skip, dp[r + 1][c][k - 1])
                        if c + 1 < cols:
                            best_skip = max(best_skip, dp[r][c + 1][k - 1])
                        skip = best_skip

                    dp[r][c][k] = max(take, skip)

        return dp[0][0][K]