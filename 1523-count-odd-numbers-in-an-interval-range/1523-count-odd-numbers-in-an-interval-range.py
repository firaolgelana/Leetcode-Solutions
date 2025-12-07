class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return 1 if low & 1 else 0
        else:
            if low & 1 or high & 1:
                return (high - low) // 2 + 1
            else:
                return (high - low) // 2
        