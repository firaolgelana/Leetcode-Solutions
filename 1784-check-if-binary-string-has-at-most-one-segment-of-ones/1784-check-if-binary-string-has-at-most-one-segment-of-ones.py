class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        lidx, ridx = s.index('1'), s.rindex('1')
        return '0' not in s[lidx:ridx]
        