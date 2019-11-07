# """
# 题目：
# 题目二. input.txt中有10万个随机整数，每行一个，范围从0-99999，
# 需要分别统计[0-99]、[100-199]、[200-299]、[300-399]  …… [99900, 99999]，出现的次数。
# 输出为每个范围及其中数字出现的次数，范围和数字间空格分隔，每行一个。（20）
#
# 示例：
# 输入文件input.txt:
# 123
# 12
# 5
# 123
# …
# 输出（打印到标准输出）：
# 0-99 26
# 100-199 128
# 200-2993
# …
#
# url:
# """

import random


class Solution:
    def que2(self, a):
        f = open('input.txt', 'w')
        for i in range(1000):
            f.write(str(random.randint(0, 99999)) + '\n')
        f.close()

        res = {}

        f = open('input.txt', 'r')
        for i in range(1000):
            num = int(f.readline())
            if num // 100 not in res:
                res[num // 100] = 1
            else:
                res[num // 100] += 1
        f.close()

        return res


if __name__ == '__main__':
    a = ""

    solution = Solution()
    result = solution.que2(a)

    for key in result.keys():
        print(str(key * 100) + "~" + str(key * 100 + 99) + " " + str(result[key]))

# """
# 分析:
#
# """
