class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        def can(total_time):
            current_height = 0
            for t in workerTimes:
                val = (8 * total_time) // t
                k = (-1 + math.isqrt(1 + val)) // 2
                current_height += k
                if current_height >= mountainHeight:
                    return True
            return current_height >= mountainHeight
        low = 1
        fastest = min(workerTimes)
        high = fastest * (mountainHeight * (mountainHeight + 1)) // 2
        
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans