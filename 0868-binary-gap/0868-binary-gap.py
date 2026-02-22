class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        res = 0
        prev = None
        for i in range(len(binary)):
            if binary[i] == '1' and prev != None:
                res = max(res, i - prev) 
            if binary[i] == '1':
                prev = i

        return res

        