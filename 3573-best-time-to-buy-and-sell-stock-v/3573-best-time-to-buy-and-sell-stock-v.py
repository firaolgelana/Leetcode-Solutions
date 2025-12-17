class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dfs(i, k, state):
            if i == n or k == 0:
                return 0 if state == 0 else -math.inf

            ans = dfs(i + 1, k, state)
            if state == 0:
                ans = max(ans, -prices[i] + dfs(i + 1, k, 1))
                ans = max(ans, prices[i] + dfs(i + 1, k, -1))

            elif state == 1:
                ans = max(ans, prices[i] + dfs(i + 1, k - 1, 0))

            elif state == -1:
                ans = max(ans, -prices[i] + dfs(i + 1, k - 1, 0))

            return ans

        return dfs(0, k, 0)
