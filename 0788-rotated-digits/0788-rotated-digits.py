class Solution:
    def rotatedDigits(self, n: int) -> int:
        cnt = 0
        for i in range(2, n + 1):
            str_i = str(i)
            if '3' in str_i or '4' in str_i or '7' in str_i:
                continue
            for char in '2569':
                if char in str_i:
                    cnt += 1
                    break

        return cnt
        # 123456789