class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = 0
        seen = set(word.lower())
        for char in seen:
            if char in word and char.swapcase() in word:
                cnt += 1

        return cnt