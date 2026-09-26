// 3 ms | 19.3 MB
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = []

        for num in range(left, right + 1):
            temp = num
            valid = True

            while num > 0:
                digit = num % 10

                if digit == 0 or temp % digit != 0:
                    valid = False
                    break

                num //= 10

            if valid:
                lst.append(temp)

        return lst