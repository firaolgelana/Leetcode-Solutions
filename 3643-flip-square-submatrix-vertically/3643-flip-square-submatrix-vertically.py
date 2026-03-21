class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        arr = []
        for i in range(x, x + k):
            curr = []
            for j in range(y, y + k):
                curr.append(grid[i][j])
            arr.append(curr[:])

        arr = arr[::-1]
        for i in range(x, x + k):
            for j in range(y, y + k):
                grid[i][j] = arr[i - x][j - y]

        return grid


