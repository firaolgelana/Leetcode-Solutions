class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t, disappear[v]))
            graph[v].append((u, t, disappear[u]))
        distance = [float('inf')] * n
        distance[0] = 0
        queue = [(0, 0)]
        while queue:
            cost, node = heappop(queue)
            if cost > distance[node]:
                continue
            for n, t, d in graph[node]:
                new_cost = cost + t
                if new_cost < d and distance[n] > new_cost:
                    distance[n] = new_cost
                    heappush(queue, (new_cost, n))

        return [num if num != float('inf') else -1 for num in distance]