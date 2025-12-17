class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        dp = [[float('-inf')] * 3 for _ in range(k + 1)]
        dp[0][0] = 0

        for t in range(1, k + 1):
            dp[t][0] = 0

        for price in prices:
            new_dp = [[-math.inf] * 3 for _ in range(k + 1)]
            for t in range(k + 1):
                new_dp[t][0] = max(new_dp[t][0], dp[t][0])
                new_dp[t][1] = max(new_dp[t][1], dp[t][1])
                new_dp[t][2] = max(new_dp[t][2], dp[t][2])

                if t > 0:
                    new_dp[t - 1][0] = max(new_dp[t - 1][0], dp[t][1] + price)
                    new_dp[t - 1][0] = max(new_dp[t - 1][0], dp[t][2] - price)

                new_dp[t][1] = max(new_dp[t][1], dp[t][0] - price)
                new_dp[t][2] = max(new_dp[t][2], dp[t][0] + price)

            dp = new_dp

        return max(dp[t][0] for t in range(k + 1))
