class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        @cache
        def find(i, j):
            if i == n:
                return sum(ord(c) for c in s2[j:])
            if j == m:
                return sum(ord(c) for c in s1[i:])

            if s1[i] == s2[j]:
                return find(i + 1, j + 1)
            else:
                left = find(i + 1, j) + ord(s1[i])
                right = find(i, j + 1) + ord(s2[j])
                return min(left, right)

        return find(0, 0)
