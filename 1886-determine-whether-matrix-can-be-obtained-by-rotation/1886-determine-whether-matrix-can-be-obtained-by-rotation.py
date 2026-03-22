class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rotate90(matrix):
            new_matrix = []
            for j in range(n):
                row = []
                for i in range(n):
                    row.append(mat[n - i - 1][j])
                new_matrix.append(row)
            return new_matrix
        for i in range(4):
            if mat == target:
                return True
            mat = rotate90(mat)

        return False