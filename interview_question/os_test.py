# """
# 题目：设计实现遍历目录与子目录，抓取.py文件
#
# """

import os

class Solution:
    def os_test(self, s_path):
        """自己写的方法"""
        if s_path[0] != '/':
            s_path = os.path.join(os.getcwd(), s_path)

        for cur in os.listdir(s_path):
            cur = os.path.join(s_path, cur)
            if os.path.isdir(cur):
                self.os_test(cur)
            else:
                if '.py' in cur:
                    print(cur)

        return s_path


if __name__ == '__main__':
    s_path = "/home/niracler/PycharmProjects/python-exercise"

    solution = Solution()
    result = solution.os_test(s_path)
    print(result)

# """
# 分析:
#
# """
