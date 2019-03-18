# """
# 题目：设计实现遍历目录与子目录，抓取.py文件
#
# """

import os
from glob import iglob

class Solution:
    def os_test(self, s_path, suffix):
        """自己写的方法, 使用listdir获得文件列表"""

        res = []

        if s_path[0] != '/':
            s_path = os.path.join(os.getcwd(), s_path)

        for cur in os.listdir(s_path):
            cur = os.path.join(s_path, cur)
            if os.path.isdir(cur):
                self.os_test(cur, suffix)
            else:
                if suffix in cur:
                    res.append(cur)

        return s_path

    def get_files1(self, dir, suffix):
        """
        使用os.walk, os.walk可以得到一个三元tupple(dirpath, dirnames, filenames)
        dirpath: 是一个string, 代表目录的路径,
        dirname: 是一个list, 包含dirpath下所有子目录的名字
        filenames: 是一个list, 包含了非目录文件的名字
        使用os.splittext可以得到文件后缀
        """
        res = []
        for root, dirs, files in os.walk(dir):
            for filename in files:
                name, suf = os.path.splitext(filename)
                if suf == suffix:
                    res.append(os.path.join(root, filename))
        return res

    def get_files2(self, dir, suffix):
        """使用glob进行文件搜索"""
        res = []
        for i in iglob(f"{dir}/**/*{suffix}", recursive=True):
            res.append(i)

        return res


if __name__ == '__main__':
    s_path = "/home/niracler/PycharmProjects/python-exercise"
    suffix = ".py"

    solution = Solution()
    result = solution.os_test(s_path, suffix)
    print(result)
    result = solution.get_files1(s_path, suffix)
    print(result)
    result = solution.get_files2(s_path, suffix)
    print(result)
    
# """
# 分析:
#
# """
