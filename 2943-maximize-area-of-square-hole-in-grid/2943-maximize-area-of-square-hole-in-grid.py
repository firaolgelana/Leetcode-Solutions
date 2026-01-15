class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        n, m = len(hBars), len(vBars)
        def calculate_cons(n, bars):
            max_cons, count = 0, 1
            for i in range(1, n):
                if bars[i - 1] == bars[i] - 1:
                    count += 1
                else:
                    max_cons = max(max_cons, count)
                    count = 1
            return max(count, max_cons)
        length = min(calculate_cons(n, hBars), calculate_cons(m, vBars))
        return (length + 1) ** 2
