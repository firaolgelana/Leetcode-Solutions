class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        arr = []
        for event in events:
            arr.append((event[0], 1, event[2]))
            arr.append((event[1] + 1, 0, event[2]))
        arr.sort()
        ans, max_num = 0, 0
        for event, status, value in arr:
            if status:
                ans = max(ans, max_num + value)
            else:
                max_num = max(max_num, value)
        return ans

        