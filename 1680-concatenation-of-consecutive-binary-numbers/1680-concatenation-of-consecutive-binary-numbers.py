class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = j = 0
        mod = 10 ** 9 + 7
        for i in range(1, n + 1):
            res <<= i.bit_length()
            res += i
            res %= mod

        return res % mod