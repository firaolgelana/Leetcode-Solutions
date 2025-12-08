class Solution:
    def countTriples(self, n: int) -> int:
        numTriples = 0
        for i in range(1, n):
            for j in range(1, n + 1):
                square = i ** 2 + j ** 2
                c = sqrt(square)
                if c <= n and c >= 1 and c == int(c):
                    numTriples += 1

        return numTriples
        