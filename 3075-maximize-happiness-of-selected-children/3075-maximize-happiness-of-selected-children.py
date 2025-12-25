class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        max_sum = 0
        for i in range(k):
            max_sum += max(happiness[i] - i, 0)

        return max_sum
        