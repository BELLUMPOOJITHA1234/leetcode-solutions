// 0 ms | 19.2 MB
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def days(date):
            months = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]
            month, day = map(int, date.split("-"))
            return sum(months[:month - 1]) + day

        start = max(days(arriveAlice), days(arriveBob))
        end = min(days(leaveAlice), days(leaveBob))

        return max(0, end - start + 1)
        