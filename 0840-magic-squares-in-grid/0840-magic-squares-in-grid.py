class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(grid):
            seen = set()
            for i in range(3):
                for j in range(3):
                    seen.add(grid[i][j])
                    if grid[i][j] < 1 or grid[i][j] > 9:
                        return False
            if len(seen) < 9:
                return False
            main_diagonal = sum(grid[i][i] for i in range(3))
            diagonal = sum(grid[i][2 - i] for i in range(3))
            if main_diagonal != diagonal:
                return False
            for i in range(3):
                row_sum = sum(grid[i])
                col_sum = sum(grid[j][i] for j in range(3))
                if diagonal != row_sum or diagonal != col_sum:
                    return False

            return True

        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(n - 2):
            for j in range(m - 2):
                new_grid = [row[j:j + 3] for row  in grid[i:i + 3]]
                if isMagicSquare(new_grid):
                    count += 1
        
        return count
