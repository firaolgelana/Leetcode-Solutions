class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        def pref(nums):
            count = defaultdict(int)
            total = defaultdict(int)
            res = [0] * len(nums)

            for i, num in enumerate(nums):
                res[i] = count[num] * i - total[num]
                count[num] += 1
                total[num] += i

            return res

        prefix = pref(nums)
        suffix = pref(nums[::-1])[::-1]

        return [p + s for p, s in zip(prefix, suffix)]