class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        if total % 2 != 0:
            return False
        _sum = 0
        for i in range(n):
            for j in range(m):
                _sum += grid[i][j]
            if total // 2 == _sum:
                return True
        _sum = 0
        for i in range(m):
            for j in range(n):
                _sum += grid[j][i]
            if total // 2 == _sum:
                return True

        return False            

        

        