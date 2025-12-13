class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        def validCode(code):
            for char in code:
                if not char.lower().isalnum() and char != '_':
                    return False
            return True and code
        ans = []
        for code, business, active in zip(code, businessLine, isActive):
            if validCode(code) and active and business in categories:
                ans.append((code, business))
        ans.sort(key=lambda x:(x[1], x[0]))
        return [code for code, categories in ans]

        