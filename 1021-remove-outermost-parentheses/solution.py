// 3 ms | 19.2 MB
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        count = 0

        for ch in s:
            if ch == '(':
                if count > 0:
                    result += ch
                count += 1

            else:
                count -= 1
                if count > 0:
                    result += ch

        return result