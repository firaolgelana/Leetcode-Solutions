class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = defaultdict(int)
        new_paragraph = re.findall(r'\b[a-zA-Z]+\b', paragraph)
        for word in new_paragraph:
            word = word.lower()
            count[word] += 1
        res, _max = '', 0
        for word, val in count.items():
            if val > _max and word not in banned:
                res = word
                _max = val

        return res
        