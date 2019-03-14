#
#
# def get_directory_contents(s_path):
#    """
#    返回该文件夹中文件的路径,以及其包含文件夹中文件的路径
#    :param s_path: 文件夹的路径
#    :return: 返回该文件夹中文件的路径,以及其包含文件夹中文件的绝对路径
#    """
#    pass


import os


def get_directory_contents(s_path):
    """
    返回该文件夹中文件的路径,以及其包含文件夹中文件的路径
    :param s_path: 文件夹的路径
    :return: 返回该文件夹中文件的路径,以及其包含文件夹中文件的绝对路径
    """

    # 假如是相对路径的话,要加上当前路径
    if s_path[0] != "/":
        s_path = os.path.join(os.getcwd(), s_path)

    # 递归一层一层地遍历文件夹
    for cur_dir in os.listdir(s_path):
        cur_dir = os.path.join(s_path, cur_dir)
        if os.path.isdir(cur_dir):
            get_directory_contents(cur_dir)
        else:
            print(cur_dir)


if __name__ == '__main__':
    # print(get_directory_contents("/home/niracler/PycharmProjects/python-exercise"))
    get_directory_contents("../venv")
