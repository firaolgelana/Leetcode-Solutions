class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box)
        m = len(box[0])
        rotated_box = [[0 for _ in range(n)]for _ in range(m)]
        x = n
        for i in range(n):
            stack = []
            for char in reversed(box[i]):
                temp = []
                while stack and stack[-1] == '.' and char == '#':
                    temp.append(stack.pop())
                stack.append(char)
                stack.extend((temp))
            n = 0
            for char in reversed(stack):
                rotated_box[n][x-1] = char
                n += 1
            x -= 1

        return rotated_box
        