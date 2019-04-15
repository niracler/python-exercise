# """
# 题目：Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
# """


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        cur = [1]
        for i in range(numRows):
            result.append(cur)
            cur = self.gen_next(cur)

        return result

    def gen_next(self, cur):
        """
        由当前列表获得下一个列表
        :param cur:
        :return:
        """
        next_list = [1]

        for i in range(len(cur)-1):
            next_list.append(cur[i] + cur[i + 1])

        next_list.append(1)

        return next_list


if __name__ == '__main__':
    a = 5

    solution = Solution()
    result = solution.generate(a)
    print(result)

# """
# 分析: 这个的话，如果您能够给个方向让我们去完成的话，我们可以自己去查找资料完成，因为我们也是在这个方向上自学的，
# 我们会在弄出阶段性的成果时再找您交流一下，不知可以不
# 实在是没时间的话我们再尝试去找其他导师
# """
