class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        n = 1
        while candies > 0:
            for i in range(num_people):
                if candies < 0:
                    break
                res[i] += min(n, candies)
                candies -= n
                n += 1

        return res


        