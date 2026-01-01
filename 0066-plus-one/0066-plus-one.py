class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in reversed(range(len(digits))):
            _sum = digits[i] + 1
            digits[i] = _sum % 10
            carry = _sum // 10
            if carry == 0:
                break
        if carry:
            digits.insert(0, carry)

        return digits