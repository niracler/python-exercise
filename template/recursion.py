MAX_LEVEL = None


def process_data(level, data):
    pass


def reverse_state(level):
    pass


def recursion(level, param1, param2):
    """
    关于递归函数的模板，是可以有更多参数的
    :param level:递归的层级
    :param param1:参数1
    :param param2:参数2
    :return:
    """

    # 递归的终止条件
    if level > MAX_LEVEL:
        print("result")
        return

    # 在这一层你所需要做的事情
    process_data(level, param1)

    # 进入下一层
    recursion(level + 1, param1, param2)

    # 回来的时候要做的事情
    reverse_state(level)
