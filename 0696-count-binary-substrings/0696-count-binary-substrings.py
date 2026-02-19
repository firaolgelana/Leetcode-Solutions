class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = prev = 0
        cnt = 1
        count = False
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                res += min(prev, cnt)
                prev = cnt
                cnt = 1
                count = True
            else:
                cnt += 1
        if count:
            res += cnt
        return res 
    



        