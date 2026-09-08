// 75 ms | 19.3 MB
class Solution:
    def findKthPositive(self, arr, k):
        num = 1

        while k > 0:
            if num not in arr:
                k -= 1

            if k == 0:
                return num

            num += 1