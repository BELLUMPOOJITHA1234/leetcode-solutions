// 644 ms | 22.2 MB
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return ans
       