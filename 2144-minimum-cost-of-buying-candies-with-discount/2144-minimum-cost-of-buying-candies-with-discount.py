class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        two, min_cost = 2, 0
        for cost in cost:
            if two:
                min_cost += cost
            else: 
                two = 2
            two -= 1
        
        return min_cost

        