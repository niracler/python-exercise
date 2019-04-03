# """
# 题目：统计一段字符串中字符出现的次数
#
# """


class Solution:
    def count_str(self, a):
        str_dict = {}
        for i in a:
            str_dict[i] = str_dict.get(i, 0) + 1

        return str_dict


if __name__ == '__main__':
    a = "ghodfigidnfouinbsdibnasipodbjp[af[asfljansf/Z:nasmflin.xfn/zxfp'zc;xzv.x/zc,o;ajf;oasjfnlknzxlcisa857324b8ds"

    solution = Solution()
    result = solution.count_str(a)
    print(result)

# """
# 分析:
#
# """