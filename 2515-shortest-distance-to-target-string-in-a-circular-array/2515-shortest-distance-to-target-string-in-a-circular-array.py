class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        shortest = 0
        for k in range(len(words)):
            i = (startIndex + k) % len(words)
            if target == words[i % len(words)]:
                break
            shortest += 1
        cnt = 0
        for k in range(len(words)):
            i = (startIndex - k) % len(words)
            if target == words[i % len(words)]:
                break
            cnt += 1

        return min(shortest, cnt)