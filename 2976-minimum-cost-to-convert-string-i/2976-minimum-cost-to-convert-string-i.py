class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for start, end, cst in zip(original, changed, cost):
            graph[start].append((end, cst))

        def shortest(node):
            heap = [(0, node)]
            min_cost = {}
            while heap:
                curr_cost, curr_node = heappop(heap)
                if curr_node in min_cost:
                    continue
                min_cost[curr_node] = curr_cost
                for nei, cost in graph[curr_node]:
                    heappush(heap, (cost + curr_cost, nei))
            
            return min_cost
        
        min_cost_map = {char : shortest(char) for char in set(source)}
        ans = 0
        for src, tar in zip(source, target):
            if tar not in min_cost_map[src]:
                return -1
            ans += min_cost_map[src][tar]

        return ans


        