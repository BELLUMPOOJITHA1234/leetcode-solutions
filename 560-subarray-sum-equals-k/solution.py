// 28 ms | 21.7 MB
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        total = 0
        ans = 0

        for x in nums:
            total += x

            if total - k in count:
                ans += count[total - k]

            count[total] = count.get(total, 0) + 1

        return ans
        