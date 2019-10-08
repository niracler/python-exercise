def prepare_data(problem):
    pass


def split_problem(problem, data):
    pass


def process_result(subresult1, subresult2, subresult3):
    pass


def divide_conquer(problem, param1, param2):
    """
    关于分治问题的函数模板，可以更多参数
    :param problem:
    :param param1:
    :param param2:
    :return:
    """

    # 结束条件
    if problem is None:
        print('result')
        return

    # 准备数据，并将大问题转换为小问题
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # 对问题进行分治，并得出子结果
    subresult1 = divide_conquer(subproblems[0], param1, param2)
    subresult2 = divide_conquer(subproblems[1], param1, param2)
    subresult3 = divide_conquer(subproblems[2], param1, param2)

    # 将子结果进行合并再返回
    result = process_result(subresult1, subresult2, subresult3)
    return result