class Solution:
    def bestClosingTime(self, customers: str) -> int:
        score = 0
        max_score = 0
        best_time = 0

        for i, c in enumerate(customers):
            score += 1 if c == 'Y' else -1
            if score > max_score:
                max_score = score
                best_time = i + 1

        return best_time
