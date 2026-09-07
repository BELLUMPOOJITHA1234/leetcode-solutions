// 51 ms | 19.1 MB
class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                # mid is bad, but there may be an earlier bad version
                right = mid
            else:
                # mid is good, so search after mid
                left = mid + 1

        return left