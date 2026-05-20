class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common = [0] * len(A)
        seenA, seenB = set(), set()
        for i in range(len(A)):
            common[i] = common[i-1]
            if A[i] == B[i]:
                common[i] += 1
            else:
                if A[i] in seenB:
                    common[i] += 1
                if B[i] in seenA:
                    common[i] += 1
            seenA.add(A[i])
            seenB.add(B[i])
        return common

        