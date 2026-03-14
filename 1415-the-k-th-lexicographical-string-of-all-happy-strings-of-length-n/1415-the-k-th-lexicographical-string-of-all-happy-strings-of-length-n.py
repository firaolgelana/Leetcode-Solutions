class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        def bactrack(idx, current):
            if len(current) == n:
                self.count += 1
                if self.count == k:
                    return "".join(current)
                return
            for char in "abc":
                if current and current[-1] == char:
                    continue
                current.append(char)
                find = bactrack(idx + 1, current)
                if find:
                    return find
                current.pop()
        
        ans = bactrack(0, [])
        return ans if ans else ""