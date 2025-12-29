class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[(a, b)].append(c)
        @cache
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True

            def backtrack(i: int, next_row: list[str]) -> bool:
                if i == len(row) - 1:
                    return dfs("".join(next_row))

                pair = (row[i], row[i + 1])
                if pair not in mp:
                    return False

                for ch in mp[pair]:
                    next_row.append(ch)
                    if backtrack(i + 1, next_row):
                        return True
                    next_row.pop()

                return False

            return backtrack(0, [])

        return dfs(bottom)
