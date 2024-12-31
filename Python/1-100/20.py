class Solution:
    def isValid(self, s: str) -> bool:
        order = []
        for char in s:
            if char in "({[":
                order += char
            elif char == ")":
                if not order or order.pop() != "(":
                    return False
            elif char == "}":
                if not order or order.pop() != "{":
                    return False
            elif char == "]":
                if not order or order.pop() != "[":
                    return False
        return not order
