class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        length = len(encodedText)
        if length == 0:
            return ""
        
        cols = length // rows
        ans = []
        
        for j in range(cols):
            r, c = 0, j
            while r < rows and c < cols:
                ans.append(encodedText[r * cols + c])
                r += 1
                c += 1
        
        return "".join(ans).rstrip()