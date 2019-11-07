# """
# 题目：题目五. 输入两个JSON对象，第二个JSON对象是第一个JSON对象的类型描述（schema），
# 请写代码检查第一个对象（数据对象）是否满足第二个对象定义的类型要求。例如，
#
# 对于JSON对象：
# {
# “organization”:”shumei”,
# “type”: “tech”,
# “features”:{
#      “timestamp”: 1558031759,
#          “cities”:[“BeiJing”,”ShangHai”，“ShenZhen”],
#          “apps”:[{“name”:”TianWang”, “date”:”2018-01”},
#  {“name”:”TianJing”, “date”:”2016-01”}]
# }
# }
# 的类型描述是：
# {
#         "organization":"string",
#         "type":"string",
#         "features":{
#             "timestamp":"long",
#             "cities":["string"],
#             "apps":[{"name":"string", "date":"string"}]
#         }
# }
#
# 说明：假设在我们简化的类型系统中，仅支持以下类型
# 1. 基础类型：字符串(string)，整数(long)
# 2. 复合类型：数组([])，对象({})
#
# 请写代码实现函数
# boolean type_check(const json &data, const json &schema);
# 如果data满足schema的类型要求，返回true，否则返回false
#
# 注：可以使用你熟悉的一个json库，也可以假设json对象支持如下操作:
# 1. obj[name]: 如果obj是个复合json对象，返回这个对象中名字叫name的字段值（也是json）
# 2. obj.has(name)：如果obj是个复合json对象，返回名字name是否是该对象的一个成员名
# 3. obj[i]：如果obj是个json数组，返回这个数组中下标为 i的元素。
# 4. obj.size()：如果obj是个json数组，返回该数组的大小
# 5. obj.type(): 返回当前json对象（原子对象或者复合对象）的类型，可能返回值“string”、“long”、“object”、“array”。
#
# url:
# """


class Solution:
    def type_check(self, data, schema) -> bool:
        # 深度搜索

        return self._dfs(data, schema)

    def _dfs(self, data, schema):
        try:
            for key in data.keys():
                res = True
                if isinstance(data[key], dict):
                    res = self._dfs(data[key], schema[key])
                elif isinstance(data[key], list):
                    res = self.list_dfs(data[key], schema[key])
                else:
                    res = isinstance(data[key], schema[key])
                if not res:
                    return False
        except Exception as e:
            return False

        return True

    def list_dfs(self, data, schema):
        try:
            for key in range(len(data)):
                res = True
                if isinstance(data[key], dict):
                    res = self._dfs(data[key], schema[0])
                elif isinstance(data[key], list):
                    res = self.list_dfs(data[key], schema[0])
                else:
                    res = isinstance(data[key], schema[0])
                if not res:
                    return False
        except Exception as e:
            return False

        return True


if __name__ == '__main__':
    data = {
        "organization": "shumei",
        "type": "tech",
        "features": {
            "timestamp": 1558031759,
            "cities": ["BeiJing", "ShangHai", "ShenZhen"],
            "apps": [
                {"name": "TianWang", "date": "2018 - 01"},
                {"name": "TianJing", "date": "2016 - 01"}
            ]
        }
    }

    schema = {
        "organization": str,
        "type": str,
        "features": {
            "timestamp": int,
            "cities": [str],
            "apps": [{"name": str, "date": int}]
        }
    }

    solution = Solution()
    result = solution.type_check(data, schema)
    print(result)

# """
# 分析:
#
# """
