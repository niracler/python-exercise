# """
# 题目：题目四. 给定如下设备数据文件input.txt，其中每行一条记录，空格分隔。一行记录包含3个字段：
# 设备ID、连接的wifimac、时间戳。
# 输入文件是一个设备一段时间范围内连接过的wifimac的列表（设备ID都一样），请计算每个设备连接过的wifimac的熵。
# 熵的计算方法：对于一个长度为n的序列xs，它包含m+1中不同的取值，s0, s1, …, sm，
# 这些取值对应的出现概率分别是p0, p1, …,pm，则这个序列的熵为H(X) = -(p0*log2(p0) + p1*log2(p1) + … + pm*log2(pm)).
# 其中，某个取值出现的概率p的计算方法为：这个取值出现的次数 除以 长度n。
#
# 示例：
# 输入input.txt：
# deviceId1 wifimac1 t1
# deviceId1 wifimac2 t2
# deviceId1 wifimac3 t3
# deviceId1 wifimac3 t4
# 输出:
# devicId1, 1.5
#
# 熵的计算过程：
# deviceId1活跃4次，
# 	wifimac1 出现1次   wifimac1 概率：0.25
# 	wifimac2 出现1次   wifimac2 概率：0.25
# 	wifimac3 出现2次   wifimac3 概率：0.5
# deviceId1下wifimac熵值：-0.25*log2(0.25) - 0.25*log2(0.25) - 0.5*log2(0.5)
#
# url:
# """


class Solution:
    def que1(self, a):
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
