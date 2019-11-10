visited = set()


def dfs(node, visited):
    """
    :param node:当前要处理的节点
    :param visited:访问过的节点
    :return:
    """
    visited.add(node)

    # 在当前节点要做的事情

    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)

