class Solution:
    def countAndSay(self, n: int) -> str:
        output = "1"
        for _ in range(n - 1):
            newOutput = ""
            streaks = []
            i = 0
            while i < len(output):
                current = output[i]
                count = 0
                j = i
                while j < len(output) and output[i] == output[j]:
                    count += 1
                    j += 1
                else:
                    i = j
                if count > 0:
                    streaks += [(current, count)]
            for pair in streaks:
                newOutput += str(pair[1]) + pair[0]
            output = newOutput
        return output
