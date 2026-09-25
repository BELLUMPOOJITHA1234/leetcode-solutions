// 10 ms | 34.9 MB
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        a=set(nums)
        for i in range(1,len(nums)+2):
            if i not in a:
                return i