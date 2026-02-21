class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return False
                    
            return n >= 2
        
        count = 0
        for i in range(left , right + 1):
            new = i.bit_count()
            if is_prime(new):
                count += 1
        return count
            
            
        
        