class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        # Map each value to all indices where it appears
        pos = defaultdict(list)
        for i, val in enumerate(arr):
            pos[val].append(i)

        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        steps = 0

        while queue:
            # Process all nodes at the current BFS level
            for _ in range(len(queue)):
                i = queue.popleft()
                
                # Reached the last index
                if i == n - 1:
                    return steps

                # 1. Jump to adjacent indices (i-1, i+1)
                for nxt in (i - 1, i + 1):
                    if 0 <= nxt < n and not visited[nxt]:
                        visited[nxt] = True
                        queue.append(nxt)

                # 2. Jump to indices with the same value
                val = arr[i]
                if val in pos:
                    for nxt in pos[val]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            queue.append(nxt)
                    # Remove the value from the map after first use.
                    # This prevents O(N^2) behavior when many elements share the same value.
                    del pos[val]

            steps += 1

        return steps