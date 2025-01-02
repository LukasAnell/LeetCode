from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        while len(tokens) > 1:
            firstOperator = ""
            i = 0
            for i in range(len(tokens)):
                token = tokens[i]
                if token in operators:
                    firstOperator = token
                    break
            num1 = tokens[i - 2]
            num2 = tokens[i - 1]
            result = str(int(eval(num1 + firstOperator + num2)))
            tokens[i] = result
            tokens = tokens[:i - 2] + tokens[i:]
        return int(tokens[0])
