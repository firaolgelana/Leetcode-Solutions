class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row, col = [0] * len(mat), [0] * len(mat[0])
        for i in range(len(mat)):
            row[i] += mat[i].count(1)
        for j in range(len(mat[0])):
            cnt = 0
            for i in range(len(mat)):
                cnt += mat[i][j]
            col[j] += cnt

        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] and row[i] == 1 and col[j] == 1:
                    res += 1

        return res

        