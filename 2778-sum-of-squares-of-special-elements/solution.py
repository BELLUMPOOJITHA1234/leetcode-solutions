// 4 ms | 19.4 MB
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for i in range(n):
            if n % (i + 1) == 0:
                total += nums[i] * nums[i]

        return total