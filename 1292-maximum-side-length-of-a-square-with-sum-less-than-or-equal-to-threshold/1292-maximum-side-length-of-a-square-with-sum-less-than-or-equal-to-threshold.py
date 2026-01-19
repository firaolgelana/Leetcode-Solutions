class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        ps = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                ps[i][j] = (
                    mat[i-1][j-1]
                    + ps[i-1][j]
                    + ps[i][j-1]
                    - ps[i-1][j-1]
                )

        def can(mid):
            for i in range(n - mid + 1):
                for j in range(m - mid + 1):
                    square_sum = (
                        ps[i + mid][j + mid]
                        - ps[i][j + mid]
                        - ps[i + mid][j]
                        + ps[i][j]
                    )
                    if square_sum <= threshold:
                        return True
            return False


        low, high = 0, min(n, m)
        while low <= high:
            mid = low + (high - low) // 2
            if can(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
        