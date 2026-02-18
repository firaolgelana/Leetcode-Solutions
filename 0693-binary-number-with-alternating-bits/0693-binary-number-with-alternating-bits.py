class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)
        return '11' not in binary and '00' not in binary
        