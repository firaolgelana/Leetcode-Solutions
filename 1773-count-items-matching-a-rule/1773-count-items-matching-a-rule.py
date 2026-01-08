class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        maps = {'type': 0, 'color': 1, 'name': 2}
        count = 0
        for i in range(len(items)):
            if items[i][maps[ruleKey]] == ruleValue:
                count += 1
        
        return count
        