# """
# 题目：输入日期， 判断这一天是这一年的第几天？
#
# """

import datetime


class Solution:
    def get_date(self, year, month, day):
        """
        输入日期， 判断这一天是这一年的第几天
        :param year:
        :param month:
        :param day:
        :return:
        """

        data1 = datetime.date(year=int(year), month=1, day=1)  # 该年第一天
        data2 = datetime.date(year=int(year), month=int(month), day=int(day))  # 该年日期的那一天

        return (data2 - data1).days + 1


if __name__ == '__main__':
    year = "2018"
    month = "5"
    day = "1"

    solution = Solution()
    result = solution.get_date(year, month, day)
    print(result)
