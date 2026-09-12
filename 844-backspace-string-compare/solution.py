// 0 ms | 19.3 MB
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def built(x):
            stack=[]
            for ch in x:
                if ch=='#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return ''.join(stack)
        return built(s)==built(t)