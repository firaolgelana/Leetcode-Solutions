class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]

        def combinations(nums, k):
            res = []
            path = []

            def backtrack(start):
                if len(path) == k:
                    res.append(sum(path))
                    return

                for i in range(start, len(nums)):
                    path.append(nums[i])
                    backtrack(i + 1)
                    path.pop()

            backtrack(0)
            return res

        result = []

        for h_led in range(0, min(4, turnedOn) + 1):
            m_led = turnedOn - h_led

            if m_led > 6:
                continue

            possible_hours = combinations(hours, h_led)
            possible_minutes = combinations(minutes, m_led)

            for h in possible_hours:
                if h > 11:
                    continue
                for m in possible_minutes:
                    if m > 59:
                        continue
                    result.append(f"{h}:{m:02d}")

        return result
