class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total_pack = sum(apple)
        curr = 0
        for i, cap in enumerate(capacity):
            curr += cap
            if curr >= total_pack:
                return i + 1
        
        return len(capacity)

        