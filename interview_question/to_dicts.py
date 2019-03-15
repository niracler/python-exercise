# """
# 题目：将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
#
# """


class Solution:
    def to_dicts(self, a):
        """
        这个是我的解法， 我没有将最后的结果的value
        :param a:
        :return:
        """
        result = {}
        for i in a.split("|"):
            result[i.split(":")[0]] = i.split(":")[1]  # 这段不够pythonic

        return result

    def to_dicts2(self, a):
        """
        这个是别人的解法
        :param a:
        :return:
        """
        result = {}
        for item in a.split("|"):
            key, value = item.split(":")
            result[key] = int(value)

        return result

    def to_dicts3(self, a):
        """
        当然，还有更为pythonic的
        :param a:
        :return:
        """

        return {k: int(v) for t in a.split("|") for k, v in (t.split(":"), )}


if __name__ == '__main__':
    a = "k:1 |k1:2|k2:3|k3:4"

    solution = Solution()
    result = solution.to_dicts(a)
    print(result)

    result = solution.to_dicts2(a)
    print(result)

    result = solution.to_dicts3(a)
    print(result)

# """
# 分析:
#
# """
