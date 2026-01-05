class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        count_neg, min_val = 0, float('inf')
        _sum = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    count_neg += 1
                min_val = min(min_val, abs(matrix[i][j]))
                _sum += abs(matrix[i][j])
                
        return _sum if count_neg % 2 == 0 else _sum - 2 * min_val
        