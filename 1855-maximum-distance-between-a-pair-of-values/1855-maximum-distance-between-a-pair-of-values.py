class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def search(idx, num):
            left, right = idx, len(nums2) - 1
            best = 0
            while left <= right:
                mid = left + (right - left) // 2
                if nums2[mid] >= num:
                    best = mid
                    left = mid + 1
                else:
                    right = mid - 1
            # print(idx, num, left, right)
            return best
            
        max_dist = float('-inf')
        for i in range(len(nums1)):
            idx = search(i, nums1[i])
            max_dist = max(max_dist, idx - i)

        return max_dist      
