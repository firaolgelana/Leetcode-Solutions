class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for num in arr1:
            s = str(num)
            prefix = ""
            
            for ch in s:
                prefix += ch
                prefixes.add(prefix)

        longest = 0
        for num in arr2:
            s = str(num)
            prefix = ""

            for i, ch in enumerate(s):
                prefix += ch

                if prefix in prefixes:
                    longest = max(longest, i + 1)

        return longest