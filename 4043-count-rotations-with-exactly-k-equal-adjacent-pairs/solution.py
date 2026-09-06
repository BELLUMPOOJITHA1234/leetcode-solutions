// 3 ms | 19.2 MB
class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)

        if n == 1:
            return 1 if k == 0 else 0

        # Count equal adjacent pairs in the circular string
        total = 0

        for i in range(n):
            if s[i] == s[(i + 1) % n]:
                total += 1

        # Count boundaries where adjacent characters are equal
        equal_boundaries = total

        # Number of boundaries where characters are different
        different_boundaries = n - total

        if k == total:
            return different_boundaries

        if k == total - 1:
            return equal_boundaries

        return 0