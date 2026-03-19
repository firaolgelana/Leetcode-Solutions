class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        
        px = [[0] * (m + 1) for _ in range(n + 1)]
        py = [[0] * (m + 1) for _ in range(n + 1)]
        
        ans = 0
        
        for i in range(n):
            for j in range(m):
                px[i+1][j+1] = px[i][j+1] + px[i+1][j] - px[i][j] + (grid[i][j] == 'X')
                py[i+1][j+1] = py[i][j+1] + py[i+1][j] - py[i][j] + (grid[i][j] == 'Y')
                
                cnt_x = px[i+1][j+1]
                cnt_y = py[i+1][j+1]
                
                if cnt_x == cnt_y and cnt_x > 0:
                    ans += 1
        
        return ans