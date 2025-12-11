class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        mapsX = defaultdict(list)
        mapsY = defaultdict(list)
        for x, y in buildings:
            insort(mapsX[x], y)
            insort(mapsY[y], x)
        count = 0
        for x, y in buildings:
            if mapsX[x][0] < y < mapsX[x][-1] and mapsY[y][0] < x < mapsY[y][-1]:
                count += 1
        
        return count


        