# """
# 题目：输入某年某月某日，判断这一天是这一年的第几天？
#
# """

import datetime

class Solution:
    def get_data_in_year(self, year, month, day):
        dif_day = datetime.date(year=year, month=month, day=day) - datetime.date(year=year, month=1, day=1)

        return dif_day.days


if __name__ == '__main__':
    year = 2019
    month = 12
    day = 2

    solution = Solution()
    result = solution.get_data_in_year(year, month, day)
    print(result)

# """
# 分析:
#
# """
