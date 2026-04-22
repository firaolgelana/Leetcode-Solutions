class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for word in queries:
            if word in dictionary:
                ans.append(word)
                continue
            for d in dictionary:
                diff = 0
                for i in range(len(d)):
                    if word[i] != d[i]:
                        diff += 1
                    if diff > 2:
                        break
                if diff <= 2:
                    ans.append(word)
                    break
        
        return ans
            
        