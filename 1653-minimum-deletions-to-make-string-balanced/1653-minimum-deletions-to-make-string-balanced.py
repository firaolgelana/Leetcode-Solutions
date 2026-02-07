class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        pref, suff = [0] * n, [0] *  n
        cnt = 0
        for i in range(n):
            pref[i] = cnt
            if s[i] == 'b':
                cnt += 1
        cnt = 0
        for i in range(n - 1, -1, -1):
            suff[i] = cnt
            if s[i] == 'a':
                cnt += 1

        min_del = n
        for i in range(n):
            min_del = min(min_del, pref[i] + suff[i])

        return min_del
        