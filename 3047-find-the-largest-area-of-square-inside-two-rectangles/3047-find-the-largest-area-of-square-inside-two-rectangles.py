class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0

        for i in range(n - 1):
            x1_i, y1_i = bottomLeft[i]
            x2_i, y2_i = topRight[i]

            for j in range(i + 1, n):
                x1_j, y1_j = bottomLeft[j]
                x2_j, y2_j = topRight[j]

                left_x = max(x1_i, x1_j)
                left_y = max(y1_i, y1_j)
                right_x = min(x2_i, x2_j)
                right_y = min(y2_i, y2_j)

                if right_x > left_x and right_y > left_y:
                    width = right_x - left_x
                    height = right_y - left_y
                    max_side = max(max_side, min(width, height))

        return max_side * max_side
