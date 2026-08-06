class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            for x in str(n):
                product *= int(x)
            if product % t == 0:
                return n

            n += 1

        
        