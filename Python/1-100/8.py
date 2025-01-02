class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        if s[0] not in "+-0123456789":
            return 0
        if s[0] in "+-" and len(s) == 1:
            return 0
        if s[0] in "+-" and s[1] not in "0123456789":
            return 0
        for i in range(1, len(s)):
            if s[i] not in "0123456789":
                s = s[:i]
                break
        if s[0] in "+-":
            if int(s[1:]) > 2**31 - 1:
                return 2**31 - 1 if s[0] == "+" else -(2**31)
            return int(s)
        if int(s) > 2**31 - 1:
            return 2**31 - 1
        return int(s)
