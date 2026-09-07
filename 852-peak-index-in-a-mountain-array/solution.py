// 0 ms | 31.1 MB
class Solution:
    def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                # We are on increasing side
                left = mid + 1
            else:
                # We are on decreasing side or at peak
                right = mid

        return left