# """
# 题目：
# 题目一. 文件input.txt是一个文本文件，每一行有多列（用空格分隔）。
# keyword.conf是一个关键词配置文件，每一行是一个词。
# 请找出文件input.txt中第一列包含keyword.conf中任意一个关键词的文本行并输出。（25）
# 示例
# 输入：
# 文件input.txt内容：
# abc xxx
# bcd xxx
# def xxx
# xyz xxx
#
# 文件keyword.conf内容：
# bc
# eft
#
# 输出（打印到标准输出）：
# abc xxx
# bcd xxx
#
# url:
# """


class Solution:
    def que1(self, a):
        keyword_list = []

        f2 = open('keyword.conf', 'r')
        for i in f2.readlines():
            keyword_list.append(i.split()[0])

        f1 = open('input.txt', 'r')
        for i in f1.readlines():
            inp = i.split(' ')
            for keyword in keyword_list:
                if keyword in inp:
                    print(i)


        f1.close()
        f2.close()


        return ""


if __name__ == '__main__':
    a = ""

    solution = Solution()
    result = solution.que1(a)
    print(result)

# """
# 分析:
#
# """
