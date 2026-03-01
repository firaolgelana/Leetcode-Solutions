class Solution:
    def minPartitions(self, n: str) -> int:
        lst = list(n)
        return int(max(lst, key=lambda x : int(x)))
