class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(len(positions))])
        stack = []
        
        for pos, health, dir, idx in robots:
            if dir == 'R':
                stack.append([pos, health, dir, idx])
            else:
                while stack and stack[-1][2] == 'R' and health > 0:
                    if stack[-1][1] < health:
                        health -= 1
                        stack.pop()
                    elif stack[-1][1] > health:
                        stack[-1][1] -= 1
                        health = 0
                    else:
                        stack.pop()
                        health = 0
                if health > 0:
                    stack.append([pos, health, dir, idx])
        
        stack.sort(key=lambda x: x[3])
        return [h for _, h, _, _ in stack]
