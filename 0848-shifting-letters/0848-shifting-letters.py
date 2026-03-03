class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = []
        _sum = sum(shifts)
        for i in range(len(s)):
            new_char = chr((ord(s[i]) - ord('a') + _sum) % 26 + ord('a'))
            res.append(new_char)
            _sum -= shifts[i] 

        return ''.join(res)
