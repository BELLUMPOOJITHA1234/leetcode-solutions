// 51 ms | 51.5 MB
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        ans = ""
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i+1:j]

                ans += d.get(key, "?")
                i = j + 1
            else:
                ans += s[i]
                i += 1

        return ans